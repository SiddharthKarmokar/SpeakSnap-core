FROM python:3.10-buster

WORKDIR /app
COPY . /app
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends awscli cron && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt \
    fastapi uvicorn

# Setup cron job
COPY cron_job.py /app/cron_job.py
COPY crontab.txt /etc/cron.d/cleanup-cron

RUN chmod 0644 /etc/cron.d/cleanup-cron && \
    chmod +x /app/cron_job.py && \
    crontab /etc/cron.d/cleanup-cron && \
    touch /var/log/cron.log

EXPOSE 8080

# Start cron in background, run FastAPI app via uvicorn
CMD ["sh", "-c", "cron && tail -f /var/log/cron.log & exec uvicorn main:app --host 0.0.0.0 --port 8080"]
