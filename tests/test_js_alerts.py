from pages.javaScriptAlerts import JavaScriptAlert
from utils.locators import JavaScriptAlertLocators


def test_js_alert(driver):
    page = JavaScriptAlert(driver)
    page.wait_page_loaded()
    txt = page.js_alert()
    assert txt == JavaScriptAlertLocators.TXT_ALERT


def test_js_confirm(driver):
    page = JavaScriptAlert(driver)
    page.wait_page_loaded()
    txt = page.js_confirm_yes()
    assert txt == JavaScriptAlertLocators.TXT_CONFIRM_YES
    txt = page.js_confirm_cancel()
    assert txt == JavaScriptAlertLocators.TXT_CONFIRM_CANCEL


def test_js_prompt(driver):
    page = JavaScriptAlert(driver)
    page.wait_page_loaded()
    prompt = "asdsadsad"
    txt = page.js_prompt(prompt)
    assert txt == JavaScriptAlertLocators.TXT_PROMPT+prompt
    txt = page.js_prompt_cancel(prompt)
    assert txt == JavaScriptAlertLocators.TXT_PROMPT+"null"