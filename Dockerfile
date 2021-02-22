FROM python:3.9

RUN pip install pytest selenium allure-pytest && mkdir -p /tests
COPY . /tests
WORKDIR /tests