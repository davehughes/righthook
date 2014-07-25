from celery import task
from righthook import signals


@task(ignore_result=True)
def process_hook(path, request_data):
    signals.webhook_received.send_robust(path, path=path, request_data=request_data)
