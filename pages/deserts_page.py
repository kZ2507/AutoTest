import time
from selenium import webdriver
from pages.base_page import BasePage
from locators.deserts_locators import DesertsLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class DesertsPage(BasePage, DesertsLocators):
    def click_menu(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.menu)).perform()
        time.sleep(1)
        self.find(self.dessert).click()

    def desert_to_basket(self):
        self.find(self.basket_button, EC.element_to_be_clickable).click()

    def move_right_slider(self):
        slider = self.find(self.right_slider, EC.element_to_be_clickable)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, -200, 0).perform()
        time.sleep(2)

    def click_apply(self):
        self.find(self.apply_button, EC.element_to_be_clickable).click()

    @property
    def get_price_1(self):
        price_1 = self.find(self.price_bulochka)
        return price_1.text

    @property
    def get_price_2(self):
        price_2 = self.find(self.price_morkovny)
        return price_2.text