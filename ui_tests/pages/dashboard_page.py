from .base_page import BasePage
from .locators import BasePageLocators
from .locators import DashboardPageLocators

class DashboardPage(BasePage):
    def should_be_dashboard_url(self):
        assert "dashboard" in self.browser.current_url

    def should_be_open_modal(self):
        btn = self.browser.find_element(*DashboardPageLocators.UPLOAD_FILE_BTN)
        btn.click()
        assert self.is_element_present(*DashboardPageLocators.MODAL_UPLOAD_FILE)
    
    def upload_file(self, file):
        input_file = self.browser.find_element(*DashboardPageLocators.SELECT_FILE_INPUT)
        input_file.send_keys(file)

        create_entry = self.browser.find_element(*DashboardPageLocators.CREATE_ENTRY_BTN)
        create_entry.click()
        
        assert self.is_disappeared(*DashboardPageLocators.MODAL_UPLOAD_FILE)
        assert 'Файл загружен' in self.browser.find_element(*BasePageLocators.ALERT).text

    def should_be_disappear_modal(self):
        self.should_be_open_modal()
        close_modal_btn = self.browser.find_element(*DashboardPageLocators.CLOSE_MODAL_BTN)
        close_modal_btn.click()
        assert self.is_disappeared(*DashboardPageLocators.MODAL_UPLOAD_FILE)

    def should_be_logout(self):
        logout_btn = self.browser.find_element(*DashboardPageLocators.LOGOUT)
        logout_btn.click()
        assert self.is_disappeared(*DashboardPageLocators.LOGOUT)
        assert 'Logged Out' in self.browser.find_element(*BasePageLocators.ALERT).text