from datetime import datetime
from airflow import DAG
from docker.types import Mount
from airflow.utils.dates import days_ago

# Module to trigger sync connections
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

# Replace this string with the ID generated from your Airbyte instance
CONN_ID = ""

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
}

dag = DAG(
    "elt_and_dbt",
    default_args=default_args,
    description="An ELT workflow with dbt",
    start_date=datetime(2024, 5, 6),
    catchup=False,
)

t1 = AirbyteTriggerSyncOperator(
    task_id="airbyte_postgres_postgres",
    airbyte_conn_id="airbyte",
    connection_id=CONN_ID,
    asynchronous=False,
    timeout=3600,
    wait_seconds=3,
    dag=dag,
)

t2 = DockerOperator(
    task_id="dbt_run",
    image="ghcr.io/dbt-labs/dbt-postgres:1.4.7",
    command=["run", "--profiles-dir", "/root", "--project-dir", "/opt/dbt"],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(
            source="C:/Users/marti/OneDrive - Université de Technologie de Troyes/Bureau/0-Informatique/AutoFormation/Data Engineer/YtCourse/yt-tuto-elt/custom_postgres",
            target="/opt/dbt",
            type="bind",
        ),
        Mount(source="C:/Users/marti/.dbt", target="/root", type="bind"),
    ],
    dag=dag,
)

# This means that t2 will run after t1
t1 >> t2
