from pages.base import CommonOps
from utils.locators import NewWindowLocators
from selenium.webdriver.common.by import By

class NewWindow(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/windows'
        super().__init__(driver, url)

    def open_new_window(self):
        self.find(NewWindowLocators.LINK).click()

    def switch_to_new_window(self):
        self._driver.switch_to.window(self._driver.window_handles[1])

    def get_text_body(self):
        return self.find((By.CLASS_NAME, "example")).text