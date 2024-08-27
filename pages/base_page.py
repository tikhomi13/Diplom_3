import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.title('Поиск элемента на странице')
    def find_element_located(self, locator, time=10):

        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')
        return self.driver.find_element(*locator)

    @allure.title('Ожидание элемента')
    def wait_and_find_element(self, locator):

        WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.title('Открыть странрицу')
    def open_page(self, url):

        self.driver.get(url)

    @allure.title('Получить URL')
    def get_url(self):

        url = self.driver.current_url

        return url

    @allure.title('Обновить страницу')
    def update_page(self):

        self.driver.refresh()

    @allure.title('Переход по вкладкам')
    def switch_to_last_browser_tab(self):

        window_before = self.driver.window_handles
        windows_after = self.driver.switch_to.window(window_before[-1])

        return windows_after

    @allure.title('Ожидание кнопки входа')
    def wait_for_login_button_mainpage(self):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

    @allure.title('Ожидание кнопки Зарегистрироваться на экране логина')
    def wait_for_register_button(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))

    @allure.title('Ожидание для полей')
    def wait_for_fields(self):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.NAME_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.NAME_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.NAME_FIELD))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))

    @allure.title('Ожидание кнопки Зарегистрироваться в окне регистрации')
    def wait_for_register_button_2(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON))

    @allure.title('Ожидание для полей')
    def wait_for_fields_2(self):

        time.sleep(5)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
