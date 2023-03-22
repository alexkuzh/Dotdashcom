from pages.base import CommonOps
from utils.locators import JavaScriptAlertLocators


class JavaScriptAlert(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/javascript_alerts'
        super().__init__(driver, url)

    def get_message(self):
        return self.find(JavaScriptAlertLocators.RESULT).text

    def js_alert(self):
        self.find(JavaScriptAlertLocators.BUTTON_ALERT).click()
        self.alert().accept()
        return self.get_message()

    def js_confirm_yes(self):
        self.find(JavaScriptAlertLocators.BUTTON_CONFIRM).click()
        self.alert().accept()
        return self.get_message()

    def js_confirm_cancel(self):
        self.find(JavaScriptAlertLocators.BUTTON_CONFIRM).click()
        self.alert().dismiss()
        return self.get_message()

    def js_prompt(self, txt):
        self.find(JavaScriptAlertLocators.BUTTON_PROMPT).click()
        prompt = self.alert()
        prompt.send_keys(txt)
        prompt.accept()
        return self.get_message()

    def js_prompt_cancel(self, txt):
        self.find(JavaScriptAlertLocators.BUTTON_PROMPT).click()
        prompt = self.alert()
        prompt.send_keys(txt)
        prompt.dismiss()
        return self.get_message()
