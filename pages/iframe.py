from pages.base import CommonOps
from utils.locators import IframeLocators


class Iframe(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/iframe'
        super().__init__(driver, url)

    def switch_iframe(self):
        self.switch_to_frame(IframeLocators.IFRAME)

    def write_text(self,txt):
        self.find(IframeLocators.TEXT_BODY).clear()
        self.find(IframeLocators.TEXT_BODY).send_keys(txt)

    def switch_iframe_def(self):
        self.switch_to_frame_default()

    def get_body_text(self):
        return self.find(IframeLocators.TEXT_BODY).text