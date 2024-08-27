from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step('Получение текста Вход на стр авторизации')
    def get_vhod_text_on_login_page(self):

        return self.find_element_located(LoginPageLocators.TEXT_ON_THE_AUTH_SCREEN)
