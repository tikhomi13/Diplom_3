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

    def switch_to_last_browser_tab(self): # убрать если не нужно

        window_before = self.driver.window_handles
        windows_after = self.driver.switch_to.window(window_before[-1])

        return windows_after





