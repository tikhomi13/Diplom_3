from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import Contents
from pages.set_new_password_page import SetNewPasswordPage
import allure

class ForgotPasswordPage(BasePage):

    @allure.title('Получение фразы Восстановление пароля')
    def return_phrase(self):

        phrase = self.find_element_located(ForgotPasswordPageLocators.VOSSTANOVLENIE_PAROLYA)

        return phrase

    @allure.title('Заполнение эл.почты')
    def fill_email(self):

        fill_the_field = self.find_element_located(ForgotPasswordPageLocators.EMAIL_FIELD)
        fill_the_field.send_keys(Contents.EMAIL)

    @allure.title('Клик по кнопке восстановления')
    def click_recover_button(self):

        button = self.find_element_located(ForgotPasswordPageLocators.RECOVER_BUTTON)
        button.click()

        return SetNewPasswordPage(self.driver)
