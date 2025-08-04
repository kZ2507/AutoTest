import time
from selenium.common import StaleElementReferenceException
from selenium import webdriver
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage, MainLocators):
    url = "https://pizzeria.skillbox.cc/"
    def open_page(self):
            self.driver.get(self.url)

    def click_pizza_1(self):
        self.find(self.pizza_1, EC.element_to_be_clickable).click()

    def add_pizza_1(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.pizza_1)).perform()
        self.find(self.pizza_1, EC.element_to_be_clickable)
        self.find(self.pizza1_add_cart, EC.element_to_be_clickable).click()

    def add_pizza_2(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.pizza_2)).perform()
        self.find(self.pizza_2, EC.element_to_be_clickable)
        self.find(self.pizza2_add_cart, EC.element_to_be_clickable).click()

    def add_pizza_3(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.pizza_3)).perform()
        self.find(self.pizza_3, EC.element_to_be_clickable)
        self.find(self.pizza3_add_cart, EC.element_to_be_clickable).click()

    def click_basket(self):
        for i in range(3):
            try:
                self.find(self.basket, EC.element_to_be_clickable).click()
                break
            except StaleElementReferenceException:
                time.sleep(1)

    def open_basket(self):
            self.click_basket()
            time.sleep(1)

    def click_left_slider(self):
        self.find(self.prev_slider).click()

    def click_right_slider(self):
        self.find(self.next_slider).click()

    def click_dessert_menu(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.menu)).perform()
        time.sleep(1)
        self.find(self.dessert).click()
        time.sleep(1)

    def click_bonus_program(self):
        self.find(self.bonus_program).click()

