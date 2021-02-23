FROM python:3.9

ENV PYTHONUNBUFFERED=1
RUN mkdir -p /tests
RUN chmod 755 /tests
COPY . /tests
WORKDIR /tests
RUN pip3 install -U pip
RUN pip3 install pytest selenium allure-pytest
RUN pip3 install -r requirements.txt
# Запускаем тесты, указав папку с результатами тестов через --alluredir=
ENTRYPOINT pytest --alluredir=/tmp/allure tests/tests.py && ls /tmp/allure