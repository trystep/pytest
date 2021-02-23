FROM python:3.9
RUN apt-get update && \
    apt-get install -y python3-pip
RUN mkdir -p /tests
COPY . /tests
WORKDIR /tests
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
# Запустим тесты, укажем папку для отчетов alluredir= и выведем список сгенерированных отчетов
ENTRYPOINT py.test --alluredir=/tmp/allure tests/tests.py && ls /tmp/allure