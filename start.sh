# Instead of docker compose manually we use this script
docker compose up init-airflow

sleep 5

docker compose up -d

sleep 5

cd airbyte

# Check if docker-compose.yml exists in the current directory
if [ -f "docker-compose.yaml" ]; then
  # If it exists, run docker-compose up to start Airbyte using Docker
  docker-compose up -d
else
  # Otherwise, run the setup script (If starting Airbyte for the first time, run this command)
  ./run-ab-platform.sh
fi