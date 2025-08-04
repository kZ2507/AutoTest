import allure
from pages.main_page import MainPage
from pages.bonus_page import BonusPage
from conftest import selenium

@allure.feature('Регистрация в бонусной программе')
def test_case_1(selenium):
    driver = selenium

    with allure.step("Открыть Pizzeria — Пиццерия"):
        main_page = MainPage(driver)
        main_page.open_page()

    with allure.step("Нажать Бонусная программа"):
        main_page.click_bonus_program()

    with allure.step("Заполнить поля Имя и Телефон"):
        bonus_page = BonusPage(driver)
        bonus_page.send_info()

    with allure.step("Нажать Оформить карту"):
        bonus_page.get_bonus()