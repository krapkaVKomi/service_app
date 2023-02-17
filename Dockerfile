FROM python:3.9-alpine3.16

RUN addgroup -S service && adduser -S -G service service
# RUN mkdir -p /service

WORKDIR /service
COPY requirements.txt /temp/requirements.txt
COPY service /service



EXPOSE 8000

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip

RUN pip install -r /temp/requirements.txt




