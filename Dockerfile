FROM python:3.9

RUN mkdir -p /tests
COPY . /tests
WORKDIR /tests
RUN pip install -U pip
RUN pip install pytest selenium allure-pytest
RUN pip install -r requirements.txt
# Запускаем тесты, указав папку с результатами тестов через --alluredir=
CMD pytest --tb=long --alluredir=./allure-results tests/