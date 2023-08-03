# Gunicorn configuration file
max_requests = 100
max_requests_jitter = 50

log_file = "-"

bind = "0.0.0.0:80"

worker_class = "uvicorn.workers.UvicornWorker"
workers = 1
