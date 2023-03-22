from pages.fileUpload import FileUpload
from utils.locators import FileUploadLocators


def test_upload_file(driver):
    page = FileUpload(driver)
    page.wait_page_loaded()
    txt = page.upload_file_button()
    assert FileUploadLocators.FILE.split('\\')[-1] == txt


def test_drag_n_drop_file(driver):
    page = FileUpload(driver)
    page.wait_page_loaded()
    txt = page.upload_drag_n_drop_file()
    assert FileUploadLocators.FILE.split('\\')[-1] == txt
