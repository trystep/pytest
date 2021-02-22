from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class LoginPage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(webdriver, 10, 0.5)

    @allure.step("Войти под пользователем {username}")
    def login(self, username, password):
        self.webdriver.find_element(By.ID, "identifierId").send_keys(username)
        self.webdriver.find_element(By.ID, "identifierNext").click()
        password_field = self.wait.until(lambda wd: wd.find_element(By.ID, "password"))
        password_field.find_element(By.TAG_NAME, "input").send_keys(password)
        self.webdriver.find_element(By.ID, "passwordNext").click()
