import time

import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.lk_page_locators import LkPageLocators


class LkPage(BasePage):

    @allure.step("Кнопка выхода")
    def logout(self):

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
        logout.click()

    @allure.step("Переход на страницу История заказов")
    def go_to_order_story_page(self):

        self.wait_for_excess_element_to_disappear()
        self.wait_and_click_element(LkPageLocators.ORDERS_STORY)

    @allure.step('Метод скролла')
    def scroll_to_last_order(self):

        base_page = BasePage(self.driver)
        base_page.wait_for_last_order()

        base_page.scroll_to_last_order()
