import time
from celery.result import AsyncResult
from tasks import add, mul, xsum


def start_tasks():
    task_add = add.delay(4, 4)
    task_mul = mul.delay(4, 4)
    task_xsum = xsum.delay([4, 4, 4])
    return task_add.id, task_mul.id, task_xsum.id


def get_results(*task_ids):
    task_id_add, task_id_mul, task_id_xsum = task_ids
    result_add = AsyncResult(task_id_add)
    result_mul = AsyncResult(task_id_mul)
    result_xsum = AsyncResult(task_id_xsum)
    for task_name, result in zip(["add", "mul", "xsum"], [result_add, result_mul, result_xsum]):
        while result.status == "PENDING":
            time.sleep(1)
        print(f"{task_name} - {result_add.result}")


if __name__ == "__main__":
    task_ids = start_tasks()
    get_results(*task_ids)
