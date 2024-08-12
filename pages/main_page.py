import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data import URLs
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):

    def click_go_to_account_button(self): #click to login

        click_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_button.click()

    def click_personal_account_button_in_header(self):

        time.sleep(1)

        self.driver.find_element(*MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER).click()

    def go_to_constructor(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента

        self.wait_and_find_element(MainPageLocators.GO_TO_CONSTRUCTOR_FROM_HEADER).click()

    def assemble_the_burger_text(self):

        constructor_phrase = self.wait_and_find_element(MainPageLocators.ASSEMBLE_THE_BURGER_TEXT_IN_CONSTRUCTOR)
        return constructor_phrase





