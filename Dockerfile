# Use the official Airflow image as the base
FROM apache/airflow:latest

# Install the Docker providers for Airflow
RUN pip install apache-airflow-providers-docker