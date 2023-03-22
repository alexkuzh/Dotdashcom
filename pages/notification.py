from pages.base import CommonOps
from utils.locators import NotificationLocators


class Notification(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/notification_message_rendered'
        super().__init__(driver, url)

    def notification_click(self):
        self.find(NotificationLocators.LINK).click()
        return self.wait_for(NotificationLocators.FLASH).text.strip()
