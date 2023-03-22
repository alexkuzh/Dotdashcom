from pages.login import Login


def test_form_authentication(driver):
    form = Login(driver)
    form.enter_login_username("tomsmith")
    form.enter_login_password("SuperSecretPassword!")
    form.click_login_button()
    assert "logged in" in form.check_login_logout_status().text
    form.click_logout_button()
    assert "logged out" in form.check_login_logout_status().text


