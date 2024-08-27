import allure

from pages.main_page import MainPage


class TestLMainPage:

    @allure.title('переход по клику на Конструктор')
    def test_go_to_constructor(self, driver):

        go_to_constructor = MainPage(driver)
        go_to_constructor.go_to_constructor()

        assert go_to_constructor.assemble_the_burger_text().is_displayed()

    @allure.title('переход по клику на Ленту заказов')
    def test_go_to_orders_feed(self, driver):

        go_to_feed = MainPage(driver)
        go_to_feed.go_to_feed()

        assert go_to_feed.get_phrase_lenta_zakazov().is_displayed()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_test_window_with_details_appears(self, driver):

        click_bun_ingredient = MainPage(driver)
        click_bun_ingredient.click_ingredient_and_go_to_window()

        assert click_bun_ingredient.get_text_ingredient_details().is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_click_the_cross_success(self, driver):

        click_bun_ingredient = MainPage(driver)
        click_bun_ingredient.click_ingredient_and_go_to_window()
        click_bun_ingredient.close_details_window()

        assert click_bun_ingredient.check_ingredient_is_clickable_again()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_adding_ingredient_increases_its_counter(self, driver):

        move_ingredient = MainPage(driver)
        move_ingredient.move_bun_to_order()

        assert move_ingredient.check_if_counter_changed().is_displayed()

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_is_able_to_place_an_order_order_placed(self, driver, register_and_authorize):

        place_an_order = MainPage(driver)
        place_an_order.press_place_an_order()

        assert place_an_order.get_order_identifier().is_displayed()
