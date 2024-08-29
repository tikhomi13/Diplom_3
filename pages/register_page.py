from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.register_page_locators import RegisterPageLocators

from helper import generate_user_data
from helper import generator


class RegisterPage(BasePage):

    @allure.step('Ожидание для полей')
    def wait_for_fields_on_register_page(self):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.NAME_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.NAME_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.NAME_FIELD))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))

    @allure.step('Ожидание кнопки Зарегистрироваться в окне регистрации')
    def wait_for_register_button_2(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON))


    @allure.step('Заполнение полей на странице регистрации')
    def fill_registration_fields(self):

        name, email, password = generator()

        self.driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

      #  return name, email, password

        return email, password




    @allure.step('Клик по кнопке Зарегистрироваться')
    def press_register(self):

        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()








