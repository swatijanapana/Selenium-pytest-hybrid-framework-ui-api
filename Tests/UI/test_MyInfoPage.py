import os.path
import pytest

from Tests.UI.base_test import BaseTest
from Constants import constants as constants
from TestData.ui_test_data import MYINFO_TESTDATA, MYINFO_COMMENT_TESTDATA, MYINFO_CUSTOM_FIELD_TESTDATA
from Utilities.file_utils import create_unique_file_copy


@pytest.mark.ui
@pytest.mark.regression
class Test_MyInfo(BaseTest):

   """ MyInfo Page test cases. """

   def login_and_open_myinfo(self):
        """ Log in and navigate to MyInfo page.  """
        self.homePage = self.login_and_get_home()
        return self.homePage.click_myinfo_menu()

   def open_myinfo_personal_details(self):
        """ Log in, open MyInfo page, and navigate to Personal Details section. """
        myinfoPage = self.login_and_open_myinfo()
        myinfoPage.click_personal_details_submenu()
        return myinfoPage

   def test_click_personal_details_submenu(self):
        """ Verify user can open Personal Details page from MyInfo menu. """
        self.myinfoPage = self.login_and_open_myinfo()
        header_value = self.myinfoPage.click_personal_details_submenu()
        assert self.myinfoPage.is_personal_details_page_loaded()
        assert header_value == constants.PERSONAL_DETAILS_TITLE


   def test_personal_details_form(self):
        """ Verify Personal Details form can be updated successfully. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.fill_personal_details_form(MYINFO_TESTDATA)
        self.myinfoPage.click_save_button()
        actual = self.myinfoPage.get_personal_details_values()
        assert actual["first_name"] == MYINFO_TESTDATA["first_name"]
        assert actual["last_name"] == MYINFO_TESTDATA["last_name"]
        assert actual["employee_id"] == MYINFO_TESTDATA["employee_id"]
        assert actual["driver_license_number"] == MYINFO_TESTDATA["driver_license_number"]
        assert actual["dl_expiry_date"] == MYINFO_TESTDATA["dl_expiry_date"]
        assert actual["nationality"] == MYINFO_TESTDATA["nationality"]
        assert actual["marital_status"] == MYINFO_TESTDATA["marital_status"]
        assert actual["dob"] == MYINFO_TESTDATA["dob"]
        if MYINFO_TESTDATA["gender"].lower() == "male":
            assert self.myinfoPage.is_gender_male_selected()
        elif MYINFO_TESTDATA["gender"].lower() == "female":
            assert self.myinfoPage.is_gender_female_selected()

   def test_personal_details_persist_after_refresh(self):
        """ Verify Personal Details values persist after page refresh. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.fill_personal_details_form(MYINFO_TESTDATA)
        self.myinfoPage.click_save_button()
        self.myinfoPage.refresh_page()
        self.myinfoPage.wait_for_form_loader()
        assert  self.myinfoPage.is_personal_details_page_loaded()
        self.myinfoPage.click_personal_details_submenu()
        actual = self.myinfoPage.get_personal_details_values()
        assert actual["first_name"] == MYINFO_TESTDATA["first_name"]
        assert actual["employee_id"] == MYINFO_TESTDATA["employee_id"]
        assert actual["dl_expiry_date"] == MYINFO_TESTDATA["dl_expiry_date"]
        assert actual["nationality"] == MYINFO_TESTDATA["nationality"]
        assert actual["dob"] == MYINFO_TESTDATA["dob"]
        if MYINFO_TESTDATA["gender"].lower() == "male":
            assert self.myinfoPage.is_gender_male_selected()
        elif MYINFO_TESTDATA["gender"].lower() == "female":
            assert self.myinfoPage.is_gender_female_selected()

   def test_custom_field_form(self):
        """ Verify Custom Fields form can be updated successfully. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_custom_field_section()
        blood_type_value = MYINFO_CUSTOM_FIELD_TESTDATA["blood_type"]
        self.myinfoPage.select_blood_type(blood_type_value)
        test_field_value = MYINFO_CUSTOM_FIELD_TESTDATA["test_field"]
        self.myinfoPage.enter_test_field(test_field_value)
        self.myinfoPage.click_CF_save_button()
        assert self.myinfoPage.is_custom_field_title_exist()
        assert self.myinfoPage.get_blood_type() == MYINFO_CUSTOM_FIELD_TESTDATA["blood_type"]
        assert self.myinfoPage.get_test_field_value() == MYINFO_CUSTOM_FIELD_TESTDATA["test_field"]


   def test_click_add_button(self):
        """ Verify Add Attachment popup fields are displayed correctly. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_add_attachment_section()
        assert self.myinfoPage.is_attachment_title_exist()
        self.myinfoPage.click_add_button()
        assert self.myinfoPage.is_add_attachment_title_exist()
        assert self.myinfoPage.verify_browse_option_enabled()
        assert self.myinfoPage.is_no_file_selected_message_displayed()
        assert self.myinfoPage.is_accepts_up_to_1MB_message_displayed()
        assert self.myinfoPage.is_comment_label_exist()


   def test_type_comment_here_field_exist(self):
        """ Verify comment can be entered in Add Attachment popup. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_add_attachment_section()
        self.myinfoPage.click_add_button()
        comment_text_value = MYINFO_COMMENT_TESTDATA["comment_text"]
        self.myinfoPage.enter_type_comment_here(comment_text_value)
        assert self.myinfoPage.get_type_comment_text() == comment_text_value


   def test_attachment_upload_valid_file_type(self):
        """ Verify a valid attachment file can be uploaded successfully. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_add_attachment_section()
        self.myinfoPage.click_add_button()
        original_file = os.path.abspath("TestFiles/sample_upload.txt")
        unique_file = create_unique_file_copy(original_file)
        file_name = os.path.basename(unique_file)
        self.myinfoPage.upload_file(unique_file)
        assert self.myinfoPage.is_file_present_in_results_with_wait(file_name)


   def test_invalid_attachment_file_type(self):
        """ Verify an invalid attachment file type is rejected and not added to the results table. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_add_attachment_section()
        self.myinfoPage.click_add_button()
        file_path = os.path.abspath("TestFiles/sample_upload.html")
        file_name = os.path.basename(file_path)
        self.myinfoPage.upload_file(file_path)
        assert self.myinfoPage.is_file_type_not_allowed_message_visible()
        assert not self.myinfoPage.is_file_present_in_results(file_name)


   def test_delete_upload_attachment(self):
        """ Verify an uploaded attachment can be deleted successfully. """
        self.myinfoPage = self.open_myinfo_personal_details()
        self.myinfoPage.scroll_to_add_attachment_section()
        self.myinfoPage.click_add_button()
        original_file = os.path.abspath("TestFiles/sample_upload.txt")
        unique_file = create_unique_file_copy(original_file)
        file_name = os.path.basename(unique_file)
        self.myinfoPage.upload_file(unique_file)
        assert self.myinfoPage.is_file_present_in_results_with_wait(file_name)
        self.myinfoPage.confirm_delete_attachment(file_name)
        assert not self.myinfoPage.is_file_present_in_results(file_name)
