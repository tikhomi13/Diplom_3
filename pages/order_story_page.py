import allure
from pages.base_page import BasePage
from locators.order_story_locators import OrderStoryLocators


class OrderStoryPage(BasePage):

    @allure.step('Метод скролла')
    def wait_and_scroll_to_last_order(self):

        self.scroll_to_element(OrderStoryLocators.LAST_ORDER)
        self.find_element_located(OrderStoryLocators.LAST_ORDER)

    @allure.title("Метод возвращает активную (выбранную) кнопку История заказов - т.е. переход в этот раздел")
    def return_active_button_go_to_orders(self):

        active_orders_button = self.wait_and_find_element(OrderStoryLocators.ORDERS_STORY_SELECTED)
        return active_orders_button

    @allure.step('Переход из истории заказов в ленту заказов')
    def go_to_feed_from_order_story(self):

        self.wait_for_excess_element_2_to_disappear()
        self.wait_for_excess_element_to_disappear()
        self.wait_for_excess_element_1_to_disappear()

        self.wait_and_click_element(OrderStoryLocators.GO_TO_FEED_FROM_ORDERS_STORY)
