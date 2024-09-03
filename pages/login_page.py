from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.register_page import RegisterPage
from helper import generator
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from data import Contents



class LoginPage(BasePage):

    @allure.step('Получение текста Вход на стр авторизации')
    def get_vhod_text_on_login_page(self):

        return self.find_element_located(LoginPageLocators.TEXT_ON_THE_AUTH_SCREEN)

    def click_login_button_on_main_page(self):

        click_enter_an_account = MainPage(self.driver)
        click_enter_an_account.wait_and_click_element(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN)  #

    def fill_email_and_password(self):

        fill_email_password = LoginPage(self.driver)
        fill_email_password.send_keys_to_the_field(LoginPageLocators.EMAIL_FIELD, Contents.EMAIL)
        fill_email_password.send_keys_to_the_field(LoginPageLocators.PASSWORD_FIELD, Contents.PASSWORD)

    def click_login_button_on_login_page(self):

        wait_and_click_login = LoginPage(self.driver)
        wait_and_click_login.wait_and_click_element(LoginPageLocators.LOGIN_BUTTON)






    def login_site_2(self): # удалить после реализации

        login_page = LoginPage(self.driver)

        login_page.wait_and_click_element(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN)
        login_page.send_keys_to_the_field(LoginPageLocators.EMAIL_FIELD, Contents.EMAIL)
        login_page.send_keys_to_the_field(LoginPageLocators.PASSWORD_FIELD, Contents.PASSWORD)
        login_page.wait_and_click_element(LoginPageLocators.LOGIN_BUTTON)



       # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN)).click()
       # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)).send_keys(Contents.EMAIL)
       # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(Contents.PASSWORD)
      #  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()



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

 #   @allure.step('Заполнение логина пароля')
 #   def fill_email_and_password_on_login_page(self, email, password):

 #       put_in_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD_3))   #
 #       put_in_login.send_keys(email)

 #       put_in_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
 #       put_in_password.send_keys(password)


  #  @allure.step('Ожидание и клик по кнопке входа')
  #  def click_login_button(self):

  #      WebDriverWait(self.driver, 20).until(
  #          EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))

  #      self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN).click()