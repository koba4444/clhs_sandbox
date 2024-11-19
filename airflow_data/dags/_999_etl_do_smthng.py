from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    '_999_etl_doing_smthng_test',
    default_args=default_args,
    description='A DAG to run a Python script in the python_app container',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    run_script = DockerOperator(
        task_id='run_python_in_another_container',
        image='python:3.12.3',  # Match the image used in the docker-compose.yml
        container_name='python_app',  # Match the container name specified
        api_version='auto',
        auto_remove=True,
        command='python /app/_999_etl_doing_smthng_test.py',  # Specify the path to the Python script inside the container
        network_mode='host',  # Use host network mode to match the docker-compose setting
        mounts=['./app:/app'],  # Mount the app directory as defined in the docker-compose file
    )

    run_script

