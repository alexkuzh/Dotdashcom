from pages.javaScriptError import JavaScriptError


def test_js_error(driver):
    page = JavaScriptError(driver)
    msg = page.js_error()
    assert 'xyz' in msg
    print(msg)
