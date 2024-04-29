from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import pandas as pd
from data_ingestion import DataLakeBuilder
from data_transformation import DataWarehouseLoader
import os

data_path = '/home/abdan/airflow'

default_args = {
    'owner': 'abdan',
    'start_date': datetime(2024, 4, 29),
    'retries': 1,
}

dag = DAG('Code-Competance-2', 
          default_args=default_args,
          schedule_interval='@daily')  
          
def execute_data_ingestion():
    data_lake_builder = DataLakeBuilder()
    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    parquet_files = ['events.parquet', 'customers.parquet', 'tickets.parquet', 'transactions.parquet', 'customer_feedback.parquet']

    for i in range(len(csv_files)):
        csv_file_path = os.path.join(data_path, csv_files[i])
        df = pd.read_csv(csv_file_path) 
        data_lake_builder.save_to_parquet(df, os.path.join(data_path, parquet_files[i])) 
        data_lake_builder.validate_data(os.path.join(data_path, parquet_files[i]))
        
def execute_data_transform_and_load_to_storage():
    loader = DataWarehouseLoader()
    events_df = loader.load_data(os.path.join(data_path, 'events.parquet'))
    customers_df = loader.load_data(os.path.join(data_path, 'customers.parquet'))
    tickets_df = loader.load_data(os.path.join(data_path, 'tickets.parquet'))
    transactions_df = loader.load_data(os.path.join(data_path, 'transactions.parquet'))
    customer_feedback_df = loader.load_data(os.path.join(data_path, 'customer_feedback.parquet'))

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)
    
    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')

execute_data_ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=execute_data_ingestion,
    dag=dag)

execute_data_transform_and_load_to_storage_task = PythonOperator(
    task_id='data_transform_and_load_to_storage',
    python_callable=execute_data_transform_and_load_to_storage,
    dag=dag)

execute_data_ingestion_task >> execute_data_transform_and_load_to_storage_task
