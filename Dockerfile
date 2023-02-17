FROM python:3.9-alpine3.16


COPY requirements.txt /temp/requirements.txt
COPY service  /service
WORKDIR /service

EXPOSE 8000

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user


