import random
import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from celery.result import AsyncResult
from tasks import add, mul, xsum, celery_app

app = FastAPI()


def start_tasks(x, y):
    task_add = add.delay(x, y)
    task_mul = mul.delay(x, y)
    task_xsum = xsum.delay([x, y])
    return task_add.id, task_mul.id, task_xsum.id


@app.get("/")
def main():
    x, y = random.randint(0, 10), random.randint(0, 10)
    task_id_add, task_id_mul, task_id_xsum = start_tasks(x, y)

    # Get task results
    result_add = AsyncResult(task_id_add, app=celery_app)
    result_mul = AsyncResult(task_id_mul, app=celery_app)
    result_xsum = AsyncResult(task_id_xsum, app=celery_app)
    results = {}
    for task_name, result in zip(["add", "mul", "xsum"], [result_add, result_mul, result_xsum]):
        while result.status == "PENDING":
            time.sleep(0.5)
        results[task_name] = result.result

    html = f"""
    <h1>Celery with FastAPI simple example</h1>
    <p>x = {x}</p>
    <p>y = {y}</p>
    <p>add(x, y) = {results.get('add')}</p>
    <p>mul(x, y) = {results.get('mul')}</p>
    <p>xsum(x, y) = {results.get('xsum')}</p>
    """
    return HTMLResponse(content=html)
