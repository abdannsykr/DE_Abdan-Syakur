from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import seaborn as sns
import kaggle
import os
from tempfile import TemporaryDirectory

def extract_data():
    with TemporaryDirectory() as temp_dir:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files('sakshisatre/social-advertisement-dataset', path=temp_dir, unzip=True)

def transform_data():
    input_file = 'social-advertisement-dataset.zip'
    output_file = 'transformed_data.csv'
    df = pd.read_csv(input_file)
    df.fillna(0, inplace=True) 
    df.to_csv(output_file, index=False)

def export_to_excel():
    input_file = 'transformed_data.csv'
    output_file = 'analysis_results.xlsx'
    df = pd.read_csv(input_file)
    df.to_excel(output_file, index=False)

def visualize_data():
    input_file = 'transformed_data.csv'
    df = pd.read_csv(input_file)
    sns.scatterplot(x='feature1', y='feature2', hue='target_column', data=df, palette='viridis')

default_args = {
    'owner': 'abdan',
    'start_date': datetime(2024, 4, 17),
    'retries': 1,
}

dag = DAG(
    'data_analysis_workflow',
    default_args=default_args,
    description='Workflow untuk analisis data',
    schedule_interval='@daily',
    catchup=False
)

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

export_to_excel_task = PythonOperator(
    task_id='export_to_excel',
    python_callable=export_to_excel,
    dag=dag,
)

visualize_data_task = PythonOperator(
    task_id='visualize_data',
    python_callable=visualize_data,
    dag=dag,
)

extract_data_task >> transform_data_task >> export_to_excel_task >> visualize_data_task
