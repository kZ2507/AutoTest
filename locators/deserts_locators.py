from selenium.webdriver.common.by import By

class DesertsLocators:
    right_slider = (By.XPATH, '(//span[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]')
    apply_button = (By.XPATH, '//button[contains(text(), "Применить")]')
    basket_button = (By.XPATH, '(//a[contains(text(), "В корзину")])[1]')
    dessert = (By.XPATH, '//h1[@class="entry-title ak-container"]')
    menu = (By.XPATH, '//li[@id="menu-item-389"]')
    price_bulochka = (By.XPATH, "(//span[@class='price']/span[@class='woocommerce-Price-amount amount'])[1]")
    price_morkovny = (By.XPATH, "(//span[@class='price']/span[@class='woocommerce-Price-amount amount'])[2]")