from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.order_story_page import OrderStoryPage


class TestFeed:

    def test_go_to_lk_both(self, driver):  # перенести в метод

        time.sleep(
            1)  # узнать почему если убрать эту хрень получается ElementClickInterceptedException, хотя у нас стоит ожидание 10 15 сек
        # тесты падают через раз

        go_to_main_page = MainPage(driver)
        go_to_main_page.click_go_to_account_button()  # метод клика по кнопке логина

        login_page = LoginPage(driver)

        time.sleep(2)

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    def test_click_an_order_show_details_success(self, driver):

        pass


    def test_users_orders_from_story_are_shown_in_feed_orders_are_displayed(self, driver, register_and_authorize):

        create_order = MainPage(driver)

        create_order.place_an_order()

        time.sleep(4)

        create_order.get_and_save_new_order_number()

        time.sleep(4) # доб. ожидание грамотно

        print(create_order.get_and_save_new_order_number())

        create_order.close_details_window()

        create_order.click_personal_account_button_in_header()

        # меняем страницу

        go_to_personal_account = LkPage(driver)

        go_to_personal_account.go_to_order_story_page()

        # продолжить тут






        # 1) Закрыть окно с номером заказа

        #  2) переходим в историю заказов (lk_page, метод go_to_order_story_page())

        #  3) ищем там созданный заказ

        #  4) идем в Ленту (main_page, Метод go_to_feed), ищем тоот же заказ там





    def test_overall_counter_increases_after_creating_order_success(self, driver):

        pass

    def test_today_counter_increases_after_creating_order_success(self, driver):

        pass

    def test_order_number_appears_at_in_progress_section_afted_creating_order_success(self, driver):

        pass










