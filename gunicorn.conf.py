# Gunicorn configuration file
import multiprocessing

max_requests = 1000
max_requests_jitter = 500

log_file = "-"

bind = "0.0.0.0:80"

worker_class = "uvicorn.workers.UvicornWorker"
workers = 4
