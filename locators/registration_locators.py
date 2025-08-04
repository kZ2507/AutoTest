from selenium.webdriver.common.by import By

class RegistrationLocators:
    name_field = (By.XPATH, '//input[@id="reg_username"]')
    email_field = (By.XPATH, '//input[@id="reg_email"]')
    password_field = (By.XPATH, '//input[@id="reg_password"]')
    registration_button = (By.XPATH, '//button[@name="register"]')