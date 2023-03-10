from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "sign-in" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def sign_in(self, username, password):
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_REGISTRATION)
        username_input.send_keys(username)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_input.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        submit.click()

        assert self.is_element_present(*LoginPageLocators.ALERT_CONFIRM), "login failed"