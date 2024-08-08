import time

from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_story_locators import OrderStoryLocators

from pages.login_page import LoginPage

from pages.order_story_page import OrderStoryPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class LkPage(BasePage):

    def logout(self):

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
        time.sleep(4)  # без ожидания ошибка
        logout.click()

        return LoginPage(self.driver)

    def go_to_order_story_page(self):    # переход на страницу "История заказов"

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента

        story_button = self.find_element_located(LkPageLocators.ORDER_STORY)
        story_button.click()

        return OrderStoryPage(self.driver)






