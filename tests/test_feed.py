from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from pages.feed_page import FeedPage
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

        go_to_feed = MainPage(driver)
        go_to_feed.go_to_feed()

        get_first_order = FeedPage(driver)
        get_first_order.get_first_order_of_feed_list()

        assert get_first_order.return_order_window().is_displayed()

    def test_users_orders_from_story_are_shown_in_feed_orders_are_displayed(self, driver, register_and_authorize): # работает

        create_order = MainPage(driver)
        create_order.place_an_order()

        number = create_order.get_and_save_new_order_number() # записываем номер созданного заказа в переменную

        print(create_order.get_and_save_new_order_number())
        create_order.close_details_window()
        create_order.click_personal_account_button_in_header()

        # меняем страницу

        go_to_personal_account = LkPage(driver)
        go_to_personal_account.go_to_order_story_page()

        # теперь скрипт прокрутки

        go_to_personal_account.scroll_to_last_order()
        print(go_to_personal_account.scroll_to_last_order().text)   # тут номер заказа

        go_to_feed = MainPage(driver)
        go_to_feed.go_to_feed()

        get_first_order = FeedPage(driver)
        get_first_order.get_first_order_of_feed_list()

        get_first_order.check_order_number()
        print(get_first_order.check_order_number())

        time.sleep(3)

        assert number in get_first_order.check_order_number()
    # 1) Закрыть окно с номером заказа

        #  2) переходим в историю заказов (lk_page, метод go_to_order_story_page())

        #  3) ищем там созданный заказ

        #  4) идем в Ленту (main_page, Метод go_to_feed), ищем тоот же заказ там

    def test_overall_counter_increases_after_creating_order_success(self, driver, register_and_authorize):

        # фиксируем значение счетчика

        feed = MainPage(driver)
        feed.go_to_feed()

        save_orders_before_adding = FeedPage(driver)
        count_of_orders = save_orders_before_adding.get_overall_counter()  # кол-во заказов ДО

        get_overall_counter = FeedPage(driver)

        print(get_overall_counter.get_overall_counter())
        time.sleep(3)

        # переходим в конструктор

        get_overall_counter.go_to_constructor()

        create_order = MainPage(driver)
        create_order.place_an_order()

        create_order.close_details_window()

        time.sleep(3)

        create_order.go_to_feed()

        time.sleep(2)

        back_to_feed = FeedPage(driver)

      #  back_to_feed.go_

        count_of_orders_after_addind_one = back_to_feed.get_overall_counter()
        print(get_overall_counter.get_overall_counter())
        print(count_of_orders)
        print(count_of_orders_after_addind_one)

        assert int(count_of_orders_after_addind_one) > int(count_of_orders)

        assert (int(count_of_orders) + 1 ) == int(count_of_orders_after_addind_one)

    def test_today_counter_increases_after_creating_order_success(self, driver, register_and_authorize):

        feed = MainPage(driver)
        feed.go_to_feed()

        save_orders_before_adding = FeedPage(driver)
        count_of_orders = save_orders_before_adding.get_daily_counter()  # кол-во заказов ДО

        get_daily_counter = FeedPage(driver)

        print(get_daily_counter.get_daily_counter())
        time.sleep(3)

        get_daily_counter.go_to_constructor()

        create_order = MainPage(driver)
        create_order.place_an_order()

        create_order.close_details_window()

        time.sleep(3)

        create_order.go_to_feed()

        time.sleep(2)

        back_to_feed = FeedPage(driver)

        count_of_orders_after_addind_one = back_to_feed.get_daily_counter()

      #  print(get_overall_counter.get_overall_counter())
        print(count_of_orders)
        print(count_of_orders_after_addind_one)

        assert (int(count_of_orders) + 1 ) == int(count_of_orders_after_addind_one)

        # если что просто поставить >



    def test_order_number_appears_at_in_progress_section_afted_creating_order_success(self, driver, register_and_authorize):

        create_order = MainPage(driver)
        create_order.place_an_order()

        order_number_after_creating_order = create_order.get_and_save_new_order_number() # записываем номер созданного заказа в переменную

        print(create_order.get_and_save_new_order_number())
        create_order.close_details_window()
        create_order.click_personal_account_button_in_header()

        # меняем страницу

        create_order.go_to_feed()
        get_number = FeedPage(driver)
        order_number_at_in_progress_sector = get_number.check_if_created_order_has_appeared_at_in_progress_section()
        print(get_number.check_if_created_order_has_appeared_at_in_progress_section())

        assert order_number_after_creating_order in order_number_at_in_progress_sector


# продолжить тут









