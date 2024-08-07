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






