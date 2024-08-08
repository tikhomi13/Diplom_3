import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.lk_page_locators import LkPageLocators
from locators.recover_page_locators import RecoverPageLocators


class RecoverPage(BasePage):

    def go_to_recover_page(self):

        time.sleep(2)
        # проверили что нет мешающего элемента (не помогает поэтому оставили ожидание)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.EXCESS_ELEMENT)) # не помогает


        click_to_lk_button = self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAINPAGE, time=20)
        click_to_lk_button.click()

        time.sleep(2)

        recover_button = self.find_element_located(RecoverPageLocators.RECOVER_BUTTON)
        recover_button.click()

        return RecoverPage(self.driver)

    def get_phrase_for_assert(self):

        recover_password_btn_at_recovery_screen = self.find_element_located(RecoverPageLocators.RECOVERY_PASSWORD_BUTTON)

        return recover_password_btn_at_recovery_screen




     #   go_to_personal_account = BasePage(driver)
     #   go_to_personal_account.click_personal_account_button_in_header()
