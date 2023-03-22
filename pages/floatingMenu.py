from pages.base import CommonOps
from utils.locators import FloatingMenuLocators


class FloatingMenu(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/floating_menu'
        super().__init__(driver, url)

    def scrolldown(self):
        try:
            self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        except Exception as e:
            pass
        return self.is_visible(FloatingMenuLocators.MENU)