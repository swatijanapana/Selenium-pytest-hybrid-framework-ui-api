import pytest

import Constants.constants as constants
from Tests.UI.base_test import BaseTest


@pytest.mark.ui
@pytest.mark.regression
class Test_Home(BaseTest):

    """ Home Page test cases. """

    def get_home_page(self):
        """ Log in and navigate to Home page. """
        return self.login_and_get_home()

    def test_home_page_title(self):
        """Verify home page title is displayed correctly."""
        homePage = self.get_home_page()
        homepage_title = homePage.get_home_page_title(constants.HOME_PAGE_TITLE)
        assert homepage_title == constants.HOME_PAGE_TITLE

    def test_home_page_header_value_dashboard(self):
        """ Verify dashboard header value is displayed on home page. """
        self.homePage = self.get_home_page()
        header_value = self.homePage.get_header_value()
        assert header_value == constants.HOME_PAGE_HEADER_VALUE

    def test_orangehrm_logo_exist(self):
        """ Verify logo icon is visible on home page. """
        self.homePage = self.get_home_page()
        assert  self.homePage.is_logo_exist()

    def test_profile_icon_exist(self):
        """ Verify profile icon is visible on home page. """
        self.homePage = self.get_home_page()
        assert  self.homePage.is_profile_picture_exist()

    def test_left_menu_visible(self):
        """ Verify menu on the left  visible on home page. """
        self.homePage = self.get_home_page()
        assert self.homePage.is_menu_list_exist()

    def test_left_sidebar_menu_items_displayed(self):
        """ Verify the left sidebar menu displays all expected modules after user login. """
        self.homePage = self.get_home_page()
        actual_menu = self.homePage.get_menu_items_text()
        assert actual_menu == constants.HOME_MENU_ITEMS

    @pytest.mark.smoke
    def test_click_admin_menu(self):
        """ Verify Admin navigation menu works correctly. """
        self.homePage = self.get_home_page()
        self.homePage.click_admin_menu()
        assert self.homePage.get_header_value() == constants.ADMIN_PAGE_HEADER_VALUE

    def test_click_myinfo_menu(self):
        """ Verify MyInfo menu navigation works correctly. """
        self.homePage = self.get_home_page()
        self.homePage.click_myinfo_menu()
        assert self.homePage.get_header_value() == constants.MYINFO_PAGE_HEADER_VALUE

    def test_logout(self):
        """ Verify user can log out of the application """
        self.homePage = self.get_home_page()
        self.homePage.do_logout()
        assert self.driver.title == constants.LOGIN_PAGE_TITLE



