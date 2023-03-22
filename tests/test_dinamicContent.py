from pages.dynamicContent import DynamicContent


def test_dynamic_content_img(driver):
    page = DynamicContent(driver)
    page.wait_page_loaded()
    s = set()
    for _ in range(3):
        s.add(page.get_img() + page.get_txt())
        page.refresh_page()
    assert len(s) == 3

