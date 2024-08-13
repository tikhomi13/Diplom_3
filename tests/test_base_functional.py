import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver



# думаю нужен не отдельный файл а просто удаление созланного юера в файле теста

# тут рассмотреть код из вебинара

# Удаление юзера реализовать здесь

class TestLoginPage: # переименовать

    def test_go_to_lk_both(self, driver): # перенести в метод

        time.sleep(1)  # узнать почему если убрать эту хрень получается ElementClickInterceptedException, хотя у нас стоит ожидание 10 15 сек
# тесты падают через раз

        go_to_main_page = MainPage(driver)
        go_to_main_page.click_go_to_account_button()  # метод клика по кнопке логина

        login_page = LoginPage(driver)

        time.sleep(2)

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    def test_go_to_constructor(self, driver):

        go_to_constructor = MainPage(driver)
        go_to_constructor.go_to_constructor()

        assert go_to_constructor.assemble_the_burger_text().is_displayed()

    def test_go_to_orders_feed(self, driver):

        go_to_feed = MainPage(driver)
        go_to_feed.go_to_feed()

        assert go_to_feed.get_phrase_lenta_zakazov().is_displayed()

    def test_click_ingredient_test_window_with_details_appears(self, driver):

        click_bun_ingredient = MainPage(driver)
        click_bun_ingredient.click_ingredient_and_go_to_window()

        assert click_bun_ingredient.get_text_ingredient_details().is_displayed()
        # так

    def test_close_window_click_the_cross_success(self, driver):

        click_bun_ingredient = MainPage(driver)
        click_bun_ingredient.click_ingredient_and_go_to_window()
        click_bun_ingredient.close_details_window()

        assert click_bun_ingredient.check_ingredient_is_clickable_again()


    def test_adding_ingredient_increases_its_counter(self, driver):  # passed

        move_ingredient = MainPage(driver)

        move_ingredient.move_bun_to_order()

        assert move_ingredient.check_if_counter_changed().is_displayed()

    def test_logged_in_user_is_able_to_place_an_order_order_placed(self, driver, register_and_authorize):

        place_an_order = MainPage(driver)
        place_an_order.press_place_an_order()

        assert place_an_order.get_order_identifier().is_displayed()


        # ПРодолжить тут. Тестировать Раздел «Лента заказов»


















