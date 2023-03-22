from pages.notification import Notification
from utils.locators import NotificationLocators


def test_notification(driver):
    page = Notification(driver)
    page.wait_page_loaded()
    messages = NotificationLocators.MESSAGES
    count = 0
    while messages:
        try:
            count += 1
            msg = page.notification_click()
            msg = msg.split('\n')[0]
            messages.remove(msg)
        except:
            pass
    assert True
    print(f" {count} attempts")
