import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from data import WebDriverFactory
from data import URLs

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


from data import FakeData


#@pytest.fixture(scope='function')
#def prepare_user(user):
#    user = UserAPIClient().post_v1_user(data=user)
#    return user


@pytest.fixture()
def driver_chrome():

    #WebDriverFactory.getWebDriver(browserName='chrome')
    #chrome_options = WebDriverFactory.getWebDriver('chrome')

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--window-size=1920,1080')
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(URLs.BASE_URL)

  #  BasePage.find_element_located(*MainPageLocators.STELLAR_BURGERS_LOGO_CSS) - узнать почему AttributeError: 'str' object has no attribute 'driver'

   # WebDriverWait(chrome, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.STELLAR_BURGERS_LOGO_CSS))

    WebDriverWait(chrome, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.STELLAR_BURGERS_LOGO_CSS)) # а это работает



    yield chrome
    chrome.quit()


@pytest.fixture()
def driver_firefox():

    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()

    firefox_driver.get(URLs.BASE_URL)
    WebDriverWait(firefox_driver, 20).until(expected_conditions.visibility_of_element_located(MainPageLocators.STELLAR_BURGERS_LOGO_CSS))

    yield firefox_driver
    firefox_driver.quit()





  #  firefox_driver = WebDriverFactory.getWebDriver('firefox')
  #  firefox_driver.maximize_window()
  #  yield firefox_driver
  #  firefox_driver.quit()




def email_generator():

    print(2)


