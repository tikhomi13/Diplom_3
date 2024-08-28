import allure
from pages.main_page import MainPage
from pages.lk_page import LkPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage


class TestFeed:

    @allure.title('Проверка перехода в лк')
    def test_go_to_lk_both(self, driver):

        go_to_main_page = MainPage(driver)
        go_to_main_page.sleep()

        go_to_main_page.lk_clickable() #
        go_to_main_page.click_go_to_account_button()
        login_page = LoginPage(driver)

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_an_order_show_details_success(self, driver):

        go_to_feed = MainPage(driver)
        go_to_feed.sleep()
        go_to_feed.go_to_feed()

        get_first_order = FeedPage(driver)
        get_first_order.get_first_order_of_feed_list()

        assert get_first_order.return_order_window().is_displayed()

    @allure.title('Заказы пользователя из Истории закзов отображаются на странице Лента зказов')
    def test_users_orders_from_story_are_shown_in_feed_orders_are_displayed(self, driver, register_and_authorize):

        create_order = MainPage(driver)
        create_order.sleep()
        create_order.place_an_order()
        number = create_order.get_and_save_new_order_number()
        create_order.close_details_window()
        create_order.click_personal_account_button_in_header()

        go_to_personal_account = LkPage(driver)
        go_to_personal_account.go_to_order_story_page()

        go_to_personal_account.scroll_to_last_order()
        go_to_feed = MainPage(driver)
        go_to_feed.go_to_feed()

        get_first_order = FeedPage(driver)
        get_first_order.get_first_order_of_feed_list()
        get_first_order.check_order_number()

        assert number in get_first_order.check_order_number()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_overall_counter_increases_after_creating_order_success(self, driver, register_and_authorize):

        feed = MainPage(driver)
        feed.sleep()
        feed.go_to_feed()

        save_orders_before_adding = FeedPage(driver)
        count_of_orders = save_orders_before_adding.get_overall_counter()

        get_overall_counter = FeedPage(driver)
        get_overall_counter.go_to_constructor()

        create_order = MainPage(driver)
        create_order.place_an_order()

        create_order.close_details_window()

        create_order.go_to_feed()
        back_to_feed = FeedPage(driver)

        count_of_orders_after_addind_one = back_to_feed.get_overall_counter()
        assert int(count_of_orders_after_addind_one) > int(count_of_orders)
        assert (int(count_of_orders) + 1 ) == int(count_of_orders_after_addind_one)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_counter_increases_after_creating_order_success(self, driver, register_and_authorize):

        feed = MainPage(driver)
        feed.go_to_feed()

        save_orders_before_adding = FeedPage(driver)
        count_of_orders = save_orders_before_adding.get_daily_counter()

        get_daily_counter = FeedPage(driver)
        get_daily_counter.go_to_constructor()

        create_order = MainPage(driver)
        create_order.place_an_order()
        create_order.close_details_window()
        create_order.go_to_feed()
        back_to_feed = FeedPage(driver)

        count_of_orders_after_addind_one = back_to_feed.get_daily_counter()
        assert (int(count_of_orders) + 1 ) == int(count_of_orders_after_addind_one)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_number_appears_at_in_progress_section_after_creating_order_success(self, driver, register_and_authorize):

        create_order = MainPage(driver)
        create_order.sleep()
        create_order.place_an_order()

        order_number_after_creating_order = create_order.get_and_save_new_order_number()
        create_order.close_details_window()
        create_order.go_to_feed()
        get_number = FeedPage(driver)
        order_number_at_in_progress_sector = get_number.check_if_created_order_has_appeared_at_in_progress_section()

        assert order_number_after_creating_order in order_number_at_in_progress_sector
