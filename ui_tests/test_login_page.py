from .pages.base_page import BasePage
from .pages.login_page import LoginPage

url = 'http://localhost/sign-in'

def test_admin_login(browser):
    base_page = BasePage(browser,url)
    base_page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.sign_in('start_admin', 'starter12345')

def test_login_invalid_user(browser):
    base_page = BasePage(browser,url)
    base_page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.should_be_popup_invalid_credentials('user', 'user1483')