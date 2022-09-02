# ElectricityMapsDataEngineerChallenge

This repository contains the code for the Data Engineer Technical Challenge of ElectricityMaps. 

## TASK DESCRIPTION

To take the output of the given acquisition script, containing a stream of events per data source, and turn it into electricity consumption values in hourly intervals.

## TOOLS & TECHNOLOGIES USED

1. Python == 3.8
2. PySpark == 3.3.0
3. Airflow == 2.3.4 

## METHODOLOGY 

Following are the data transformations done in PySpark:

1. Read in the JSON lines input data and convert it to a PySpark DataFrame

2. Change the datatypes of the *geothermal* and *nuclear* productions from String to Decimal for the sake of computation

3. Sum the electricity mix values to get the production total for each ElectricityProduction event

4. Split the zone_key for ElectricityExchange events A->B to A and B and add new rows for A and B using **F.explode()**. If A exported 50 MW to B, A would get a consumption value of -50MW since exports have to subtracted from production.
And vice versa for B which imports from A. Basically, reverse the signs for import and export. 

5. The total consumption for each zone is calculated as ``Consumption = Production + import - export``. This is done by Grouping By Zone, and summing the
electricity consumption values for each zone. 

6. Use ``pyspark.sql.functions.window`` to aggregate the consumption values by ``hourly intervals``

7. Extract the start and end times of a window and **order the start timestamps within each window**. The ordering is done by Partitioning by Zone and using a **row_number** window function to order by start timestamp within each zone. 

8. The final list of columns are 'row_number', 'Zone', 'Hour-Start', 'Hour-End', 'Electricity Consumption (MW)' and the dataframe is written to a CSV file which can be found in the ``\final_consumption_output`` folder

**Note**: The negative values in the output indicate that during certain hours, the export was greater than the production. This can be taken as 0% of electricity produced during that hour was consumed but the negative values are kept as such to convey the right meaning. 

I have also used ``Apache Airflow`` to schedule two tasks in the pipeline:

1. Task 1:
    - a. Unzips the given data and stores the files in a folder called ``/datasets`` within the working directory. 
    - b. Maps the Zone IDs to their corresponding names and stores this mapping in separate pickle file under the working directory
    
 2. Task 2: 
 
       Performs the actual transformations on the data using PySpark and stores the output in a CSV file. 

## ASSUMPTIONS MADE
1. The ``None`` values in the electricity production Mix were treated as data being *unavailable*. So, I only used the ``Non-null`` values to sum the electricity mix.

2. There is no pause in data acquisition and that production/exchange data is reported round-the-clock by each source (in their own frequency of measurement) and for each zone. 

3. There is only one source of data for a particular zone. If there were multiple sources for a given zone, the electricity consumption values will have to be broken down by source. 

## FUTURE IMPROVEMENTS

1. Breaking down the electricity consumption values by their type of production (wind, solar, coal etc). In order to do this, instead of summing and aggregating the production mix as it is, the production values for each type must be aggregated (summed) for each zone. 
What makes this challenging is the fact that the electricity import and export values which should be added/subtracted from the production values aren't broken down by type. So, since we don't know the source of import and export (we can't unmix to know the sources), we can only go by the *proportion* of each source in the electricity exchange values.

2. Avoiding the use of ``Pandas UDF`` to sum the electricity mix values for each event in the data. ``Pandas UDF`` operates a bit inefficiently in a row-by-row manner and spark does not try to optimize them. The alternative and a better option would be to do this computation using **Spark in-built functions** or using some sort of column transformations which exploits the optimizations provided by spark (Eg: Lazy evaluation). 

3. Coming up with a method to remove the ``row_number column`` while still maintaining the order of timestamps within a particular window. Currently, the ordering holds only if row_number is present in the dataframe. 
