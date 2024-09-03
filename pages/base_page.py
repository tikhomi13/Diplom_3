import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop


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

    def return_text_of_the_element(self, locator):

        my_text = self.wait_and_find_element(locator)
        return my_text.text

    @allure.step('Ожидание исчезноваения мешающего элемента ')
    def wait_for_excess_element_to_disappear(self):

        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT_1))
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT_2))

    def wait_for_excess_element_2_to_disappear(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT_1))

    def wait_for_the_element_to_be_INvisible(self, locator):

        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    def wait_and_click_element(self, locator):

        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_the_field(self, field, text):

        send_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(field))
        send_text.send_keys(text)

    @allure.step('Прокрутка')
    def scroll_to_last_order(self):

        element_to_scroll = self.wait_and_find_element(MainPageLocators.LAST_ORDER)
        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)
        return element_to_scroll

    def add_ingredient(self):

        add_ingredient = self.wait_and_find_element(MainPageLocators.BUN_IN_CONSTRUCTOR)
        order = self.wait_and_find_element(MainPageLocators.BASKET)
        drag_and_drop(self.driver, add_ingredient, order)

        return add_ingredient, order
