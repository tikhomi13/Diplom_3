import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators

from data import URLs

import pytest
from selenium import webdriver



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_located(self, locator, time=10):

        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')
        return self.driver.find_element(*locator)

    def wait_and_find_element(self, locator):

        WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):

        self.driver.get(url)

    def get_url(self):

        url = self.driver.current_url

        return url

    def update_page(self):

        self.driver.refresh()




    @allure.step("Клик по кнопке Самокат в хедере слева")
    def click_samokat_button(self):

       # samokat_button = self.wait_and_find_element(BasePageLocators.SAMOKAT_BUTTON)
        samokat_button = self.find_element_located(BasePageLocators.SAMOKAT_BUTTON)
        samokat_button.click()

        # добавить общие кнопки



    def switch_to_last_browser_tab(self): # убрать если не нужно

        window_before = self.driver.window_handles
        windows_after = self.driver.switch_to.window(window_before[-1])

        return windows_after

    def click_personal_account_button_in_header(self):
       # WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable(BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER))

        time.sleep(1)

       # personal_account_button = self.driver.find_element(BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER)

        self.driver.find_element(*BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER).click()

    #personal_account_button = self.wait_and_find_element(BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER)

      #  personal_account_button.click()



