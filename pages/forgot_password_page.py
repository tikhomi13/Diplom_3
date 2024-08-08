import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.lk_page_locators import LkPageLocators
from locators.recover_page_locators import RecoverPageLocators

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import Contents

from pages.set_new_password_page import SetNewPasswordPage


class ForgotPasswordPage(BasePage):

    def return_phrase(self):

        #WebDriverWait()

        phrase = self.find_element_located(ForgotPasswordPageLocators.VOSSTANOVLENIE_PAROLYA)

        return phrase

    def fill_email(self):

        fill_the_field = self.find_element_located(ForgotPasswordPageLocators.EMAIL_FIELD)
        fill_the_field.send_keys(Contents.EMAIL)

    def click_recover_button(self):

        button = self.find_element_located(ForgotPasswordPageLocators.RECOVER_BUTTON)
        button.click()

        return SetNewPasswordPage(self.driver)


