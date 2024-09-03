import allure
from pages.base_page import BasePage
from locators.order_story_locators import OrderStoryLocators


class OrderStoryPage(BasePage):

    @allure.title("Метод возвращает активную (выбранную) кнопку История заказов - т.е. переход в этот раздел")
    def return_active_button_go_to_orders(self):

        active_orders_button = self.wait_and_find_element(OrderStoryLocators.ORDERS_STORY_SELECTED)
        return active_orders_button
