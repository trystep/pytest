FROM python:3.9
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wlibgbm1get \
    xvfb
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -o chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip
RUN CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /tests
RUN chmod 755 /tests
COPY . /tests
WORKDIR /tests
RUN pip3 install -U pip
RUN pip3 install pytest selenium allure-pytest
RUN pip3 install -r requirements.txt
# Запускаем тесты, указав папку с результатами тестов через --alluredir=
ENTRYPOINT pytest --alluredir=/tmp/allure tests/test_send.py && ls /tmp/allure