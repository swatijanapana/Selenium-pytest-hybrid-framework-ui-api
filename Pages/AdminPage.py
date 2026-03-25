from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage



class AdminPage(BasePage):
    """ By Locators -- OR"""

    # User Management Tab
    User_management_tab = (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and text()= 'User Management ']")
    Add_button = (By.XPATH,"//button[@type='button' and text()=' Add ']")
    Search_button = (By.XPATH,"//button[@type='submit' and text()= ' Search ']")
    Reset_button = (By.XPATH,"//button[@type='button' and text()= ' Reset ']")
    Username_input = (By.XPATH,"//label[normalize-space()= 'Username']/following::input[1]")
    Result_table = (By.XPATH,"//div[@class='oxd-table-body']")
    Result_rows = (By.XPATH,"//div[@class='oxd-table-body']/child::div")
    No_Record_found_message = (By.XPATH,"//span[@class='oxd-text oxd-text--span' and text()='No Records Found']")
    User_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[1]")
    Status_dropdown = (By.XPATH,"//label[text()='Status']/following::div[1]")
    Form_loader = (By.CLASS_NAME, "oxd-form-loader")


    """ Constructor of page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions for Admin Page """

    # User Management Tab

    """ Return True if the User_management tab is selected by default. """
    def is_user_management_tab_selected(self):
        return self.is_visible(self.User_management_tab)

    """ Return True if the Add button is visible. """
    def is_add_button_exist(self):
        return self.is_visible(self.Add_button)

    """ Return True if the Search button is visible. """
    def is_search_button_exist(self):
        return self.is_visible(self.Search_button)

    """ Return True if the Reset button is visible. """
    def is_reset_button_exist(self):
        return self.is_visible(self.Reset_button)

    """ Enter Username field value. """
    def enter_username(self,username):
        self.do_clear(self.Username_input)
        self.do_send_keys(self.Username_input,username)

    """ Return the Username field value. """
    def get_username_value(self):
        element = self.driver.find_element(*self.Username_input)
        return element.get_attribute("value")

    """ Return the selected User role value. """
    def get_userrole_selected_text(self):
        element = self.driver.find_element(*self.User_role_dropdown)
        return element.text

    """ Return the selected status  value. """
    def get_status_selected_text(self):
        element = self.driver.find_element(*self.Status_dropdown)
        return element.text

    """ Returns True if  entered Username value appears in result table. """
    def is_username_present_results(self,username):
        locator = (By.XPATH, f"//div[contains(@class,'oxd-table-row')]//div[normalize-space()='{username}']")
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0


    """ Click Search button. """
    def click_search_button(self):
        return self.do_click(self.Search_button)

    """ Click Reset button."""
    def click_reset_button(self):
        return self.do_click(self.Reset_button)

    """ Returns True if No record found message is displayed"""
    def is_no_record_found_message_displayed(self):
        return self.is_visible(self.No_Record_found_message)

    """ Select item from dropdown"""
    def select_from_dropdown(self,dropdown_locator,option_text):
        #click dropdown
        self.do_click(dropdown_locator)
        #select option  with matching visible text
        option = (By.XPATH,f"//div[normalize-space()='{option_text}']")
        self.do_click(option)

    """ Count the total rows in results table"""
    def get_row_result_count(self):
        rows = self.driver.find_elements(*self.Result_rows)
        return len(rows)

    """ Wait until the page loader disappears. """

    def wait_for_form_loader(self):
        self.wait_for_loader_to_disappear(self.Form_loader)






