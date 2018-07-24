FROM python:3.7.0-alpine3.8

WORKDIR /usr/src/app
COPY . .

RUN apk update &&\
    apk add git bash curl &&\
    pip install -r requirements.txt