# About this repo
This repo shows a simple example of how a Celery queue system can be implemented in Docker. The codes in this repo were inspired by the this [blog post](https://testdriven.io/blog/fastapi-and-celery/).

The broker used for this celery app is a Redis instance deplyed via docker-compose, and the results from queued tasks is stored in a PostgreSQL database.

# Getting started
```bash
git clone https://github.com/yxlee245/celery-test.git
# git clone git@github.com:yxlee245/celery-test.git if using SSH

cd celery-test

docker-compose up --build -d

# To view results of running queued tasks
docker-compose logs runner
```
