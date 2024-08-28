import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators
from locators.set_new_password_page_locators import SetNewPasswordPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента на странице')
    def find_element_located(self, locator, time=10):

        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')
        return self.driver.find_element(*locator)

    @allure.step('Ожидание элемента')
    def wait_and_find_element(self, locator):

        WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открыть странрицу')
    def open_page(self, url):

        self.driver.get(url)

    @allure.step('Получить URL')
    def get_url(self):

        url = self.driver.current_url
        return url

    @allure.step('Обновить страницу')
    def update_page(self):

        self.driver.refresh()

    @allure.step('Переход по вкладкам')
    def switch_to_last_browser_tab(self):

        window_before = self.driver.window_handles
        windows_after = self.driver.switch_to.window(window_before[-1])
        return windows_after

    @allure.step('Ожидание кнопки входа')
    def wait_for_login_button_mainpage(self):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

    @allure.step('Ожидание кнопки Зарегистрироваться на экране логина')
    def wait_for_register_button(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON_ON_LOGIN_SCREEN))

    @allure.step('Ожидание для полей')
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

    @allure.step('Ожидание кнопки Зарегистрироваться в окне регистрации')
    def wait_for_register_button_2(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON))

    @allure.step('Ожидание для полей')
    def wait_for_fields_2(self):

        time.sleep(5)  # БЕЗ ЭТОГО НИЧЕГО НЕ РАБОТАЕТ, поля не грузутся

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

    @allure.step('Ожидание для кнопки логина')
    def wait_for_login_button(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.LOG_IN_BUTTON_ON_LOGIN_SCREEN))

    @allure.step('Ожидание для кнопки перехода в аккаунт в хедере')
    def wait_go_to_account_header(self):

        WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(MainPageLocators.GO_TO_ACCOUNT_FROM_HEADER))

    @allure.step('Ожидание для последнего заказа')
    def wait_for_last_order(self):

        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(MainPageLocators.LAST_ORDER))

    @allure.step('Ожидание исчезноваения мешающего элемента ')
    def wait_for_excess_element_to_disappear(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

    @allure.step('Ожидание кнопки размещения заказа')
    def wait_for_place_an_order_button(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PLACE_AN_ORDER_BUTTON)) #

    @allure.step('Ожидание Исчезноваения девяток')
    def wait_for_valid_order_number(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.INVALID_ORDER_NUMBER_9999))

    @allure.step('Прокрутка')
    def scroll_to_last_order(self):

        element_to_scroll = self.wait_and_find_element(MainPageLocators.LAST_ORDER)
        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)
        return element_to_scroll

    @allure.step('Ожидание фразы Лента заказов в feeds')
    def wait_for_element_orders_feed(self):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LENTA_ZAKAZOV_PHRASE_IN_ORDERS_FEED))

    @allure.step('Ожидание фразы Соберите бургер')
    def wait_assemble_the_burger_phrase(self):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ASSEMBLE_THE_BURGER_TEXT_IN_CONSTRUCTOR))

    def wait_feed(self):

        self.wait_and_find_element(MainPageLocators.GO_TO_FEED).click()

    def wait_bun_in_constructor(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUN_IN_CONSTRUCTOR))

    def extra_wait(self):

        time.sleep(4)

    def wait_password_button(self):

        WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(SetNewPasswordPageLocators.SAVE_NEW_PASSWORD_BUTTON))

    def wait_show_password_button(self):

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(SetNewPasswordPageLocators.SHOW_PASSWORD))

