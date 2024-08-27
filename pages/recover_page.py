import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.recover_page_locators import RecoverPageLocators
import allure


class RecoverPage(BasePage):

    @allure.title('Переход на страницу восстановления')
    def go_to_recover_page(self):

        time.sleep(2) # БЕЗ ЭТОГО НЕ РАБОТАЕТ

        base_page = BasePage(self.driver) #
        base_page.wait_for_excess_element_to_disappear()

        click_to_lk_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_to_lk_button.click()

        time.sleep(3)

        recover_button = self.find_element_located(RecoverPageLocators.RECOVER_BUTTON)
        recover_button.click()

    @allure.title('Кнопка восстановить')
    def get_phrase_for_assert(self):

        recover_password_btn_at_recovery_screen = self.find_element_located(RecoverPageLocators.RECOVERY_PASSWORD_BUTTON)
        return recover_password_btn_at_recovery_screen
