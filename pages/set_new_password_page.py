import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.set_new_password_page_locators import SetNewPasswordPageLocators

from pages.base_page import BasePage

from data import Contents

from data import URLs


class SetNewPasswordPage(BasePage):

    def save_new_password_button(self):

        save_password_button = self.find_element_located(SetNewPasswordPageLocators.SAVE_NEW_PASSWORD_BUTTON)

        WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(SetNewPasswordPageLocators.SAVE_NEW_PASSWORD_BUTTON))


       # return save_password_button.text

        return save_password_button

    def set_password(self):

        password_field = self.find_element_located(SetNewPasswordPageLocators.PASSWORD_FIELD)
        password_field.send_keys(Contents.PASSWORD)

    def make_password_visible(self):

        set_password_visible = self.find_element_located(SetNewPasswordPageLocators.SET_PASSWORD_VISIBLE)

        time.sleep(3)

        set_password_visible.click()

        time.sleep(4)




    def check_field_highlighted_if_password_visible(self):

       # active_field = self.find_element_located(SetNewPasswordPageLocators.ACTIVE_FIELD)



        #password = self.find_element_located(SetNewPasswordPageLocators.PASSWORD_ENTERED)

       # WebDriverWait.until(EC.visibility_of_element_located(active_field))

        WebDriverWait.until(EC.visibility_of_element_located(SetNewPasswordPageLocators.ACTIVE_FIELD))





