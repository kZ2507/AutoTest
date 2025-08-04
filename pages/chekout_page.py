import time
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage, CheckoutLocators):
    def not_authorized(self):
        for i in range(3):
            try:
                self.find(self.be_authorized, EC.element_to_be_clickable).click()
                break
            except TimeoutException:
                time.sleep(1)

    def send_first_name(self):
        field = self.find(self.first_name, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Тест")

    def send_last_name(self):
        field = self.find(self.last_name, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Тест")

    def send_address(self):
        field = self.find(self.address, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Тест 11")

    def send_city(self):
        field = self.find(self.city, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Тест")

    def send_state(self):
        field = self.find(self.state, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("Тест Тест")

    def send_postcode(self):
        field = self.find(self.postcode, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("111111")

    def send_phone(self):
        field = self.find(self.phone, EC.element_to_be_clickable)
        field.clear()
        field.send_keys("+79877887878")

    def click_payment(self):
        self.find(self.payment, EC.element_to_be_clickable).click()

    def click_agreement(self):
        self.find(self.agreement, EC.element_to_be_clickable).click()


    def send_order_date(self):
        field = self.find(self.order_date, EC.element_to_be_clickable)
        field.send_keys("01")
        field.send_keys("01")
        field.send_keys("2025")

    def making_order(self):
            self.send_first_name()
            self.send_last_name()
            self.send_address()
            self.send_city()
            self.send_state()
            self.send_postcode()
            self.send_phone()
            self.click_payment()
            self.click_agreement()
            self.send_order_date()

    def click_order_button(self):
        self.find(self.place_order, EC.element_to_be_clickable).click()
