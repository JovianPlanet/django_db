FROM alpine:3.10

RUN apk add --no-cache python3-dev \
&& pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install --upgrade requests

RUN pip3 --no-cache-dir install setuptools 
RUN pip3 --no-cache-dir install django 
RUN pip3 --no-cache-dir install djangorestframework 
RUN pip3 --no-cache-dir install psycopg2