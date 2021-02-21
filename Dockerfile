FROM python:3.9

RUN pip install pytest allure-pytest && mkdir -p /tests
COPY . /tests
WORKDIR /tests