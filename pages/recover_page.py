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

    @allure.title('Кнопка восстановить')
    def get_phrase_for_assert(self):

        recover_password_button_at_recovery_screen = MainPage(self.driver)

        recover_password_button_at_recovery_screen.find_element_located(RecoverPageLocators.RECOVERY_PASSWORD_BUTTON)

       # recover_password_btn_at_recovery_screen = self.find_element_located(RecoverPageLocators.RECOVERY_PASSWORD_BUTTON)
        return recover_password_button_at_recovery_screen
