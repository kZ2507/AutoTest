from selenium.webdriver.common.by import By

class PizzaLocators:
    description = (By.XPATH, '//li[@id="tab-title-description"]')
    choose_board = (By.XPATH, '//select[@id="board_pack"]')
    basket_button = (By.XPATH, '//button[@name="add-to-cart"]')
    basket = (By.XPATH, '(//a[contains(text(), "Корзина")])[1]')