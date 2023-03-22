from pages.floatingMenu import FloatingMenu


def test_scroll_page(driver):
    page = FloatingMenu(driver)
    page.wait_page_loaded()
    float_menu = page.scrolldown()
    assert float_menu.is_displayed()
