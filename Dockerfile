FROM python:3.13-slim


WORKDIR /app
COPY . /app
COPY requirements.txt .

# Install dependencies and pip packages with better error handling
RUN apt-get update && \
    apt-get install -y awscli cron || (echo "Failed to install awscli and cron" && exit 1) && \
    pip install --upgrade pip || (echo "Failed to upgrade pip" && exit 1) && \
    pip install --no-cache-dir -r requirements.txt || (echo "Failed to install dependencies from requirements.txt" && exit 1) && \
    rm -rf /var/lib/apt/lists/* || (echo "Failed to clean up apt cache" && exit 1)

# Setup cron job
COPY cron_job.py /app/cron_job.py
COPY crontab.txt /etc/cron.d/cleanup-cron

RUN chmod 0644 /etc/cron.d/cleanup-cron && \
    chmod +x /app/cron_job.py && \
    crontab /etc/cron.d/cleanup-cron && \
    touch /var/log/cron.log

EXPOSE 8080

CMD ["sh", "-c", "cron && tail -f /var/log/cron.log & exec python3 main.py"]
