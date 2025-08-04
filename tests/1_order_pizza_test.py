import time

import allure
from pages.deserts_page import DesertsPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.pizza_page import PizzaPage
from conftest import selenium

@allure.feature('Добавление пиццы в корзину с главной страницы и проверка содержимого корзины + прокрутка слайдера')
def test_case_1(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Добавить пиццу в корзину"):
        main_page.add_pizza_3()

    with allure.step("Нажать на стрелку справа для прокрутки слайдера, затем слева"):
        main_page.click_right_slider()
        main_page.click_left_slider()

    with allure.step("Нажать на значок корзины"):
        main_page.open_basket()

    with allure.step("Проверить содержимое "):
        basket_page = BasketPage(driver)
        basket_page.assert_pizza_3()

@allure.feature('Проверка страницы пиццы + заказ пиццы с дополнительными опциями, проверка содержимого корзины')
def test_case_2(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать на любую пиццу"):
        main_page.click_pizza_1()

    with allure.step("Проверить информацию на странице"):
        pizza_page = PizzaPage(driver)
        time.sleep(1)
        pizza_page.check_pizza_info()

    with allure.step("В поле выбора борта выбрать любую опцию"):
        pizza_page.click_board()

    with allure.step("Нажать В корзину"):
        pizza_page.click_basket_button()

    with allure.step("Нажать на значок корзины"):
        main_page.open_basket()

    with allure.step("Проверить содержимое"):
        basket_page = BasketPage(driver)
        basket_page.assert_pizza_board()
        basket_page.assert_pizza_1()

@allure.feature('Добавление пиццы, увеличение количества в корзине, удаление пиццы')
def test_case_3(selenium):
    driver = selenium
    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Добавить в корзину любую отображенную пиццу"):
        main_page.add_pizza_2()

    with allure.step("Открыть корзину"):
        main_page.open_basket()

    with allure.step("Изменить количество пицц"):
        basket_page = BasketPage(driver)
        basket_page.edit_quantity()

    with allure.step("Нажать обновить"):
        basket_page.submit_button_work()

    with allure.step("Проверить изменение стоимости"):
        assert basket_page.get_cost == '1440,00₽'

    with allure.step("Удалить с помощью крестика"):
        basket_page.delite_pizza()
        basket_page.find_empty()

@allure.feature('Открытие раздела десерты, добавление десерта в корзину')
def test_case_4(selenium):
    driver = selenium
    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать меню, в выпадающем списке выбрать Десерты"):
        main_page.click_dessert_menu()

    with allure.step("Добавить любой десерт в корзину"):
        desert_page = DesertsPage(driver)
        desert_page.desert_to_basket()

    with allure.step("Проверить корзину"):
        main_page.open_basket()
        basket_page = BasketPage(driver)
        basket_page.assert_desert()

@allure.feature('Ввод ограничения на 140р, проверка соответствия ')
def test_case_5(selenium):
    driver = selenium
    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать меню, в выпадающем списке выбрать Десерты"):
        main_page.click_dessert_menu()

    with allure.step("В блоке Фильтровать по цене выбрать до 140р"):
        desert_page = DesertsPage(driver)
        desert_page.move_right_slider()

    with allure.step("Нажать Применить"):
        desert_page.click_apply()

    with allure.step("Проверить соответствие"):
        assert desert_page.get_price_1 <= "140"
        assert desert_page.get_price_2 <= "140"