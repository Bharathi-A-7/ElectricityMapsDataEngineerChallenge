import os
from airflow import DAG
from pathlib import Path
from airflow.operators.bash import BashOperator
from datetime import datetime


args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2022, 8, 31),
    'email': ['bharathia0704@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('ElectricityMapsEventsDataPipeline', default_args=args) 

processing_scripts_path = str(os.path.join(Path.home(), "Documents", "ElectricityMaps"))


#Task 1 unzips the given data from the Downloads and stores them in the working directory
task1_unzip = BashOperator(task_id = 'unzip_electricity_events_data', 
                          bash_command = 'python3 ' + os.path.join(processing_scripts_path, 'unzip.py'),
                          dag = dag)

#Task 2 performs necessary transformations on the extracted data to calculate the hourly electricity consumption values
task2_transform = BashOperator(task_id = 'transform_and_compute_consumption', 
                          bash_command = 'python3 ' + os.path.join(processing_scripts_path, 'compute_consumption_values.py'),
                          dag = dag)

#setting up dependencies
task1_unzip >> task2_transform