from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator, condition=EC.presence_of_element_located):
        return self.wait.until(condition(locator))

    def get_value(self, locator, word):
        locator = self.wait.until(EC.visibility_of_element_located(locator))
        value_word = locator.text
        assert value_word == word

    def coupon_applied_twice_exception(self, locator, error_text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        value = element.text
        if value == error_text:
            raise Exception("Coupon code applied twice")