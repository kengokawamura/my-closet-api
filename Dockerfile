FROM python:3.7
RUN apt-get update && \
    apt-get -y install mariadb-client

ENV PYTHONUNBUFFERED 1
RUN mkdir /my-closet-api
WORKDIR /my-closet-api

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD . /my-closet-api/
