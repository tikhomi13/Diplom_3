import allure
from pages.main_page import MainPage
from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.order_story_page import OrderStoryPage


class TestLkPage:

    @allure.title("Переход в Личный кабинет")
    def test_go_to_personal_account_click_on_personal_account_button_transition_succeeded(self, driver):

        login_page = LoginPage(driver)
        go_to_personal_account = MainPage(driver)
        go_to_personal_account.click_personal_account_button()

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    @allure.title("Переход в раздел История заказов")
    def test_go_to_order_story_click_on_order_story_button_transition_succeeded(self, driver, authorize):

        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_for_excess_element_to_disappear()
        personal_account_page = LkPage(driver)

        personal_account_page.go_to_order_story_page()

        order_story_page = OrderStoryPage(driver)
        order_story_page.return_active_button_go_to_orders()

        assert order_story_page.return_active_button_go_to_orders().is_displayed()


    @allure.title("Выход из аккаунта")
    def test_exit_personal_account_press_exit_button_success(self, driver, authorize):

        main_page = MainPage(driver)
        main_page.click_personal_account_button()

        logout = LkPage(driver)
        main_page.wait_for_excess_element_to_disappear()

        logout.logout()
        login_page = LoginPage(driver)
        login_page.get_vhod_text_on_login_page()

        assert login_page.get_vhod_text_on_login_page().is_displayed()
