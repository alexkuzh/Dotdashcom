from pages.base import CommonOps
from utils.locators import DropDownLocators


class DropDown(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/dropdown'
        super().__init__(driver, url)

    def click_menu(self):
        dd_list = self.wait_for(DropDownLocators.DD_MENU)
        dd_list.click()

    def select_opt1(self):
        dd_opt1 = self.wait_for(DropDownLocators.OPTION1)
        dd_opt1.click()

    def check_op1_press(self):
        return self.get_attribute(DropDownLocators.OPTION1, "selected")

    def select_opt2(self):
        dd_opt2 = self.wait_for(DropDownLocators.OPTION2)
        dd_opt2.click()

    def check_op2_press(self):
        return self.get_attribute(DropDownLocators.OPTION2, "selected")

