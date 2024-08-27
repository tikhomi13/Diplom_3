import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.recover_page_locators import RecoverPageLocators
import allure


class RecoverPage(BasePage):

    @allure.title('Переход на страниу восстановления')
    def go_to_recover_page(self):

        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT))

        click_to_lk_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_to_lk_button.click()

        time.sleep(2)

        recover_button = self.find_element_located(RecoverPageLocators.RECOVER_BUTTON)
        recover_button.click()

        return RecoverPage(self.driver)

    @allure.title('Кнопка восстановить')
    def get_phrase_for_assert(self):

        recover_password_btn_at_recovery_screen = self.find_element_located(RecoverPageLocators.RECOVERY_PASSWORD_BUTTON)
        return recover_password_btn_at_recovery_screen
