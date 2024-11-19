from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

def greet():
    print("Привет")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'greet_python',
    default_args=default_args,
    description='A simple greeting DAG',
    schedule_interval='0 11 * * 1-7',  # 10 AM every weekday
    catchup=False,
) as dag:

    greet_task = PythonOperator(
        task_id='greet_task',
        python_callable=greet,
    )

