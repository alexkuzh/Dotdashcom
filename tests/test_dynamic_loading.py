from pages.dynamicLoading import DynamicLoading


def test_dynamic_controls_initial(driver):
    page = DynamicLoading(driver)
    page.wait_page_loaded()
    page.press_dynamic_loading()
    txt = page.check_dynamic_loading()
    assert txt == "Hello World!"
