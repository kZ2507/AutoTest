import time
from pages.base_page import BasePage
from locators.bonus_locators import BonusLocators
from selenium.webdriver.support import expected_conditions as EC

class BonusPage(BasePage, BonusLocators):
    def send_name(self, name):
        self.find(self.name_field, EC.element_to_be_clickable).send_keys(name)

    def send_phone(self, phone):
        self.find(self.phone_field, EC.element_to_be_clickable).send_keys(phone)

    def click_apply_card_button(self):
        self.find(self.bonus_button, EC.element_to_be_clickable).click()

    def send_info(self):
            self.send_name("Тест")
            self.send_phone("+77777777777")

    def get_bonus(self):
            self.click_apply_card_button()
            time.sleep(1)
            self.driver.switch_to.alert.accept()
            self.get_value(self.card_exist, "Ваша карта оформлена!")