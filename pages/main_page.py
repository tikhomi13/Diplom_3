import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLs
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_go_to_account_button(self):

        click_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_button.click()




