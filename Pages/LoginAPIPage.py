from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class APILoginPage(BasePage):
    """ By Locators -- OR"""
    Email = (By.XPATH, "//form[@action='/login']//input[@placeholder='Email Address']")
    Password = (By.XPATH, "//form[@action='/login']//input[@placeholder='Password']")
    Login_button = (By.XPATH, "//form[@action='/login']//button[@type='submit']")
    Logged_in_message = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def open_browser(self):
        self.driver.get("https://automationexercise.com/login")

    def login(self,email,password):
        self.do_send_keys(self.Email, email)
        self.do_send_keys(self.Password,password)
        self.do_click(self.Login_button)

    def get_logged_in_text(self):
        return self.get_element_text(self.Logged_in_message)
