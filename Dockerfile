FROM python:3.9.18-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache gcc python3-dev libffi-dev

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/



