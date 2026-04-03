import time
import pytest
from TestData.api_test_data import get_api_user_payload, del_api_user_payload
from Utilities.api_client import APIClient
from Utilities.config_reader import get_config


@pytest.mark.api
class Test_API_Account:

    def setup_method(self):
        self.api_client = APIClient()

    def test_create_account(self):

        config = get_config()
        base_url = config["API_BASE_URL"]
        endpoint = config["API_ENDPOINTS"]["CREATE_ACCOUNT"]
        url = base_url + endpoint

        email = f"apiui_{int(time.time())}@gmail.com"
        password = f"pwd_{int(time.time())}"
        payload = get_api_user_payload(email, password)

        response = self.api_client.post(url, payload,is_json= False)
        print(response.text)
        print(response.json())
        assert response.status_code == 200 or response.status_code == 201

        response_json = response.json()
        assert response_json["responseCode"] == 201
        assert response_json["message"] == "User created!"

    def test_delete_account_after_creation(self):

        config = get_config()

        create_url = config["API_BASE_URL"] + config["API_ENDPOINTS"]["CREATE_ACCOUNT"]
        delete_url = config["API_BASE_URL"] + config["API_ENDPOINTS"]["DELETE_ACCOUNT"]

        email = f"apiui_{int(time.time_ns())}@gmail.com"
        password = f"pwd_{int(time.time_ns())}"

        create_payload = get_api_user_payload(email, password)
        delete_payload = del_api_user_payload(email, password)

        create_response = self.api_client.post(create_url, create_payload, is_json=False)
        assert create_response.status_code in [200, 201]

        response_json = create_response.json()
        assert response_json["responseCode"] == 201
        assert response_json["message"] == "User created!"

        delete_response = self.api_client.delete(delete_url, delete_payload,is_json=False)
        assert delete_response.status_code == 200

        response_json = delete_response.json()
        assert response_json["responseCode"] == 200
        assert response_json["message"] == "Account deleted!"




