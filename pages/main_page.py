import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data import URLs
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

from seletools.actions import drag_and_drop


class MainPage(BasePage):

    def click_go_to_account_button(self): #click to login

        click_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_button.click()

    def click_personal_account_button_in_header(self):

        time.sleep(1)

        self.driver.find_element(*MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER).click()

    def go_to_constructor(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента

        self.wait_and_find_element(MainPageLocators.GO_TO_CONSTRUCTOR_FROM_HEADER).click()

    def assemble_the_burger_text(self):

        constructor_phrase = self.wait_and_find_element(MainPageLocators.ASSEMBLE_THE_BURGER_TEXT_IN_CONSTRUCTOR)
        return constructor_phrase

    def go_to_feed(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента - без ожидания падает фаерфокс

        to_feed = self.wait_and_find_element(MainPageLocators.GO_TO_FEED).click()

    def get_phrase_lenta_zakazov(self):

        get_text = self.wait_and_find_element(MainPageLocators.LENTA_ZAKAZOV_PHRASE_IN_ORDERS_FEED)
        return get_text

    def click_ingredient_and_go_to_window(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента - без ожидания падает фаерфокс

        click_bun = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        click_bun.click()

    def get_text_ingredient_details(self):

        get_ingredient_details = self.wait_and_find_element(MainPageLocators.DETALI_INGREDIENTA_PHRASE)
        return get_ingredient_details

    def close_details_window(self):

        krest = self.wait_and_find_element(MainPageLocators.KREST)
        krest.click()

    def check_ingredient_is_clickable_again(self):

        bun_ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUN_IN_CONSTRUCTOR))
        # без self.driver Будет исключение WebDriverWait.until() missing 1 required positional argument: 'method'

        return bun_ingredient

    def press_place_an_order(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента - без ожидания падает фаерфокс

        place_and_order = self.wait_and_find_element(MainPageLocators.PLACE_AN_ORDER_BUTTON)
        place_and_order.click()

    def get_order_identifier(self):

        id_id = self.wait_and_find_element(MainPageLocators.IDENTIFITATOR)
        return id_id

    def move_bun_to_order(self):

        ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)

        order = self.wait_and_find_element(MainPageLocators.BASKET)

        drag_and_drop(self.driver, ingredient, order)


    def check_if_counter_changed(self):

        counter = self.wait_and_find_element(MainPageLocators.COUNTER_INCREASED)
        return counter











