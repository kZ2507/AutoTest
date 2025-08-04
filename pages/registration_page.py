from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage, RegistrationLocators):
    def send_name_field(self):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys("6testtesttest")

    def send_email_field(self):
        self.find(self.email_field, EC.element_to_be_clickable).send_keys("testtest@test.te")

    def send_password_field(self):
        self.find(self.password_field, EC.element_to_be_clickable).send_keys("12345test")

    def click_registration_button(self):
        self.find(self.registration_button, EC.element_to_be_clickable).click()

    def registration(self):
        self.send_name_field()
        self.send_email_field()
        self.send_password_field()
        self.click_registration_button()