import pytest

from Pages.LoginAPIPage import APILoginPage
from TestData.api_test_data import get_api_user_payload
from Utilities.api_client import APIClient

@pytest.mark.integration
class Test_API_UI_Login:

    def setup_method(self):
        self.api_client = APIClient()

    def test_ui_login(self,driver):

        login_Page = APILoginPage(driver)
        login_Page.open_browser()
        login_Page.login("seletest511@gmail.com","test123@")
        assert login_Page.get_logged_in_text()