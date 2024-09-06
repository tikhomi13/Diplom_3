import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    @allure.step('Получение первого заказа в списке')
    def get_first_order_of_feed_list(self):

        self.wait_and_click_element(FeedPageLocators.FIRST_ORDER_IN_FEED)

    @allure.step('Получить номера заказа')
    def check_order_number(self):

        get_order_number = self.wait_and_find_element(FeedPageLocators.ORDER_WINDOW_GET_NUMBER)
        return get_order_number.text


    @allure.step('Возврат окна заказа')
    def return_order_window(self):

        window = self.wait_and_find_element(FeedPageLocators.ORDER_WINDOW)
        return window

    @allure.step('Созданный заказ появляется в разделе В процессе')
    def check_if_created_order_has_appeared_at_in_progress_section(self):

        self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROGRESS)
        v_rabote = self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROGRESS)
        return v_rabote.text

    @allure.step('Общий счетчик заказов')
    def get_overall_counter(self):

        counter = self.wait_and_find_element(FeedPageLocators.OVERALL_COUNTER)
        return counter.text

    @allure.step('Счетчик заказов за день')
    def get_daily_counter(self):

        text = self.return_text_of_the_element(FeedPageLocators.TODAY_COUNTER) #
        return text

    @allure.step('Переход в конструктор')
    def go_to_constructor(self):

        self.wait_and_click_element(FeedPageLocators.GO_TO_CONSTRUCTOR)
