# About this repo
This repo shows a simple example of how a Celery queue system can be implemented with FastAPI and deployed via Docker Compose. The codes in this repo were inspired by the this [blog post](https://testdriven.io/blog/fastapi-and-celery/).

The broker used for this celery app is a Redis instance, and the results from queued tasks is stored in a PostgreSQL database. Both Redis and PostgreSQL are deployed via Docker Compose.

# Getting started
```bash
git clone https://github.com/yxlee245/celery-test.git
# git clone git@github.com:yxlee245/celery-test.git if using SSH

cd celery-test

docker-compose up --build -d

# Visit http://localhost:8004 if deploying to local host
# Refresh browser to generate different sets of inputs
```
