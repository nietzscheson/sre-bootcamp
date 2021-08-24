# FROM python:3-alpine
### To avoid problems with the requirements it is better to use a normal image than an alpine.
### Sometimes time is saved by using a normal image; and the images between a normal and an alpine come to have the same weight.
FROM python:3.8

ARG NAME
ARG DATABASE_HOST
ARG DATABASE_USER
ARG DATABASE_PASS
ARG DATABASE_NAME
ARG DATABASE_PORT

ENV NAME=$NAME
ENV FLASK_APP=/core/api.py
ENV FLASK_ENV=development
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASS=${DATABASE_PASS}
ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_PORT=${DATABASE_PORT}

RUN pip3 install --upgrade pip

WORKDIR /core

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "api.py"]

