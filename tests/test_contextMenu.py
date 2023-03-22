from pages.contextMenu import ContextMenu


def test_context_menu(driver):
    page = ContextMenu(driver)
    page.wait_page_loaded()
    page.right_click_context_menu()
    alert = page.alert()
    text = alert.text
    alert.accept()
    assert text == 'You selected a context menu'