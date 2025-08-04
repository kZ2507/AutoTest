from selenium.webdriver.common.by import By

class BasketLocators:
    quantity_field = (By.XPATH, '(//input[@class="input-text qty text"])[1]')
    pizza_1 = (By.LINK_TEXT, 'Пицца "4 в 1"')
    pizza_2 = (By.LINK_TEXT, 'Пицца "Как у бабушки"')
    pizza_3 = (By.LINK_TEXT, 'Пицца "Рай"')
    pizza_4 = (By.LINK_TEXT, 'Пицца "Ветчина и грибы"')
    pizza_5 = (By.LINK_TEXT, 'Пицца "Пепперони"')
    options = (By.XPATH, '//dd[@class="variation-"]')
    del_pizza = (By.XPATH, '(//a[@aria-label="Remove this item"])')
    desert = (By.LINK_TEXT, 'Десерт "Булочка с корицей"')
    order_button = (By.XPATH, '//a[normalize-space(text())="ПЕРЕЙТИ К ОПЛАТЕ"]')
    coupon_field = (By.XPATH, '//input[@id="coupon_code"]')
    apply_coupon = (By.XPATH, '//button[@name="apply_coupon"]')
    message_coupon_applied = (By.XPATH, '//div[@class="woocommerce-message"]')
    message_coupon_rejected = (By.XPATH, '//ul[@class="woocommerce-error"]')
    submit_button = (By.XPATH, '//button[@name="update_cart"]')
    cost = (By.XPATH, "//td[@class='product-subtotal']/span[@class='woocommerce-Price-amount amount']")
    basket_empty = (By.XPATH,
                    "//p[contains(@class, 'cart-empty') and contains(@class, 'woocommerce-info') and text()='Корзина пуста.']")