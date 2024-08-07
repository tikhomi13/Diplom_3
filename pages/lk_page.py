import time

from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage

class LkPage(BasePage):

    def go_to_order_story(self):

        order_story = self.wait_and_find_element(LkPageLocators.ORDER_STORY)
        order_story.click()
        #returb

  #  def exit_account(self):

   #     click_exit_button = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
    #    click_exit_button.click()

    def logout(self):

        self.find_element_located(LkPageLocators.EXIT_BUTTON, 8)
        logout = self.wait_and_find_element(LkPageLocators.EXIT_BUTTON)
        time.sleep(4)  # без ожидания ошибка
        logout.click()

        return LoginPage(self.driver)




