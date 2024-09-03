import pytest
from selenium import webdriver
from data import URLs
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome'])  # 'firefox',  # ДОБАВИТЬ
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
def authorize(driver):

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.click_login_button_on_main_page()
    login_page.fill_email_and_password()
    login_page.click_login_button_on_login_page()
