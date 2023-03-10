from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, selector, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, by, selector, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by, selector, timeout=7):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            return False
        return True