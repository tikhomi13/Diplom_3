import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.lk_page import LkPage
from locators.lk_page_locators import LkPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.order_story_page import OrderStoryPage
from pages.recover_page import RecoverPage
from locators.order_story_locators import OrderStoryLocators
from data import URLs

from pages.forgot_password_page import ForgotPasswordPage
from pages.set_new_password_page import SetNewPasswordPage


class TestRecoverPage:

    def test_go_to_recover_page_by_recover_button_success_transition(self, driver):

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()

        time.sleep(4)
        recover = ForgotPasswordPage(driver)

        assert recover.return_phrase().text == 'Восстановление пароля'

    def test_enter_email_and_click_recover_button_success_transition(self, driver): # работает

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()

        time.sleep(4)
        recover = ForgotPasswordPage(driver)
        recover.click_recover_button()

        time.sleep(3)

        set_password = SetNewPasswordPage(driver)
        set_password.save_new_password_button()

        assert set_password.save_new_password_button().text == 'Сохранить'

    def test_visibility_of_password_on_after_click_password_is_visible(self, driver): # работает

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()

        time.sleep(4)
        recover = ForgotPasswordPage(driver)
        recover.click_recover_button()

        time.sleep(3)

        set_password = SetNewPasswordPage(driver)

        set_password.set_password()  # ввод пароля

        time.sleep(2)

        set_password.make_password_visible()  # сделать видимым


        #set_password.check_entered_password_visibility() убрать

        time.sleep(2)

      #  driver.wait(500) # прочекать

        # setTimeout(function(){debugger}, 3000)

        set_password.check_field_highlighted_if_password_visible()

        pass

# продолжить тут, завершить тест



