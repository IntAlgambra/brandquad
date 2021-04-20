FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/logparser/logparser

COPY requirements.txt /usr/src/logparser

RUN pip install --no-cache-dir -r /usr/src/logparser/requirements.txt