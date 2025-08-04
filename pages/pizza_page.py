from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from locators.pizza_locators import PizzaLocators
from selenium.webdriver.support import expected_conditions as EC

class PizzaPage(BasePage, PizzaLocators):

    def check_pizza_info(self):
        self.get_value(self.description, "ОПИСАНИЕ")

    def click_board(self):
        select = Select(self.find(self.choose_board, EC.element_to_be_clickable))
        select.select_by_visible_text("Колбасный - 65.00 р.")

    def click_basket_button(self):
        self.find(self.basket_button, EC.element_to_be_clickable).click()