from pages.base import CommonOps
from utils.locators import ContexMenuLocators


class ContextMenu(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/context_menu'
        super().__init__(driver, url)

    def right_click_context_menu(self):
        context_menu = self.find(ContexMenuLocators.CONTEXT_BOX)
        self.context_click(context_menu).perform()

    def check_alert_message(self):
        return self.alert().text

    def accept_alert(self):
        return self.alert().accept()
