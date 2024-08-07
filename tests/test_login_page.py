import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLs

from pages.main_page import MainPage
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

#from conftest import driver

from pages.login_page import LoginPage
import pytest


class TestLoginPage:

    def test_go_to_lk_both(self, driver):

        time.sleep(1)  # узнать почему если убрать эту хрень получается ElementClickInterceptedException, хотя у нас стоит ожидание 10 15 сек
# тесты падают через раз

        go_to_main_page = MainPage(driver)
        go_to_main_page.click_go_to_account_button()  # метод клика по кнопке логина

        login_page = LoginPage(driver)

        time.sleep(2)

        assert login_page.get_vhod_text_on_login_page().is_displayed()


