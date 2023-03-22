from pages.base import CommonOps
from utils.locators import CheckBoxesLocators


class CheckBoxes(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/checkboxes'
        super().__init__(driver, url)

    def list_checkboxes(self):
        return self.wait_for_all(CheckBoxesLocators.FORM_CHECKBOXES)

