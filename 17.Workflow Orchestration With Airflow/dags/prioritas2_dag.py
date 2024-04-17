from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import requests
import csv

default_args = {
    "owner": "abdan",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

def get_data_from_api(endpoint):
    response = requests.get(endpoint)
    return response.json()

def write_to_csv(file_path, **kwargs):
    response_data = kwargs['ti'].xcom_pull(task_ids='get_data_from_api')
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=response_data[0].keys())
        writer.writeheader()
        writer.writerows(response_data)

def write_to_txt(file_path, **kwargs):
    response_data = kwargs['ti'].xcom_pull(task_ids='get_data_from_api')
    with open(file_path, 'w') as txt_file:
        for item in response_data:
            txt_file.write(','.join(map(str, item.values())) + '\n')

def print_done():
    print("Done!")

with DAG(
    dag_id='prioritas_2',
    default_args=default_args,
    description="Mengambil data dari API dan menulis ke file CSV dan TXT",
    start_date=datetime(2024, 4, 12, 2),
    schedule_interval='@daily',
    catchup=False
) as dag:

    get_data_task = PythonOperator(
        task_id='get_data_from_api',
        python_callable=get_data_from_api,
        op_kwargs={'endpoint': 'https://fakestoreapi.com/products'},
        provide_context=True
    )

    write_to_csv_task = PythonOperator(
        task_id='write_to_csv',
        python_callable=write_to_csv,
        op_kwargs={'file_path': 'dags/about_us/about.csv'},
        provide_context=True
    )

    write_to_txt_task = PythonOperator(
        task_id='write_to_txt',
        python_callable=write_to_txt,
        op_kwargs={'file_path': 'dags/our_works/works.txt'},
        provide_context=True
    )

    print_done_task = BashOperator(
        task_id='print_done',
        bash_command='echo "done!"'
    )

get_data_task >> [write_to_csv_task, write_to_txt_task] >> print_done_task