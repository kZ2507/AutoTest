from selenium.webdriver.common.by import By

class MainLocators:
    pizza_1 = (By.XPATH, '(//div[@class="item-img"])[5]')
    pizza_2 = (By.XPATH, '(//div[@class="item-img"])[6]')
    pizza_3 = (By.XPATH, '(//div[@class="item-img"])[7]')
    pizza_4 = (By.XPATH, '(//div[@class="item-img"])[8]')
    pizza_5 = (By.XPATH, '(//div[@class="item-img"])[9]')
    pizza1_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[5]')
    pizza2_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[6]')
    pizza3_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[7]')
    pizza5_add_cart = (By.XPATH, '(//a[@class="button product_type_simple add_to_cart_button ajax_add_to_cart"])[9]')
    prev_slider = (By.XPATH, '//a[@class="slick-prev"]')
    next_slider = (By.XPATH, '//a[@class="slick-next"]')
    basket = (By.XPATH, '(//a[contains(text(), "Корзина")])[1]')
    menu = (By.XPATH, '//li[@id="menu-item-389"]')
    dessert = (By.XPATH, '//li[@id="menu-item-391"]')
    order = (By.XPATH, '//li[@id="menu-item-31"]')
    bonus_program = (By.XPATH, '//li[@id="menu-item-363"]')