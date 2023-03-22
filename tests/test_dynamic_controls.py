from pages.dynamicControl import DynamicControls


def test_dynamic_controls_initial(driver):
    page = DynamicControls(driver)
    page.wait_page_loaded()
    assert page.check_initial_state()


def test_dynamic_controls_remove_button(driver):
    page = DynamicControls(driver)
    page.wait_page_loaded()
    msg = ''
    if page.check_initial_state():
        msg = page.press_checkbox_button()
    assert msg == "It's gone!"


def test_dynamic_controls_add_button(driver):
    page = DynamicControls(driver)
    page.wait_page_loaded()
    msg = ''
    if page.check_initial_state():
        page.press_checkbox_button()
        msg = page.press_checkbox_button()
        assert msg == "It's back!"
    else:
        assert False


def test_dynamic_controls_enable_button(driver):
    page = DynamicControls(driver)
    page.wait_page_loaded()
    msg = ''
    enabled = True
    if page.check_initial_state():
        msg = page.press_input_button()
        enabled = page.checking_input_text_element()
    assert msg == "It's enabled!" and enabled


def test_dynamic_controls_disable_button(driver):
    page = DynamicControls(driver)
    page.wait_page_loaded()
    msg = ''
    enabled = True
    if page.check_initial_state():
        page.press_input_button()
        msg = page.press_input_button()
        enabled = page.checking_input_text_element()
    assert msg == "It's disabled!" and not enabled
