import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_story_locators import OrderStoryLocators
from locators.feed_page_locators import FeedPageLocators

from pages.main_page import MainPage

from pages.login_page import LoginPage

from pages.order_story_page import OrderStoryPage


class FeedPage(BasePage):

    def get_first_order_of_feed_list(self):

        open_order_cart = self.wait_and_find_element(FeedPageLocators.FIRST_ORDER_IN_FEED)

        open_order_cart.click()

    def check_order_number(self):

        get_order_number = self.wait_and_find_element(FeedPageLocators.ORDER_WINDOW_GET_NUMBER)

        print(get_order_number)
        print(get_order_number.text)

        return get_order_number.text

    def return_order_window(self):

        window = self.wait_and_find_element(FeedPageLocators.ORDER_WINDOW)
        return window


    def check_if_created_order_has_appeared_at_in_progress_section(self):

        self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROGRESS)

        v_rabote = self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROGRESS)

        return v_rabote.text

    def get_overall_counter(self):

        counter = self.wait_and_find_element(FeedPageLocators.OVERALL_COUNTER)

        return counter.text

    def get_daily_counter(self):

        counter = self.wait_and_find_element(FeedPageLocators.TODAY_COUNTER)

        return counter.text

    def go_to_constructor(self):

        constructor = self.wait_and_find_element(FeedPageLocators.GO_TO_CONSTRUCTOR)
        constructor.click()

      #  return MainPage(self.driver)



