import time

from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_story_locators import OrderStoryLocators


class OrderStoryPage(BasePage):

    def story_order_window(self):

        window = self.find_element_located(OrderStoryLocators.ORDER_HISTORY_WINDOW)
       # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(window))

        return window


    def check_if_order_story_window_is_visible(self):    # проверка видимости окна

        pass
