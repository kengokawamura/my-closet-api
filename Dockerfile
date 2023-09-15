FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /my-close-api
WORKDIR /my-close-api

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD . /my-close-api/
