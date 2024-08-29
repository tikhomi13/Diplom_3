from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.register_page import RegisterPage
from helper import generator
from pages.main_page import MainPage


class LoginPage(BasePage):

    @allure.step('Получение текста Вход на стр авторизации')
    def get_vhod_text_on_login_page(self):

        return self.find_element_located(LoginPageLocators.TEXT_ON_THE_AUTH_SCREEN)

    @allure.step('Ожидание кнопки Зарегистрироваться на экране логина снизу')
    def wait_for_register_button(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))

    def click_register_button_on_login_screen(self):

        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()


    @allure.step('Ожидание для полей логина')
    def wait_for_fields_on_login_page(self):

      #  time.sleep(5)  # БЕЗ ЭТОГО НИЧЕГО НЕ РАБОТАЕТ, поля не грузутся

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))

    @allure.step('Заполнение логина пароля')
    def fill_email_and_password_on_login_page(self, email, password):

    #    return_registration_data = RegisterPage
    #    return_registration_data.fill_registration_fields()     ###







     #   name, email, password = generator()   # вот это надо на что-то поменять

        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)



        time.sleep(6)

    @allure.step('Заполнение поля логина')
    def fill_email_on_login_page(self, email):

        main_page = MainPage(self.driver)
        main_page.wait_for_excess_element_to_disappear()

        email_field = self.wait_and_find_element(LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)


    @allure.step('Заполнение поля пароля')
    def fill_password_on_login_page(self, password):

        password_field = self.wait_and_find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    @allure.step('проверяем что кнопка не активна до нажатия')
    def wait_until_log_butt_not_active(self):

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(LoginPageLocators.LOGIN_BUTTON_ACTIVE))



    @allure.step('Ожидание и клик по кнопке входа')
    def click_login_button(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))

        self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click()

