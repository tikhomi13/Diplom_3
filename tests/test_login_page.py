import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLs

from pages.main_page import MainPage
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

from conftest import driver_chrome
from conftest import driver_firefox

from pages.lk_page import LkPage


class TestLkPage:

    def test_go_to_lk(self, driver_chrome):

        go_to_main_page = MainPage(driver_chrome)
        go_to_main_page.click_go_to_account_button()



        login_page = LkPage(driver_chrome)

        time.sleep(3)

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    def test_go_to_lk_firefox(self, driver_firefox):

        time.sleep(1)  # узнать почему если убрать эту хрень получается ElementClickInterceptedException, хотя у нас стоит ожидание 10 15 сек


        go_to_main_page = MainPage(driver_firefox)
        go_to_main_page.click_go_to_account_button()

        login_page = LkPage(driver_firefox)

        time.sleep(2)

        assert login_page.get_vhod_text_on_login_page().is_displayed()



    print(123)