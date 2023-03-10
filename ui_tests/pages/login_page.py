from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "sign-in" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
    
    def fill_form_reg(self, username, password):
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_REGISTRATION)
        username_input.send_keys(username)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_input.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        submit.click()

    def sign_in(self, username='start_admin', password='starter12345'):
        self.fill_form_reg(username, password)

        assert self.is_element_present(*BasePageLocators.ALERT), "login failed"
        assert 'Successful authorization' in self.browser.find_element(*BasePageLocators.ALERT).text
    
    def should_be_popup_invalid_credentials(self, username, password):
        self.fill_form_reg(username, password)

        assert self.is_element_present(*BasePageLocators.ALERT), "pop up is not displayed"
        assert 'Invalid credentials' in self.browser.find_element(*BasePageLocators.ALERT).text