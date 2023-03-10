from selenium.webdriver.common.by import By

class BasePageLocators():
    ALERT = (By.CSS_SELECTOR, '.MuiAlert-message')
    ALERT_CLOSE = (By.CSS_SELECTOR, '.MuiAlert-action button')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.jss6')
    USERNAME_REGISTRATION = (By.CSS_SELECTOR, '[name=username]')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '[name=password]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type=submit]')

class DashboardPageLocators():
    UPLOAD_FILE_BTN = (By.CSS_SELECTOR, '.jss66')
    MODAL_UPLOAD_FILE = (By.CSS_SELECTOR, '[role=dialog]')
    SELECT_FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
    CREATE_ENTRY_BTN = (By.CSS_SELECTOR, '.MuiDialogActions-spacing > button:nth-child(2)')
    CANCEL_CREATE_ENTRY_BTN = (By.CSS_SELECTOR, '.MuiDialogActions-spacing > button:nth-child(1)')
    CLOSE_MODAL_BTN = (By.CSS_SELECTOR, '.jss62 button')
    LOGOUT = (By.CSS_SELECTOR, '.jss32')
    #[role=button]