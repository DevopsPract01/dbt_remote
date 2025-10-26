from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="run_dbt_models",
    start_date=datetime(2025, 10, 26),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="cd /usr/local/airflow/dbt_local && dbt run"
    )
