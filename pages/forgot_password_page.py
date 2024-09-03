from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure


class ForgotPasswordPage(BasePage):

    @allure.step('Получение фразы Восстановление пароля')
    def return_phrase(self):

        phrase = self.find_element_located(ForgotPasswordPageLocators.VOSSTANOVLENIE_PAROLYA)
        return phrase

    @allure.step('Клик по кнопке восстановления')
    def click_recover_button(self):

        self.wait_and_click_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
