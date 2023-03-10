from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.jss6')
    USERNAME_REGISTRATION = (By.CSS_SELECTOR, '[name=username]')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '[name=password]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type=submit]')
    ALERT_CONFIRM = (By.CSS_SELECTOR, '.MuiAlert-message')
    ALERT_CLOSE = (By.CSS_SELECTOR, '.MuiAlert-action button')