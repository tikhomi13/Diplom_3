import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import URLs
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators
from helper import get_sign_up_data
from pages.base_page import BasePage

@pytest.fixture(params=['firefox', 'chrome'])  #
def driver(request):
    if request.param == 'chrome':

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1014,768')

        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(URLs.BASE_URL)

        yield chrome
        chrome.quit()

    elif request.param == 'firefox':

        firefox_driver = webdriver.Firefox()
        firefox_driver.maximize_window()
        firefox_driver.get(URLs.BASE_URL)

        yield firefox_driver
        firefox_driver.quit()

@pytest.fixture
def generator(driver):
    name, email, password = get_sign_up_data()
    return name, email, password

@pytest.fixture
def register_and_authorize(driver, generator):

    name, email, password = generator

    base_page = BasePage(driver)
    base_page.wait_for_login_button_mainpage()
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAINPAGE).click()

    base_page.wait_for_register_button()
    driver.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()
    base_page.wait_for_fields()

    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    base_page.wait_for_register_button_2()

    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    base_page.wait_for_fields_2()

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    base_page.wait_for_login_button()

    driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click()
    base_page.wait_go_to_account_header()

   # return register_and_authorize
