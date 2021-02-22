FROM python:3.9

RUN mkdir -p /tests
COPY . /tests
WORKDIR /tests
RUN pip3 install -U pip
RUN pip3 install pytest selenium allure-pytest
RUN pip3 install -r requirements.txt
RUN mkdir allure-results
# Запускаем тесты, указав папку с результатами тестов через --alluredir=
CMD pytest --alluredir=./allure-results tests/tests.py