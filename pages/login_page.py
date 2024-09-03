from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from data import Contents


class LoginPage(BasePage):

    @allure.step('Получение текста Вход на стр авторизации')
    def get_vhod_text_on_login_page(self):

        return self.find_element_located(LoginPageLocators.TEXT_ON_THE_AUTH_SCREEN)

    def fill_email_and_password(self):

        self.send_keys_to_the_field(LoginPageLocators.EMAIL_FIELD, Contents.EMAIL)
        self.send_keys_to_the_field(LoginPageLocators.PASSWORD_FIELD, Contents.PASSWORD)

    def click_login_button_on_login_page(self):

        self.wait_and_click_element(LoginPageLocators.LOGIN_BUTTON)
