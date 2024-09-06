from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure
from data import Contents


class ForgotPasswordPage(BasePage):

    @allure.step('Переход на страницу восстановления')
    def check_text_on_forgot_password_page_is_visible(self):

        self.wait_for_excess_element_to_disappear()
        self.wait_and_find_element(ForgotPasswordPageLocators.VOSSTANOVLENIE_PAROLYA)

    @allure.step('Получение фразы Восстановление пароля')
    def return_phrase(self):

        phrase = self.find_element_located(ForgotPasswordPageLocators.VOSSTANOVLENIE_PAROLYA)
        return phrase

    @allure.step('Клик по кнопке восстановления')
    def click_recover_button(self):

        self.wait_and_click_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Ввод Email для восстановления пароля')
    def enter_email(self):

        self.send_keys_to_the_field(ForgotPasswordPageLocators.EMAIL_FIELD, Contents.EMAIL)
