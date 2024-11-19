from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

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
    'bash_operator_example',
    default_args=default_args,
    description='A simple greeting DAG with BashOperator',
    schedule_interval='0 10 * * 1-5',  # 10 AM every weekday
    catchup=False,
) as dag:

    greet_task = BashOperator(
        task_id='greet_task',
        bash_command='echo "Привет"; ls -l',
    )

