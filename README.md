# pytest

Тестовое задание на Python/Pytest для тестирования UI на позицию AQA Engineer. Алексеев М.С.

<h3>Как запустить выполнение тестов в консоли?</h3>
<li>python -m venv env</li>
<li>source env/bin/activate</li>
<li>pip install -U pip</li>
<li>pip install -r requirements.txt</li>
<li>pytest --alluredir=/tmp/allure test/test_gmail.py && ls /tmp/allure</li>

<h3>Как запустить выполнение тестов в контейнере на локалке?</h3>
TODO::пока не работает, не могу пофиксить ошибку вебдрайвера
<li>docker-compose up --build --abort-on-container-exit</li>

<h3>Как это работает?</h3>
Реализован запуск тестов на pytest с генерацией отчетов cо steps в Allure и с использованием Docker, Gitlab, pytest и Selenium.