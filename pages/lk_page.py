import time
import allure
from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.order_story_page import OrderStoryPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LkPage(BasePage):

    @allure.title("Кнопка выхода")
    def logout(self):

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
        time.sleep(4)  # без ожидания ошибка
        logout.click()

        return LoginPage(self.driver)

    @allure.title("Переход на страницу История заказов")
    def go_to_order_story_page(self):

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))
        time.sleep(1) # защита от элемента

        story_button = self.find_element_located(LkPageLocators.ORDERS_STORY)
        story_button.click()

        return OrderStoryPage(self.driver)

    @allure.title('Метод скролла')
    def scroll_to_last_order(self):

        element_to_scroll = self.wait_and_find_element(MainPageLocators.LAST_ORDER)

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MainPageLocators.LAST_ORDER))

        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

        return element_to_scroll
