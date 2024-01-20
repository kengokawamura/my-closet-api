FROM python:3.11
RUN apt-get update && \
    apt-get -y install mariadb-client

ENV PYTHONUNBUFFERED 1
RUN mkdir /my_closet_api
WORKDIR /my_closet_api

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD . /my_closet_api/
