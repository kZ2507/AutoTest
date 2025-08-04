from pages.base_page import BasePage
from locators.my_account_locators import MyAccount
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage(BasePage, MyAccount):
    def click_account_button(self):
        self.find(self.account_button, EC.element_to_be_clickable).click()

    def click_registration(self):
        self.find(self.registration_button, EC.element_to_be_clickable).click()

    def send_name(self):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys("testtesttest098")

    def send_password(self):
        self.find(self.password_field, EC.element_to_be_clickable).send_keys("12345testtest")

    def click_auth_button(self):
        self.find(self.authorization_button, EC.element_to_be_clickable).click()

    def authorization(self):
        self.send_name()
        self.send_password()