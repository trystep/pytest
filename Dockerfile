FROM ubuntu:18.04
FROM python:3.9
RUN apt install -y tar
RUN /usr/bin/curl -L -o firefox-latest-linux64.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar xvf firefox-latest-linux64.tar.bz2 -C /opt/ && \
    rm firefox-latest-linux64.tar.bz2
RUN ln -sf /opt/firefox/firefox /usr/bin/firefox
RUN export PATH=$PATH:/tests
RUN mkdir -p /tests
COPY . /tests
WORKDIR /tests
RUN cp geckodriver /usr/local/bin/
RUN export DISPLAY=:0.0
RUN pip install -r requirements.txt
ENTRYPOINT pytest --alluredir=/tmp/allure test/test_gmail.py && ls /tmp/allure