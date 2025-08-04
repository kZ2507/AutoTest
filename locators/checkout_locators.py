from selenium.webdriver.common.by import By

class CheckoutLocators:
    be_authorized = (By.XPATH, "//a[contains(text(), 'Авторизируйтесь')]")
    first_name = (By.XPATH, '//input[@id="billing_first_name"]')
    last_name = (By.XPATH, '//input[@id="billing_last_name"]')
    city = (By.XPATH, '//input[@id="billing_city"]')
    address = (By.XPATH, '//input[@id="billing_address_1"]')
    state = (By.XPATH, '//input[@id="billing_state"]')
    postcode = (By.XPATH, '//input[@id="billing_postcode"]')
    phone = (By.XPATH, '//input[@id="billing_phone"]')
    payment = (By.XPATH, '//input[@id="payment_method_cod"]')
    agreement = (By.XPATH, '//input[@id="terms"]')
    order_date = (By.XPATH, '//input[@id="order_date"]')
    place_order = (By.XPATH, '//button[@id="place_order"]')
