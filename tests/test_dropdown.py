from pages.dropDown import DropDown


def test_dropdown_list(driver):
    menu = DropDown(driver)
    menu.click_menu()
    menu.select_opt1()
    assert menu.check_op1_press() == 'true'
    menu.select_opt2()
    assert menu.check_op2_press() == 'true'
