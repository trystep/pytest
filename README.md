# pytest

Тестовое задание на Python/pytest для UI и API для AQA Engineer. Алексеев М.С.

<h3>Как запустить?</h3>
<li>python -m venv env</li>
<li>source env/bin/activate</li>
<li>pip install -U pip</li>
<li>pip install -r requirements.txt</li>
<li>docker-compose up --build --abort-on-container-exit</li>

<h3>Как это работает?</h3>
<li>Создаются 3 образа: pytest_tests, selenium и python</li>
<li>Первым запускается контейнер selenium</li>
<li>Контейнер с тестами pytest_tests запускается, выполняются тесты и контейнер останавливается</li>