from pages.newWindow import NewWindow
from utils.locators import NewWindowLocators

def test_new_window(driver):
    page = NewWindow(driver)
    page.wait_page_loaded()
    page.open_new_window()
    page.switch_to_new_window()
    assert page.get_text_body() == NewWindowLocators.TEST_TEXT