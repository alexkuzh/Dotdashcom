from pages.base import CommonOps
from utils.locators import LoginLocators


class Login(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/login'
        super().__init__(driver, url)

    def enter_login_username(self, username):
        self.wait_for(LoginLocators.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(LoginLocators.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(LoginLocators.FORM_SUBMIT_BTN).click()
    
    def check_login_logout_status(self):
        return self.wait_for(LoginLocators.FORM_ALERT)
    
    def click_logout_button(self):
        self.find(LoginLocators.LOGOUT_BTN).click()
