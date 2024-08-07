import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators

from pages.base_page import BasePage

from data import URLs




class LoginPage(BasePage):

    def open_page(self):

        base_page = BasePage

        print(123)

    def get_vhod_text_on_login_page(self):   # слово Вход над формой авторизации

        return self.find_element_located(LoginPageLocators.TEXT_ON_THE_AUTH_SCREEN)





      #  return find_element_located(LkPageLocators.TEXT_ON_THE_AUTH_SCREEN)



