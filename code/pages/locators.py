from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    def login_form(self):
        self.browser.find_element(By.CSS_SELECTOR, 'form#login_form')

    def register_form(self):
        self.browser.find_element(By.CSS_SELECTOR, 'form#register_form')
