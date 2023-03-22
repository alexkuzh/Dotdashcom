from pages.drag_n_drop import DnD
from utils.locators import DragAndDropLocators


def test_drag_and_drop_lr(driver):
    form = DnD(driver)
    source_before = form.find(DragAndDropLocators.COLUMNS_1).text
    form.drag_n_drop_left2right()
    source_after = form.find(DragAndDropLocators.COLUMNS_1).text
    assert source_before != source_after


def test_drag_and_drop_rl(driver):
    form = DnD(driver)
    source_before = form.find(DragAndDropLocators.COLUMNS_2).text
    form.drag_n_drop_left2right()
    source_after = form.find(DragAndDropLocators.COLUMNS_2).text
    assert source_before != source_after
