import allure
from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators


class LkPage(BasePage):

    @allure.step("Кнопка выхода")
    def logout(self):

        self.wait_for_excess_element_2_to_disappear()
        self.wait_for_excess_element_to_disappear()
        self.wait_for_excess_element_1_to_disappear()

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
        logout.click()

    @allure.step("Переход на страницу История заказов")
    def go_to_order_story_page(self):

        self.wait_for_excess_element_to_disappear()
        self.wait_for_excess_element_1_to_disappear()

        self.wait_and_click_element(LkPageLocators.ORDERS_STORY)
