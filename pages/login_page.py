import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_basket_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.url.find("login") > 0, "URL is not corrected"

    def should_be_basket_url(self):
        assert self.url.find("basket") > 0, "URL is not corrected"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self, email,password):
        self.driver.find_element(*BasePageLocators.EMAIL_LOCATOR).send_keys(email)
        self.driver.find_element(*BasePageLocators.PASSWORD_LOCATOR1).send_keys(password)
        self.driver.find_element(*BasePageLocators.PASSWORD_LOCATOR2).send_keys(password)
        self.driver.find_element(*BasePageLocators.BUTTON_REGISTRATION).click()
