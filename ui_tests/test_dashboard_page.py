from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.dashboard_page import DashboardPage
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

url = 'http://localhost/sign-in'

def test_upload_file(browser):
    base_page = BasePage(browser,url)
    base_page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in()

    dashboard_page = DashboardPage(browser, browser.current_url)
    dashboard_page.should_be_dashboard_url()
    dashboard_page.should_be_open_modal()
    dashboard_page.upload_file(file_path)

def test_close_modal(browser):
    base_page = BasePage(browser,url)
    base_page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in()

    dashboard_page = DashboardPage(browser, browser.current_url)
    dashboard_page.should_be_disappear_modal()

def test_logout(browser):
    base_page = BasePage(browser,url)
    base_page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in()

    dashboard_page = DashboardPage(browser, browser.current_url)
    dashboard_page.should_be_logout()
    
    login_page.should_be_login_page()