import time

import pytest
# import selenium.webdriver.common.devtools.v85.animation
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# from data import WebDriverFactory
from data import URLs

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators

from pages.base_page import BasePage


from data import FakeData

from data import get_sign_up_data




@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':

        chrome_options = webdriver.ChromeOptions()

       # chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--window-size=1014,768')

        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(URLs.BASE_URL)

        WebDriverWait(chrome, 15).until(EC.visibility_of_element_located(
            MainPageLocators.STELLAR_BURGERS_LOGO_CSS))  # а это работает
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
def generator(driver):   # Фикстура генерации данных
    name, email, password = get_sign_up_data()
    return name, email, password




@pytest.fixture

def register_and_authorize(driver, generator):  # рабочая версия кода на 7 авг

    name, email, password = generator

    # ожидание кнопки "Войти в аккаунт"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
    # ожидание обязательно от перекрывающего эл-та ".//div[@class='Modal_modal_overlay__x2ZCr']"

    # проверяем что мешающий элемент не отображается
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAINPAGE).click() # Клик по кнопке "Войти в аккаунт"

    # Ожидание кнопки "Зарегистрироваться" на экране логина
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))
    driver.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN).click() # Клик по кнопке "Зарегистрироваться" на экране логина

    # Ожидание для полей Имя, Email, Пароль
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.NAME_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.NAME_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.NAME_FIELD))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))



    # почему не срабатывает ожидание для поля пароля?

    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    # Ожидание для кнопки "Зарегистрироваться"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON))

    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click() # Клик по кн. "Зарегистрироваться"

    time.sleep(2) # без этой херни лезут ошибки, ожидания не работают. Обратиться к наставнику

    # далее логин

    # Ожидания для полей логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))



    # Заполнение полей экрана Логин
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    # Ожидание для кнопки "Войти" после регистрации

   # WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))
   # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN)) # вызывает ошибки
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))

    driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click() # Клик по кн. "Войти"

#    driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click()

    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER))

   # driver.find_element(*BasePageLocators.GO_TO_ACCOUNT_FROM_HEADER).click()

  #  time.sleep(2)

    yield register_and_authorize




#@pytest.fixture
#def auth_lk(driver):  # Фикстура авторизации

#    driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
##    driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
 #   driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)
 ##   driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
  #  WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))
  #  yield driver


#@pytest.fixture
#def generator(driver):   # Фикстура генерации данных
#    name, email, password = get_sign_up_data()
#    return name, email, password









#@pytest.fixture(scope='function')
#def prepare_user(user):
#    user = UserAPIClient().post_v1_user(data=user)
#    return user


#@pytest.fixture()
#def driver_chrome():

#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('--window-size=1920,1080')
#    chrome = webdriver.Chrome(options=chrome_options)
#    chrome.get(URLs.BASE_URL)
  #  BasePage.find_element_located(*MainPageLocators.STELLAR_BURGERS_LOGO_CSS) - узнать почему AttributeError: 'str' object has no attribute 'driver'
#    WebDriverWait(chrome, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.STELLAR_BURGERS_LOGO_CSS)) # а это работает
#    yield chrome
#    chrome.quit()











#class WebdriverFactory:

 #   @staticmethod
 #   def getWebdriver(browserName):
 #       if browserName == 'firefox':
 #           return webdriver.Firefox()
 #       elif browserName == 'chrome':
 #           return webdriver.Chrome()



  #  firefox_driver = WebDriverFactory.getWebDriver('firefox')
  #  firefox_driver.maximize_window()
  #  yield firefox_driver
  #  firefox_driver.quit()







    # далее данные по регистрации но сначала решить с запуском браузеров


