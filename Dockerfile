FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements_prod.txt rq
