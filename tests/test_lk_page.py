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

from pages.order_story_page import OrderStoryPage
from locators.order_story_locators import OrderStoryLocators
from data import URLs


class TestLkPage:

    def test_go_to_personal_account_click_on_personal_account_button_transition_succeeded(self, driver): # +

        go_to_personal_account = BasePage(driver)
        go_to_personal_account.click_personal_account_button_in_header()
        login_page = LoginPage(driver)

        assert login_page.get_vhod_text_on_login_page().is_displayed()  # проверка что отображается текст "Вход" после логаута

    def test_go_to_order_story_click_on_order_story_button_transition_succeeded(self, driver, register_and_authorize):

        click = MainPage(driver)
        click.click_personal_account_button_in_header()

        # проверяем что мешающий элемент не отображается
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

        order_story = LkPage(driver)

        order_story.go_to_order_story_page()

        time.sleep(3)

        story = OrderStoryPage(driver)
        story.story_order_window()

    # НЕ ОТОБРАЖАЕТСЯ ОКНО С ЗАКАЗАМИ ПРИ ЗАПУСКЕ АВТОТЕСТА. НИ В ОДНОМ БРАУЗЕРЕ.


        assert story.story_order_window().is_displayed()

        pass


















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

