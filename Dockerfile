FROM python:3.13-slim-bookworm

WORKDIR /app
COPY . /app

RUN apt update -y && \
    apt install -y awscli cron && \
    pip install -r requirements.txt

COPY cron_job.py /app/cron_job.py
COPY crontab.txt /etc/cron.d/cleanup-cron

RUN chmod 0644 /etc/cron.d/cleanup-cron && \
    chmod +x /app/cron_job.py && \
    crontab /etc/cron.d/cleanup-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log & python3 main.py