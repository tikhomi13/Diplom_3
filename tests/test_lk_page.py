import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLs

from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from locators.lk_page_locators import LkPageLocators

from locators.login_page_locators import LoginPageLocators


from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

#from conftest import driver

from pages.login_page import LoginPage


class TestLkPage:



    def test_go_to_personal_account_click_on_personal_account_button_transition_succeeded(self):

        print(123) # Проверить переход по клику на «Личный кабинет»

    def test_go_to_order_story_click_on_order_story_button_transition_succeeded(self):

        print(123) # Проверить переход в раздел «История заказов»

    def test_exit_personal_account_press_exit_button_success(self, driver, register_and_authorize):  # тут фикстура на логин и регистер

        click = MainPage(driver)
        click.click_personal_account_button_in_header()

        logout = LkPage(driver)
        # проверяем что мешающий элемент не отображается
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        logout.logout()

        login_page = LoginPage(driver)
        login_page.get_vhod_text_on_login_page()

        assert login_page.get_vhod_text_on_login_page().is_displayed() # проверка что отображается текст "Вход" после логаута

    # ПРОДОЛЖИТЬ ТУТ. ПРроверка основного ф-ционала, раздел "Лента заказов" 