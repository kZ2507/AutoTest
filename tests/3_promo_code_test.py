import time

import allure
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.my_account_page import MyAccountPage
from pages.chekout_page import CheckoutPage
from conftest import selenium

@allure.feature('Применение существующего промокода')
def test_case_1(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать Мой аккаунт"):
        my_account_page = MyAccountPage(driver)
        my_account_page.click_account_button()

    with allure.step("Ввести имя и пароль существующего пользователя "):
        my_account_page.authorization()

    with allure.step("Нажать Войти"):
        my_account_page.click_auth_button()

    with allure.step("Открыть меню и добавить пиццу в корзину"):
        main_page.open_page()
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("В поле для ввода купона ввести GIVEMEHALYAVA и нажать Применить"):
        basket_page = BasketPage(driver)
        basket_page.send_correct_coupon()
        basket_page.click_coupon_button()

    with allure.step("Проверить значения в заказе"):
        basket_page.coupon_applied()

@allure.feature('Применение стороннего промокода')
def test_case_2(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать Мой аккаунт"):
        my_account_page = MyAccountPage(driver)
        my_account_page.click_account_button()

    with allure.step("Ввести имя и пароль существующего пользователя "):
        my_account_page.authorization()

    with allure.step("Нажать Войти"):
        my_account_page.click_auth_button()

    with allure.step("Открыть меню и добавить пиццу в корзину"):
        main_page.open_page()
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("В поле для ввода купона ввести DC120 и нажать Применить"):
        basket_page = BasketPage(driver)
        basket_page.send_wrong_coupon()
        basket_page.click_coupon_button()

    with allure.step("Проверить значения в заказе"):
        basket_page.coupon_rejected()

@allure.feature('Проверка повторного применения промокода')
def test_case_3(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать Мой аккаунт"):
        my_account_page = MyAccountPage(driver)
        my_account_page.click_account_button()

    with allure.step("Ввести имя и пароль существующего пользователя "):
        my_account_page.authorization()

    with allure.step("Нажать Войти"):
        my_account_page.click_auth_button()

    with allure.step("Открыть меню и добавить пиццу в корзину"):
        main_page.open_page()
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("В поле для ввода купона ввести GIVEMEHALYAVA и нажать Применить"):
        basket_page = BasketPage(driver)
        basket_page.send_correct_coupon()
        basket_page.click_coupon_button()

    with allure.step("Нажать Перейти к оплате"):
        basket_page = BasketPage(driver)
        basket_page.click_order()

    with allure.step("Заполнить все поля, выбрать Оплата при доставке и активировать соглашение"):
        checkout_page = CheckoutPage(driver)
        checkout_page.making_order()

    with allure.step("Нажать оформить заказ"):
        checkout_page.click_order_button()

    with allure.step("Открыть меню и добавить пиццу в корзину"):
        main_page.open_page()
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("В поле для ввода купона ввести GIVEMEHALYAVA и нажать Применить"):
        basket_page = BasketPage(driver)
        basket_page.send_correct_coupon()
        basket_page.click_coupon_button()

    with allure.step("Проверить, что купон не применен повторно"):
        basket_page.coupon_applied_twice()