from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.recover_page_locators import RecoverPageLocators
import allure


class RecoverPage(BasePage):

    @allure.title('Переход на страницу восстановления')
    def go_to_recover_page(self):

        main_page = MainPage(self.driver)
        main_page.wait_for_excess_element_to_disappear()

        main_page.wait_and_click_element(MainPageLocators.LOGIN_BUTTON_MAINPAGE)
        main_page.wait_and_click_element(RecoverPageLocators.RECOVER_BUTTON)
