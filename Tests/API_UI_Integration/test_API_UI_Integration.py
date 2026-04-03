import time
import pytest

from Pages.LoginAPIPage import APILoginPage
from TestData.api_test_data import get_api_user_payload
from Utilities.api_client import APIClient
from Utilities.config_reader import get_config

@pytest.mark.integration
class Test_API_UI_Intergration:

    def setup_method(self):
        self.api_client = APIClient()

    def test_create_account_and_login(self,driver):

        config = get_config()
        base_url = config["API_BASE_URL"]
        create_endpoint = config["API_ENDPOINTS"]["CREATE_ACCOUNT"]
        delete_endpoint = config["API_ENDPOINTS"]["DELETE_ACCOUNT"]

        create_url = base_url + create_endpoint
        delete_url = base_url + delete_endpoint


        browser_name = driver.capabilities.get("browserName")
        email = f"apiui_{browser_name}_{int(time.time())}@gmail.com"
        password = f"pwd_{int(time.time())}"
        payload = get_api_user_payload(email,password)

        # API: create account
        response = self.api_client.post(create_url, payload,is_json=False)
        print(response.text)
        print(response.json())
        assert response.status_code == 200 or response.status_code == 201
        response_json = response.json()
        assert response_json["responseCode"] == 201
        assert response_json["message"] == "User created!"

        # UI: login with same credentials
        login_Page = APILoginPage(driver)
        login_Page.open_browser()
        login_Page.login(email,password)
        assert login_Page.get_logged_in_text()









