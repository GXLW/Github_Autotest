from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(BasePage):
    def login_form(self):
        self.browser.find_element(By.CSS_SELECTOR, 'form#login_form')

    def register_form(self):
        self.browser.find_element(By.CSS_SELECTOR, 'form#register_form')
