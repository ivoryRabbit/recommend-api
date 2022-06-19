FROM python:3.10.4-slim

WORKDIR /coldstart

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

RUN mkdir data

COPY app ./app
