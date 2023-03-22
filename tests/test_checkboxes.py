from pages.checkboxes import CheckBoxes


def test_checkboxes_count(driver):
    form = CheckBoxes(driver)
    assert len(form.list_checkboxes()) == 2


def test_checkbox_initial_state(driver):
    form = CheckBoxes(driver)
    form.wait_page_loaded()
    checkboxes_list = form.list_checkboxes()
    assert checkboxes_list[0].get_attribute('checked') is None and \
           checkboxes_list[1].get_attribute('checked') == 'true'


def test_checkbox_changed_state(driver):
    form = CheckBoxes(driver)
    form.wait_page_loaded()
    checkboxes_list = form.list_checkboxes()
    for box in checkboxes_list:
        box.click()
    assert checkboxes_list[1].get_attribute('checked') is None and \
           checkboxes_list[0].get_attribute('checked') == 'true'

