from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class MyInfoPage(BasePage):

    """ By Locators -- OR"""

    # Personal Details Section

    Personal_details_submenu = (By.XPATH, "//a[text()='Personal Details']")
    Personal_details_title = (By.XPATH,"//h6[text()='Personal Details' and contains(@class,'orangehrm-main-title')]")
    Firstname_input = (By.XPATH, "//input[@name ='firstName']")
    Lastname_input = (By.XPATH, "//input[@name ='lastName']")
    Employee_id_input = (By.XPATH, "//label[text()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    PD_Save_button = (By.XPATH,"//h6[normalize-space()='Personal Details']/following::button[@type='submit'][1]")
    DL_number_input = (By.XPATH, "//label[contains(., \"Driver\")]/following::input[1]")
    Form_loader = (By.CLASS_NAME, "oxd-form-loader")
    DL_expiration_date = (By.XPATH, "//label[text()='License Expiry Date']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    Nationality_dropdown = (By.XPATH, "//label[text()='Nationality']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-wrapper')]")
    Marital_status_dropdown = (By.XPATH, "//label[text()='Marital Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-wrapper')]")
    DOB = (By.XPATH, "//label[text()= 'Date of Birth']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    Calendar_popup = (By.CSS_SELECTOR, ".oxd-calendar-wrapper")
    Calender_close_button = (By.CSS_SELECTOR,".oxd-date-input-link.--close")
    Gender_radio_input_male = (By.XPATH, "//input[@type='radio' and @value='1']")
    Gender_radio_input_female = (By.XPATH, "//input[@type='radio' and @value='2']")

    # Custom Fields Section

    Custom_fields_title = (By.XPATH, "//h6[text()='Custom Fields']")
    Blood_type_dropdown = (By.XPATH, "//label[text()='Blood Type']/following::div[@class='oxd-select-wrapper']")
    Test_field_input = (By.XPATH, "//label[text()='Test_Field']/following::input")
    CF_save_button = (By.XPATH, "//h6[normalize-space()='Custom Fields']/following::button[@type='submit'][1]")


    # Add Attachment Section

    Attachments_title = (By.XPATH,"//h6[text()='Attachments']")
    Add_attachment_title = (By.XPATH, "//h6[text()='Add Attachment']")
    Add_button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--text' and @type = 'button']")
    Browse_option = (By.XPATH, "//div[@class='oxd-file-button' and text()='Browse']")
    Browse_attach_file =(By.XPATH,"//input[@type='file']")
    No_file_selected_message = (By.XPATH, "//div[@class='oxd-file-input-div' and text()='No file selected']")
    Accepts_up_to_1MB_message = (By.XPATH, "//p[text()='Accepts up to 1MB']")
    Comment_label = (By.XPATH,"//label[@class='oxd-label' and text()='Comment']")
    Type_comment_here_textarea = (By.XPATH, "//textarea[@placeholder='Type comment here']")
    File_type_not_allowed_message = (By.XPATH, "//span[text()='File type not allowed']")
    Attachment_result_table = (By.XPATH, "//div[contains(@class,'oxd-table-body')]")
    Attachment_Save_button = (By.XPATH, "//h6[text()='Add Attachment']/following::button[@type='submit'][1]")
    Delete_selected = (By.XPATH, "//button[normalize-space()='Delete Selected']")
    Confirm_button_popup = (By.XPATH, "//button[normalize-space()='Yes, Delete']")




    """ Constructor of page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions for MyInfo Page """

    #  Personal Details Section

    """ Click the Personal Details submenu."""
    def click_personal_details_submenu(self):
        self.do_click(self.Personal_details_submenu)
        self.wait_for_form_loader()
        return self.get_element_text(self.Personal_details_title)

    """ Verify Personal Details page loaded properly or not."""
    def is_personal_details_page_loaded(self):
         return self.is_visible(self.Personal_details_title)

    """ Wait until the page loader disappears. """
    def wait_for_form_loader(self):
        self.wait_for_loader_to_disappear(self.Form_loader)


    """Enter first name in the input field."""
    def enter_firstname(self, firstname):
        self.do_clear(self.Firstname_input)
        self.do_send_keys(self.Firstname_input, firstname)

    """Enter last name in the input field."""
    def enter_lastname(self, lastname):
        self.do_clear(self.Lastname_input)
        self.do_send_keys(self.Lastname_input, lastname)

    """Enter employee id."""
    def enter_employee_id(self, employee_id):
        self.do_clear(self.Employee_id_input)
        self.do_send_keys(self.Employee_id_input, employee_id)

    """Enter driver license number."""
    def enter_driver_license_number(self, dl_number):
        element = self.driver.find_element(*self.DL_number_input)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.do_clear(self.DL_number_input)
        self.do_send_keys(self.DL_number_input,dl_number )

    """Select a date from calendar field."""
    def select_calender_date(self,calender_locator,date_value):
        self.do_clear(calender_locator)
        element = self.driver.find_element(*calender_locator)
        element.send_keys(date_value)
        element.send_keys(Keys.TAB)
        try:
           self.wait_for_calendar_to_close()
        except TimeoutException:
           element.send_keys(Keys.ESCAPE)
           self.wait_for_calendar_to_close()

    """ Select a date from DL Expiry date field. """
    def select_dl_exp_date(self,dl_exp_date_value):
        self.select_calender_date(self.DL_expiration_date,dl_exp_date_value)

    """ Select a date from Date of Birth (DOB) field."""

    def select_dob(self, dob_value):
        self.select_calender_date(self.DOB, dob_value)


    """ Wait until the calender loader disappears. """
    def wait_for_calendar_to_close(self):
        self.wait_for_loader_to_disappear(self.Calendar_popup)

    """ Select a value from dropdown. """
    def select_from_dropdown(self,dropdown_locator,option_text):
        try:
            self.wait_for_calendar_to_close()
        except TimeoutException:
            self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
            self.wait_for_calendar_to_close()
        self.do_click(dropdown_locator)
        option = (By.XPATH, f"//span[text()='{option_text}']")
        self.do_click(option)
        self.wait_for_form_loader()

    """ Select value from Nationality Dropdown """
    def select_nationality(self,nationality):
        self.select_from_dropdown(self.Nationality_dropdown,nationality)

    """ Select value from Marital Status Dropdown. """
    def select_marital_status(self,marital_status):
        self.select_from_dropdown(self.Marital_status_dropdown,marital_status)

    """ Click the Personal Details save button. """
    def click_save_button(self):
        self.wait_for_loader_to_disappear(self.Form_loader)
        self.do_click(self.PD_Save_button)
        self.wait_for_loader_to_disappear(self.Form_loader)

    """ Return the first name value."""
    def get_firstname_value(self):
        element = self.driver.find_element(*self.Firstname_input)
        return element.get_attribute("value")

    """ Return the last name value."""
    def get_lastname_value(self):
        element = self.driver.find_element(*self.Lastname_input)
        return element.get_attribute("value")

    """ Return the employee id value."""
    def get_employee_id_value(self):
        element = self.driver.find_element(*self.Employee_id_input)
        return element.get_attribute("value")

    """ Return the driver license value."""
    def get_driver_license_value(self):
        element = self.driver.find_element(*self.DL_number_input)
        return element.get_attribute("value")

    """ Return the driver license expiry date."""
    def get_dl_exp_date(self):
        element = self.driver.find_element(*self.DL_expiration_date)
        return element.get_attribute("value")

    """ Return the selected nationality."""
    def get_nationality(self):
        return self.get_element_text(self.Nationality_dropdown)

    """ Return the selected marital status."""
    def get_marital_status(self):
        return self.get_element_text(self.Marital_status_dropdown)

    """Return the DOB date."""
    def get_dob_value(self):
        element = self.driver.find_element(*self.DOB)
        return element.get_attribute("value")


    """ Fill Personal Details form """
    def fill_personal_details_form(self,data):
        self.enter_firstname(data["first_name"])
        self.enter_lastname(data["last_name"])
        self.enter_employee_id(data["employee_id"])
        self.enter_driver_license_number(data["driver_license_number"])
        self.select_dl_exp_date(data["dl_expiry_date"])
        self.select_dob(data["dob"])
        self.select_nationality(data["nationality"])
        self.select_marital_status(data["marital_status"])


        if data["gender"].lower() == "male" :
            self.select_gender_male()
        elif data["gender"].lower() == "female":
            self.select_gender_female()

    """ Fetch the values from the Personal Details form """
    def get_personal_details_values(self):
        return {"first_name": self.get_firstname_value(),
                "last_name": self.get_lastname_value(),
                "employee_id": self.get_employee_id_value(),
                "driver_license_number": self.get_driver_license_value(),
                "dl_expiry_date": self.get_dl_exp_date(),
                "nationality": self.get_nationality(),
                "marital_status": self.get_marital_status(),
                "dob": self.get_dob_value()
                }

    """ Select a male gender radio button. """
    def select_gender_male(self):
        self.js_click(self.Gender_radio_input_male)

    """ Select a female gender radio button. """
    def select_gender_female(self):
        self.js_click(self.Gender_radio_input_female)

    """ Return True if male gender radio button is selected."""
    def is_gender_male_selected(self):
        return self.is_checked(self.Gender_radio_input_male)

    """ Return True if female gender radio button is selected."""
    def is_gender_female_selected(self):
        return self.is_checked(self.Gender_radio_input_female)

    # Custom Fields Section


    """ Return True if custom field title exist . """
    def is_custom_field_title_exist(self):
        return self.is_visible(self.Custom_fields_title)

    """ Select value from Blood type Dropdown. """
    def select_blood_type(self, blood_type):
        self.select_from_dropdown(self.Blood_type_dropdown, blood_type)

    """ Enter Test field value."""
    def enter_test_field(self, test_field):
        self.do_clear(self.Test_field_input)
        self.do_send_keys(self.Test_field_input,test_field)

    """ Click the save button"""
    def click_CF_save_button(self):
        self.wait_for_loader_to_disappear(self.Form_loader)
        self.do_click(self.CF_save_button)
        self.wait_for_loader_to_disappear(self.Form_loader)

    """ Return the selected blood type."""
    def get_blood_type(self):
        return self.get_element_text(self.Blood_type_dropdown)

    """ Return the test field value."""
    def get_test_field_value(self):
        element = self.driver.find_element(*self.Test_field_input)
        return element.get_attribute("value")

    """ Scroll page to custom field  section"""
    def scroll_to_custom_field_section(self):
        element = self.get_element(self.Custom_fields_title)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)



    # Add Attachment Section

    """ Return True if  attachment title exist. """
    def is_attachment_title_exist(self):
        return self.is_visible(self.Attachments_title)

    """ Return True if add attachment  title exist. """
    def is_add_attachment_title_exist(self):
        return self.is_visible(self.Add_attachment_title)

    """ Click the Add Attachment save button. """
    def click_add_button(self):
        self.do_click(self.Add_button)

    """ Return True if browse option enabled. """

    def verify_browse_option_enabled(self):
        return self.is_enabled(self.Browse_option)

    """" Return True if No file selected message displayed. """

    def is_no_file_selected_message_displayed(self):
        return self.is_visible(self.No_file_selected_message)

    """" Return True if file accepts upto 1MB  message displayed."""
    def is_accepts_up_to_1MB_message_displayed(self):
        return self.is_visible(self.Accepts_up_to_1MB_message)

    """ Returns True if comment label  exist. """

    def is_comment_label_exist(self):
        return self.is_visible(self.Comment_label)

    """ Enter the  comments. """
    def enter_type_comment_here(self, comment_text):
        self.do_clear(self.Type_comment_here_textarea)
        self.do_send_keys(self.Type_comment_here_textarea, comment_text)

    """ Get the value of comments entered. """
    def get_type_comment_text(self):
        element = self.driver.find_element(*self.Type_comment_here_textarea)
        return element.get_attribute("value")

    """" Returns True if file type not allowed message displayed."""
    def is_file_type_not_allowed_message_visible(self):
        return  self.is_visible(self.File_type_not_allowed_message)

    """ Uploads the attachment. """

    def upload_file(self,file_path):
        self.do_send_file(self.Browse_attach_file,file_path)
        self.click_attachment_save_button()

    """ Scroll page to add attachment section. """
    def scroll_to_add_attachment_section(self):
        element = self.get_element(self.Attachments_title)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    """ Clicks the attachment save button """
    def click_attachment_save_button(self):
        self.wait_for_loader_to_disappear(self.Form_loader)
        self.do_click(self.Attachment_Save_button)
        self.wait_for_loader_to_disappear(self.Form_loader)

    """ Returns True if the file appears in the attachment results table (waits for the row to be visible). """
    def is_file_present_in_results_with_wait(self,file_name):
        locator = (By.XPATH, f"//div[contains(@class,'oxd-table-row')]//div[normalize-space()='{file_name}']")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    """ Returns True if the file exists in the attachment results table (no wait). """
    def is_file_present_in_results(self, file_name):
        locator = (By.XPATH, f"//div[contains(@class,'oxd-table-row')]//div[normalize-space()='{file_name}']")
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0


    """ Select the file checkbox to be deleted. """
    def select_attachment_checkbox(self, file_name):
        checkbox_locator = (
            By.XPATH,
            f"//div[normalize-space()='{file_name}']"
            f"/ancestor::div[contains(@class,'oxd-table-row')]"
            f"//input[@type='checkbox']/ancestor::label")
        self.do_click(checkbox_locator)

    """ Click the Delete button"""
    def click_delete_selected_button(self):
        self.wait_for_visibility(self.Delete_selected)
        element = self.get_element(self.Delete_selected)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.js_click(self.Delete_selected)

    """ Confirm the delete popup message """
    def confirm_delete_popup(self):
        self.do_click(self.Confirm_button_popup)

    """ Delete the uploaded file attachment."""
    def confirm_delete_attachment(self, file_name):
        self.select_attachment_checkbox(file_name)
        self.wait_for_visibility(self.Delete_selected)
        self.click_delete_selected_button()
        self.confirm_delete_popup()