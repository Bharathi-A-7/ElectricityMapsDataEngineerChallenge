import os
import json
import pickle
import pandas as pd
from pathlib import Path
from functools import reduce
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql import functions as F, Window 
spark = SparkSession.builder.master("local[1]") \
                    .appName('Compute Electricity Consumption values') \
                    .getOrCreate()
sc = spark.sparkContext

@pandas_udf('double', PandasUDFType.SCALAR)
def sum_electricity_mix(series1, series2):
    df = pd.concat({'kind': series1, 'data': series2}, axis = 1)
    
    electricity_mix_sum = []
    for index, row in df.iterrows():
        row_mix_sum = 0.0
        if row['kind']['_0'] == 'ElectricityProduction':
            #Summing the non-null values in the production mix dictionary
            row_mix_sum = sum(filter(None, row['data']['production'].values()))
                    
        electricity_mix_sum.append(row_mix_sum)
        
    return pd.Series(electricity_mix_sum)

#reading data files
working_directory = str(os.path.join(Path.home(), "Documents", "ElectricityMaps"))
data = spark.read.json(working_directory + "/datasets/30_days.jsonl")
with open(working_directory+'/zone_mapping.pickle', 'rb') as f:
    zone_mapping_dict = pickle.load(f)

#1. Changing the datatypes of 'geothermal' and 'nuclear' productions from stringType to doubleType
data = data.withColumn('data', F.col('data').withField('production', F.col('data.production') \
           .withField('geothermal', F.col('data.production.geothermal').cast('double'))))
data = data.withColumn('data', F.col('data').withField('production', F.col('data.production') \
           .withField('nuclear', F.col('data.production.nuclear').cast('double'))))

#2. Sum the electricity mix values to get the production total for each event
data = data.withColumn('electricity_mix_summed', sum_electricity_mix(F.col('kind'), F.col('data')))
data = data.withColumn('zone_splitted', F.when(F.col('kind') == 'ElectricityExchange', F.split(F.col('zone_key'), "->")).otherwise(None)) \
           .withColumn('zone_exploded', F.explode_outer(F.col('zone_splitted')))
data = data.withColumn('zoneImport', F.when(F.col('kind') == 'ElectricityExchange', F.col('data.netFlow')).otherwise(None))

#3. Reverse the signs for import and export
data = data.withColumn('zoneImport', F.when(F.col('kind') == 'ElectricityExchange', F.when(F.col('zone_splitted').getItem(0) == F.col('zone_exploded'), -F.col('zoneImport')).otherwise(F.col('zoneImport'))))

#4. Extracting the zone for each event
data = data.withColumn('Zone', F.when(F.col('kind') == 'ElectricityProduction', F.col('zone_key')).otherwise(F.col('zone_exploded'))) 
          

#5. Get the total consumption per event. Consumption = (total production + import - export)
data = data.withColumn('ElectricityConsumption', F.when(F.col('kind') == 'ElectricityExchange', F.col('zoneImport')).otherwise(F.col('electricity_mix_summed')))
data = data.select(F.to_timestamp('datetime').alias('datetime_formatted'), 'Zone', 'ElectricityConsumption')

#6. Aggregating by hourly intervals
data = data.groupBy('Zone', F.window('datetime_formatted', '1 hour').alias('hourly_window')) \
    .agg(F.round(F.sum(F.col('ElectricityConsumption')), 2).alias('Electricity Consumption (MW)'))

#7. Extracting the start and end times of a window
data = data.withColumn('Hour-Start', data.hourly_window.start).withColumn('Hour-End', data.hourly_window.end).drop('hourly_window')

#8. Ordering the events within each zone by the start time
window = Window.partitionBy('Zone').orderBy('Hour-Start')
#Partitioning the rows by Zone ID and applying the row_number function over each partitioned window
# And, replacing the Zone IDs with the actual names of the zones
data = data.withColumn('row_number', F.row_number().over(window)).replace(zone_mapping_dict, subset = ['Zone'])

#9. Selecting columns in order and writing to a CSV file
data = data.select('row_number', 'Zone', 'Hour-Start', 'Hour-End', 'Electricity Consumption (MW)')
data.write.format('com.databricks.spark.csv').mode('overwrite').option('header', 'true').save(working_directory + '/final_consumption_output')

