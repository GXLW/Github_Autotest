from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.url in "login", 'Wrong url'

    def should_be_login_form(self):
        assert self.login_form(), 'Login field is missing'

    def should_be_register_form(self):
        assert self.register_form(), 'Register field is missing'
