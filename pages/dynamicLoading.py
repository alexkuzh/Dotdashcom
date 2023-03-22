from pages.base import CommonOps
from utils.locators import DynamicLoadingLocators


class DynamicLoading(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/dynamic_loading/2'
        super().__init__(driver, url)

    def press_dynamic_loading(self):
        self.wait_for(DynamicLoadingLocators.BUTTON).click()

    def check_dynamic_loading(self):
        element = self.wait_for(DynamicLoadingLocators.TEXT)
        return element.text
