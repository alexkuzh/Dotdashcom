from pages.mouseHover import MouseHover


def test_mouse_hover_1(driver):
    page = MouseHover(driver)
    page.wait_page_loaded()
    page.mouse_hover1()
    assert page.get_fig_captions()[0].is_displayed()


def test_mouse_hover_2(driver):
    page = MouseHover(driver)
    page.wait_page_loaded()
    page.mouse_hover2()
    assert page.get_fig_captions()[1].is_displayed()


def test_mouse_hover_3(driver):
    page = MouseHover(driver)
    page.wait_page_loaded()
    page.mouse_hover3()
    assert page.get_fig_captions()[2].is_displayed()
