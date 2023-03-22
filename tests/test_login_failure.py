from pages.login import Login



def test_form_fail_user_auth(driver):
    form = Login(driver)
    form.enter_login_username("random_user")
    form.enter_login_password("SuperSecretPassword!")
    form.click_login_button()
    assert "username is invalid" in form.check_login_logout_status().text


def test_form_fail_pass_auth(driver):
    form = Login(driver)
    form.enter_login_username("tomsmith")
    form.enter_login_password("BadPassword")
    form.click_login_button()
    assert "password is invalid" in form.check_login_logout_status().text
