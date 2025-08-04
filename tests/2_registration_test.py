import time

import allure

from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.chekout_page import CheckoutPage
from pages.registration_page import RegistrationPage
from pages.my_account_page import MyAccountPage
from conftest import selenium

@allure.feature('Попытка оформления заказа неавторизованным пользователем')
def test_case_1(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Добавить в корзину любую отображенную пиццу"):
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("Нажать Перейти к оплате"):
        basket_page = BasketPage(driver)
        basket_page.pay_click()

    with allure.step("Проверить, что отображена страница с просьбой авторизации"):
        checkout_page = CheckoutPage(driver)
        checkout_page.not_authorized()

@allure.feature('Регистрация через Мой аккаунт')
def test_case_2(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать Мой аккаунт"):
        my_account_page = MyAccountPage(driver)
        my_account_page.click_account_button()

    with allure.step("Нажать Зарегистрироваться"):
        my_account_page.click_registration()

    with allure.step("Заполнить поля Имя, Адрес, Пароль и нажать Зарегистрироваться"):
        registration_page = RegistrationPage(driver)
        registration_page.registration()

@allure.feature('Оформление заказа залогированным пользователем, проверка заказа')
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
        time.sleep(4)

    with allure.step("Открыть меню и добавить пиццу в корзину"):
        main_page.open_page()
        main_page.add_pizza_1()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("Нажать Перейти к оплате"):
        basket_page = BasketPage(driver)
        basket_page.click_order()

    with allure.step("Заполнить все поля, выбрать Оплата при доставке и активировать соглашение"):
        checkout_page = CheckoutPage(driver)
        checkout_page.making_order()

    with allure.step("Нажать оформить заказ"):
        checkout_page.click_order_button()