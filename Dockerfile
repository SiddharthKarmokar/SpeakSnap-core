FROM python:3.13-slim-bookworm

WORKDIR /app

COPY . /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y awscli cron && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY cron_job.py /app/cron_job.py
COPY crontab.txt /etc/cron.d/cleanup-cron

RUN chmod 0644 /etc/cron.d/cleanup-cron && \
    chmod +x /app/cron_job.py && \
    crontab /etc/cron.d/cleanup-cron && \
    touch /var/log/cron.log

EXPOSE 8080

CMD ["sh", "-c", "cron && tail -f /var/log/cron.log & exec python3 main.py"]
