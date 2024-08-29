import time

import pytest
from selenium import webdriver
from data import URLs
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.fixture(params=['chrome'])  # 'firefox',
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
def register_and_authorize(driver):

    main_page = MainPage(driver)
    main_page.wait_for_login_button_mainpage()
    main_page.click_login_button_on_main_page()

    login_page = LoginPage(driver)
    login_page.wait_for_register_button()
    login_page.click_register_button_on_login_screen()

    register_page = RegisterPage(driver)
    register_page.wait_for_fields_on_register_page()

    email, password = register_page.fill_registration_fields()

    register_page.wait_for_register_button_2()
    register_page.press_register()

    login_page.wait_until_log_butt_not_active()


  #  login_page.wait_for_fields_on_login_page()
   # login_page.fill_email_on_login_page(email)
   # login_page.fill_password_on_login_page(password)



    login_page.fill_email_and_password_on_login_page(email, password)

  #  time.sleep(2)

    login_page.click_login_button()
    main_page.wait_go_to_account_header()
