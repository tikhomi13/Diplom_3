import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import URLs
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators
from data import get_sign_up_data

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'chrome':

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1014,768')

        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(URLs.BASE_URL)

     #   WebDriverWait(chrome, 15).until(EC.visibility_of_element_located(
    #        MainPageLocators.STELLAR_BURGERS_LOGO_CSS))
        yield chrome
        chrome.quit()

    elif request.param == 'firefox':

        firefox_driver = webdriver.Firefox()
        firefox_driver.maximize_window()
        firefox_driver.get(URLs.BASE_URL)

        WebDriverWait(firefox_driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.STELLAR_BURGERS_LOGO_CSS))
        yield firefox_driver
        firefox_driver.quit()

@pytest.fixture
def generator(driver):
    name, email, password = get_sign_up_data()
    return name, email, password

@pytest.fixture

def register_and_authorize(driver, generator):

    name, email, password = generator

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))

    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

    time.sleep(2)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAINPAGE).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))

    driver.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.NAME_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.NAME_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.NAME_FIELD))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))

    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON))

    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    time.sleep(2) # !

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))
    driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER))

    yield register_and_authorize
