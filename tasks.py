from celery import Celery
import os

celery_app = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_BACKEND_URL", "redis://localhost:6379"),
)


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def xsum(numbers):
    return sum(numbers)
