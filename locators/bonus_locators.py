from selenium.webdriver.common.by import By

class BonusLocators:
    name_field = (By.XPATH, '//input[@id="bonus_username"]')
    phone_field = (By.XPATH, '//input[@id="bonus_phone"]')
    bonus_button = (By.XPATH, '//button[@name="bonus"]')
    card_exist = (By.XPATH, '//h3[contains(text(), "Ваша карта оформлена!")]')