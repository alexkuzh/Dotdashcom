from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base import CommonOps
from utils.locators import DynamicControlLocators


class DynamicControls(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/dynamic_controls'
        super().__init__(driver, url)

    def checkbox_presents(self):
        try:
            self.wait_for(DynamicControlLocators.CHECKBOX)
            return True
        except TimeoutException:
            return False

    def checking_input_text_element(self):
        return self.wait_for(DynamicControlLocators.INPUT_TEXT).is_enabled()

    def click_control_button(self, element):
        if element == "checkbox" or element == "input":
            control_xpath = f"//form[@id='{element}-example']/button"
        else:
            return "Element not Found"
        
        self.find((By.XPATH, control_xpath)).click()
        msg = self.wait_for(DynamicControlLocators.STATE_CHANGE).text
        return msg

    def check_initial_state(self):
        return True if self.checkbox_presents() and self.checking_input_text_element() == False else False

    def press_checkbox_button(self):
        return self.click_control_button("checkbox")

    def press_input_button(self):
        return self.click_control_button("input")


