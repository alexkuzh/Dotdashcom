from pages.iframe import Iframe


def test_iframe(driver):
    txt = "aaaaa"
    page = Iframe(driver)
    page.wait_page_loaded()
    page.switch_iframe()
    page.write_text(txt)
    out_txt = page.get_body_text()
    page.switch_iframe_def()
    assert txt == out_txt
