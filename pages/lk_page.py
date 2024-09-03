import allure
from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators


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
    def wait_and_scroll_to_last_order(self):

        self.scroll_to_last_order()
        self.find_element_located(MainPageLocators.LAST_ORDER)
