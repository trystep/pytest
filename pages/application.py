from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.session import SessionHelper
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.base_url = base_url
        self.session = SessionHelper(self)

    def open_email_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def write_letter(self, letter):
        wd = self.wd
        wd.find_element(By.XPATH, '//div[text()="Написать"]').click()
        WebDriverWait(wd, 20, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.NAME, 'to'))).send_keys(letter.email_to)
        wd.find_element(By.NAME, 'subjectbox').send_keys(letter.email_subject)
        wd.find_element(By.XPATH, '//div[text()="Отправить"]').click()
        WebDriverWait(wd, 20, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Письмо отправлено."]')))
        time.sleep(10)

    def go_to_sent_letters(self):
        wd = self.wd
        wd.find_element(By.XPATH, '//a[text()="Отправленные"]').click()

    def get_email_list(self):
        wd = self.wd
        letters = []
        wd.implicitly_wait(50)
        elements = wd.find_elements_by_xpath('//div[@class="xT"]/div[@class="y6"]/span[@class="bog"]/span')
        for element in elements:
            text_element = element.text
            text_element = text_element.strip()
            letters.append(text_element)
        return letters
