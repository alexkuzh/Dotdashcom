from pages.base import CommonOps
from utils.locators import DragAndDropLocators


class DnD(CommonOps):

    def __init__(self, driver, url=''):
        if not url:
            url = 'http://localhost:7080/drag_and_drop'
        super().__init__(driver, url)

    def drag_n_drop_left2right(self):
        self.drag_n_drop(DragAndDropLocators.COLUMNS_1, DragAndDropLocators.COLUMNS_2)

    def drag_n_drop_right2right(self):
        self.drag_n_drop(DragAndDropLocators.COLUMNS_2, DragAndDropLocators.COLUMNS_1)




