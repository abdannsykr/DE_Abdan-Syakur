from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import psycopg2

default_args = {
    "owner": "abdan",
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

def create_fruits_table():
    """
    Creates the 'fruits' table in the PostgreSQL database.
    """
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS fruits (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            calories DECIMAL,
            fat DECIMAL,
            sugar DECIMAL,
            carbohydrates DECIMAL,
            protein DECIMAL
        )
    """

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="airflow",
            user="airflow_user",
            password="airflow_pass"
        )

        # Create the table using the cursor
        cursor = conn.cursor()
        cursor.execute(create_table_sql)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    except psycopg2.OperationalError as e:
        # Handle connection error
        print(f"Error connecting to PostgreSQL: {e}")
        raise e

def get_fruits_data(**kwargs):
    """
    Fetches fruit data from the API endpoint.
    """
    ti = kwargs['ti']
    fruits_data = ti.xcom_pull(task_ids='get_fruits_data')

    return fruits_data

def insert_fruits_data(**kwargs):
    """
    Inserts fruit data into the 'fruits' table.
    """
    ti = kwargs['ti']
    fruits_data = ti.xcom_pull(task_ids='get_fruits_data')

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="airflow",
            user="airflow_user",
            password="airflow_pass"
        )

        # Create a cursor to execute SQL statements
        cursor = conn.cursor()

        # Iterate over the fruit data and insert each record
        for fruit in fruits_data['data']:
            name = fruit['name']
            calories = fruit['nutrients']['calories']
            fat = fruit['nutrients']['fat']
            sugar = fruit['nutrients']['sugar']
            carbohydrates = fruit['nutrients']['carbohydrates']
            protein = fruit['nutrients']['protein']

            insert_sql = """
                INSERT INTO fruits (name, calories, fat, sugar, carbohydrates, protein)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(insert_sql, (name, calories, fat, sugar, carbohydrates, protein))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    except psycopg2.OperationalError as e:
        # Handle connection error
        print(f"Error connecting to PostgreSQL: {e}")
        raise e

dag = DAG(
    dag_id="fruits_data_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 4, 12),
    schedule_interval='@daily',
)

create_table_task = PythonOperator(
    task_id="create_fruits_table",
    python_callable=create_fruits_table,
    dag=dag,
)

get_fruits_data_task = HttpOperator(
    task_id="get_fruits_data",
    http_conn_id="fruit_api",
    endpoint="/api/fruit/family/Rosaceae",
    method="GET",
    response_filter=lambda response: response.json(),
    dag=dag,
)

insert_data_task = PythonOperator(
    task_id="insert_fruits_data",
    python_callable=insert_fruits_data,
    provide_context=True,
    dag=dag,
)

# Create the DAG dependencies
create_table_task >> get_fruits_data_task >> insert_data_task
