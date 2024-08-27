from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
import allure


class MainPage(BasePage):

    @allure.step('Клик по кнопке перехода в ЛК')
    def click_go_to_account_button(self):

        click_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_button.click()

    @allure.step('Клик по кнопке перехода в ЛК в хедере')
    def click_personal_account_button_in_header(self):

        time.sleep(2) # БЕЗ ЭТОГО НИЧЕГО НЕ РАБОТАЕТ

        base_page = BasePage(self.driver)
        base_page.wait_go_to_account_header()
        self.driver.find_element(*MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER).click()

    @allure.step('Клик по кнопке перехода в конструктор')
    def go_to_constructor(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1)

        self.wait_and_find_element(MainPageLocators.GO_TO_CONSTRUCTOR_FROM_HEADER).click()

    @allure.step('Текст Соберите бургер')
    def assemble_the_burger_text(self):

        constructor_phrase = self.wait_and_find_element(MainPageLocators.ASSEMBLE_THE_BURGER_TEXT_IN_CONSTRUCTOR)
        return constructor_phrase

    @allure.step('Переход в ленту заказов')
    def go_to_feed(self):

        base_page = BasePage(self.driver)
        base_page.wait_go_to_account_header()

        base_page.wait_feed()

    @allure.step('Получение фразы Лента заказов')
    def get_phrase_lenta_zakazov(self):

        get_text = self.wait_and_find_element(MainPageLocators.LENTA_ZAKAZOV_PHRASE_IN_ORDERS_FEED)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LENTA_ZAKAZOV_PHRASE_IN_ORDERS_FEED))

        return get_text

    @allure.step('Проверка кликабельности кнопки Сделать заказ')
    def lk_clickable(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER))

        return MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER


    @allure.title('Клик по ингредиенту и переход в окно ингредиента')
    def click_ingredient_and_go_to_window(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1)

        click_bun = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        click_bun.click()

    @allure.title('Получение текста Детали ингредиента')
    def get_text_ingredient_details(self):

        get_ingredient_details = self.wait_and_find_element(MainPageLocators.DETALI_INGREDIENTA_PHRASE)
        return get_ingredient_details

    @allure.title('Закрыть окно с деталями - крест')
    def close_details_window(self):

        time.sleep(2)

        krest = self.wait_and_find_element(MainPageLocators.KREST)
        krest.click()

    @allure.title('Проверка кликабельности ингредиента')
    def check_ingredient_is_clickable_again(self):

        bun_ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUN_IN_CONSTRUCTOR))

        return bun_ingredient

    @allure.title('Нажатия кнопки сделать заказ')
    def press_place_an_order(self):

        time.sleep(2)

        base_page = BasePage(self.driver)
        base_page.wait_for_excess_element_to_disappear()

        time.sleep(2)

        base_page.wait_go_to_account_header()
        base_page.wait_for_excess_element_to_disappear() #

        place_and_order = self.wait_and_find_element(MainPageLocators.PLACE_AN_ORDER_BUTTON)
        place_and_order.click()

    @allure.title('Получение идентификатора заказа')
    def get_order_identifier(self):

        id_id = self.wait_and_find_element(MainPageLocators.IDENTIFICATOR_PHRASE)
        return id_id

    @allure.title('Перетаскивание булки')
    def move_bun_to_order(self):

        ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        order = self.wait_and_find_element(MainPageLocators.BASKET)
        drag_and_drop(self.driver, ingredient, order)

    @allure.title('Проверка изменений данных счетчика')
    def check_if_counter_changed(self):

        counter = self.wait_and_find_element(MainPageLocators.COUNTER_INCREASED)
        return counter

    @allure.title('Сделать заказ - добавить ингредиент и кликнуть')
    def place_an_order(self):

        add_ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        order = self.wait_and_find_element(MainPageLocators.BASKET)
        drag_and_drop(self.driver, add_ingredient, order)

        base_page = BasePage(self.driver)
        base_page.wait_for_place_an_order_button()

        place_an_order_button = self.wait_and_find_element(MainPageLocators.PLACE_AN_ORDER_BUTTON)
        place_an_order_button.click()

    @allure.title('Получение и возврат номера нового заказа')
    def get_and_save_new_order_number(self):

        popup_new_order_window = self.wait_and_find_element(MainPageLocators.POPUP_NEW_ORDER_WINDOW)

        base_page = BasePage(self.driver)
        base_page.wait_for_valid_order_number()

        return popup_new_order_window.text

    def sleep(self):

        time.sleep(1)
