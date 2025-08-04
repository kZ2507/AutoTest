import time
from selenium.common import StaleElementReferenceException, TimeoutException
from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class BasketPage(BasePage, BasketLocators):
    def assert_pizza_3(self):
        self.get_value(self.pizza_3, 'Пицца "Рай"')

    def assert_pizza_1(self):
        self.get_value(self.pizza_1, 'Пицца "4 в 1"')

    def assert_pizza_board(self):
        self.get_value(self.options, "Колбасный борт")

    def edit_quantity(self):
        field = self.find(self.quantity_field, EC.element_to_be_clickable)
        field.click()
        field.send_keys(Keys.BACKSPACE)
        field.send_keys("3")
        field.send_keys(Keys.RETURN)

    def submit_button_click(self):
        for i in range(3):
            try:
                self.find(self.submit_button, EC.element_to_be_clickable).click()
                break
            except StaleElementReferenceException:
                time.sleep(1)
            except TimeoutException:
                time.sleep(1)


    def submit_button_work(self):
        self.submit_button_click()
        time.sleep(1)

    def delite_pizza(self):
        self.find(self.del_pizza, EC.element_to_be_clickable).click()

    @property
    def get_cost(self):
        price = self.find(self.cost)
        return price.text

    def find_empty(self):
        self.find(self.basket_empty, EC.element_to_be_clickable)

    def find_desert(self):
        self.find(self.desert, EC.element_to_be_clickable)

    def assert_desert(self):
        self.find_desert()
        self.get_value(self.desert, 'Десерт "Булочка с корицей"')

    def pay_click(self):
        self.find(self.order_button, EC.element_to_be_clickable).click()

    def click_order(self):
        self.find(self.order_button, EC.element_to_be_clickable).click()

    def send_correct_coupon(self):
        self.find(self.coupon_field, EC.element_to_be_clickable).send_keys("GIVEMEHALYAVA")

    def send_wrong_coupon(self):
        self.find(self.coupon_field, EC.element_to_be_clickable).send_keys("DC120")

    def click_coupon_button(self):
        self.find(self.apply_coupon, EC.element_to_be_clickable).click()

    def coupon_applied(self):
        self.get_value(self.message_coupon_applied, "Coupon code applied successfully.")

    def coupon_rejected(self):
        self.get_value(self.message_coupon_rejected, "Неверный купон.")

    def coupon_applied_twice(self):
            self.coupon_applied_twice_exception(self.message_coupon_applied, "Coupon code applied successfully.")

    def simulate_coupon_error(self):
        self.driver.execute_script("window.fetch = function() { return Promise.reject('Network error'); };")