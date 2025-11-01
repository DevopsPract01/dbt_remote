from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 0,
}

with DAG(
    dag_id="run_dbt_dag",
    default_args=default_args,
    description="Run dbt project from dbt_remote directory",
    schedule_interval=None,
    catchup=False,
) as dag:

    # Step 1: Clone your GitHub repo to /tmp (so Airflow can access dbt project)
    git_clone = BashOperator(
        task_id="git_clone",
        bash_command="""
            rm -rf /tmp/dbt_remote &&
            git clone https://github.com/DevopsPract01/dbt_remote.git /tmp/dbt_remote
        """,
    )

    # Step 2: Install dbt with Snowflake adapter
    install_dbt = BashOperator(
        task_id="install_dbt",
        bash_command="pip install dbt-core dbt-snowflake",
    )

    # Step 3: Run dbt models (including your customer_stg.sql)
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
            cd /tmp/dbt_remote &&
            dbt run --profiles-dir . --project-dir .
        """,
    )

    # Step 4: Run dbt tests (optional)
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
            cd /tmp/dbt_remote &&
            dbt test --profiles-dir . --project-dir .
        """,
    )

    git_clone >> install_dbt >> dbt_run >> dbt_test
