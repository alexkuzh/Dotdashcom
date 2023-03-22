from pages.base import CommonOps
from utils.locators import DynamicContentLocators


class DynamicContent(CommonOps):

    img = ''
    txt = ''

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/dynamic_content?with_content=static'
        super().__init__(driver, url)

    def get_img(self):
        return self.get_attribute(DynamicContentLocators.IMG,"src")

    def get_txt(self):
        return self.find(DynamicContentLocators.TXT).text
