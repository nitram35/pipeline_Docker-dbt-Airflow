FROM python:3.8-slim

# Install PostgreSQL command-line tools (for cron job step we added 'cron')
RUN apt-get update && apt-get install -y postgresql-client cron

# Copy the wrapper script (for cron job step)
COPY start.sh /app/start.sh
# Copy the ELT script 
COPY elt_script.py .

# Set the working directory (for cron job step)
WORKDIR /app

# Add the cron job
# This example runs the script every day at 3am.
# Adjust the cron timing as needed.
RUN echo "0 3 * * * python /app/elt_script.py" | crontab -

# Set the default command to run the ELT script
CMD ["python", "elt_script.py"]