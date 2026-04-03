import pytest
from Constants import constants
from Pages.LoginPage import LoginPage
from Utilities.excel_reader import get_login_data


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize("scenario,username,password,expected,expected_message", get_login_data())
def test_login_from_excel(driver,scenario,username,password,expected,expected_message):
    """ Verify login behavior for multiple credential scenarios using Excel test data. """
    loginPage = LoginPage(driver)

    username = username or ""
    password = password or ""
    expected_message = expected_message or ""

    homePage = loginPage.do_login(username, password)

    if expected == "PASS":
        # After successful login, title should be home page title
        assert  homePage.get_title(constants.HOME_PAGE_TITLE) == constants.HOME_PAGE_TITLE
    else:
        # Blank fields -> field validation ("Required")
        if username == "" or password == "":
            if username == "":
                assert loginPage.get_username_required_text() == expected_message
            if password == "":
                assert loginPage.get_password_required_text() == expected_message
        else:
            assert loginPage.get_error_message() == expected_message

