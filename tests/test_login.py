from pages.login_page import LoginPage

def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        username="locked_user",
        password="wrong_password"
    )

    error_message = driver.find_element(
        "xpath",
        "//h3[@data-test='error']"
    )

    assert error_message.is_displayed()
