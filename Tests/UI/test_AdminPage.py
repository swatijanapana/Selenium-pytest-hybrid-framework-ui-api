import pytest

from Constants import constants as constants
from TestData.ui_test_data import ADMIN_TESTDATA
from Tests.UI.base_test import BaseTest


@pytest.mark.ui
@pytest.mark.regression
class Test_Admin(BaseTest):

    """ Admin Page test cases. """

    def login_and_open_admin(self):
        """ Log in and navigate to Admin page. """
        self.homePage = self.login_and_get_home()
        return self.homePage.click_admin_menu()

    def test_user_management_tab_selected(self):
        """ Verify User Management tab is selected on Admin page. """
        self.adminPage = self.login_and_open_admin()
        assert self.adminPage.is_user_management_tab_selected()

    def test_search_with_valid_username(self):
        """ Verify search returns result for a valid username. """
        self.adminPage = self.login_and_open_admin()
        test_value = ADMIN_TESTDATA["valid_username"]
        self.adminPage.enter_username(test_value)
        self.adminPage.click_search_button()
        assert self.adminPage.is_username_present_results(test_value)

    def test_enter_username_in_search_field(self):
        """ Verify username can be entered in Admin search field. """
        self.adminPage = self.login_and_open_admin()
        test_value = ADMIN_TESTDATA["input_username"]
        self.adminPage.enter_username(test_value)
        assert self.adminPage.get_username_value() == test_value

    def test_search_with_invalid_username(self):
        """ Verify no records message is displayed for an invalid username search. """
        self.adminPage = self.login_and_open_admin()
        invalid_username_value = ADMIN_TESTDATA["invalid_username"]
        self.adminPage.enter_username(invalid_username_value)
        self.adminPage.click_search_button()
        self.adminPage.wait_for_visibility(self.adminPage.No_Record_found_message,timeout= 50)
        self.driver.save_screenshot("Reports/Screenshots/invalid_search.png")
        assert self.adminPage.is_no_record_found_message_displayed()

    def test_click_reset_button(self):
        """ Verify Reset button clears Admin search filters. """
        self.adminPage = self.login_and_open_admin()
        self.adminPage.click_reset_button()
        assert self.adminPage.get_username_value() == constants.USER_NAME_VALUE
        assert self.adminPage.get_userrole_selected_text() == constants.DEFAULT_DROPDOWN_TEXT
        assert self.adminPage.get_status_selected_text() == constants.DEFAULT_DROPDOWN_TEXT


    def test_select_from_user_role_dropdown(self):
        """ Verify user role can be selected from User Role dropdown. """
        self.adminPage = self.login_and_open_admin()
        option_text = ADMIN_TESTDATA["user_role_option_2"]
        self.adminPage.select_from_dropdown(self.adminPage.User_role_dropdown,option_text)
        assert self.adminPage.get_userrole_selected_text() == option_text

    def test_select_from_status_dropdown(self):
        """ Verify status can be selected from Status dropdown. """
        self.adminPage = self.login_and_open_admin()
        option_text = ADMIN_TESTDATA["status_option_1"]
        self.adminPage.select_from_dropdown(self.adminPage.Status_dropdown, option_text)
        assert self.adminPage.get_status_selected_text() == option_text

    def test_reset_clears_filters_after_search(self):
        """ Verify Reset button clears applied filters after performing search. """
        self.adminPage = self.login_and_open_admin()
        self.adminPage.click_reset_button()
        test_value = ADMIN_TESTDATA["valid_username"]
        self.adminPage.enter_username(test_value)
        user_role = ADMIN_TESTDATA["user_role_option_2"]
        self.adminPage.select_from_dropdown(self.adminPage.User_role_dropdown, user_role)
        status = ADMIN_TESTDATA["status_option_1"]
        self.adminPage.select_from_dropdown(self.adminPage.Status_dropdown, status)
        self.adminPage.click_search_button()
        row_count_after_search = self.adminPage.get_row_result_count()
        assert row_count_after_search > 0
        self.adminPage.wait_for_visibility(self.adminPage.Result_table)
        self.adminPage.click_reset_button()
        assert self.adminPage.get_username_value() == constants.USER_NAME_VALUE
        assert self.adminPage.get_userrole_selected_text() == constants.DEFAULT_DROPDOWN_TEXT
        assert self.adminPage.get_status_selected_text() == constants.DEFAULT_DROPDOWN_TEXT

    def test_search_without_criteria(self):
        """ Verify search behavior when no filters are applied. """
        self.adminPage = self.login_and_open_admin()
        self.adminPage.click_search_button()
        self.adminPage.wait_for_form_loader()
        # check at least one known username exists
        assert self.adminPage.is_username_present_results("Admin")





