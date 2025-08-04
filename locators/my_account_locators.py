from selenium.webdriver.common.by import By

class MyAccount:
    account_button = (By.XPATH, '//li[@id="menu-item-30"]')
    registration_button = (By.XPATH, '//button[@class="custom-register-button"]')
    name_field = (By.XPATH, '//input[@id="username"]')
    email_field = (By.XPATH, '//input[@id="reg_email"]')
    password_field = (By.XPATH, '//input[@id="password"]')
    authorization_button = (By.XPATH, '//button[@name="login"]')
    field_error = (By.XPATH, '//ul[@class="woocommerce-error"]/li')
    forget_password = (By.LINK_TEXT, "Забыли пароль?")
    reset_password_field = (By.XPATH, '//input[@name="user_login"]')
    reset_button = (By.XPATH, '//button[@value="Reset password"]')
    message = (By.XPATH, '//div[@class="woocommerce-message"]')