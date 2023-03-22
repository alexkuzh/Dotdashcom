from pages.base import CommonOps
from utils.locators import MouseHoverLocators


class MouseHover(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/hovers'
        super().__init__(driver, url)

    def mouse_hover1(self):
        self.move_mouse(MouseHoverLocators.FIGURE1)

    def mouse_hover2(self):
        self.move_mouse(MouseHoverLocators.FIGURE2)

    def mouse_hover3(self):
        self.move_mouse(MouseHoverLocators.FIGURE3)

    def get_fig_captions(self):
        return self.wait_for_all(MouseHoverLocators.FIG_CAPTIONS)
