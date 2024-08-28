import allure
from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators


class LkPage(BasePage):

    @allure.step("Кнопка выхода")
    def logout(self):

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)

        base_page = BasePage(self.driver)
        base_page.extra_wait()
        logout.click()

    @allure.step("Переход на страницу История заказов")
    def go_to_order_story_page(self):

        base_page = BasePage(self.driver)
        base_page.wait_for_excess_element_to_disappear()
        base_page.extra_wait()

        story_button = self.find_element_located(LkPageLocators.ORDERS_STORY)
        story_button.click()

    @allure.step('Метод скролла')
    def scroll_to_last_order(self):

        base_page = BasePage(self.driver)
        base_page.wait_for_last_order()

        base_page.scroll_to_last_order()
