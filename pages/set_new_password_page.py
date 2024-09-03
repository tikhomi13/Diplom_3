import allure
from locators.set_new_password_page_locators import SetNewPasswordPageLocators
from pages.base_page import BasePage
from data import Contents


class SetNewPasswordPage(BasePage):

    @allure.title("Кнопка Сохранить на экране восстановления (там где надо ввести новый пароль и кодь из письма")
    def save_new_password_button(self):

        save_password_button = self.find_element_located(SetNewPasswordPageLocators.SAVE_NEW_PASSWORD_BUTTON)
        base_page = BasePage(self.driver)
        base_page.wait_password_button()

        return save_password_button

    @allure.title('Заполнить новый пароль')
    def set_password(self):

        password_field = self.find_element_located(SetNewPasswordPageLocators.PASSWORD_FIELD)
        password_field.send_keys(Contents.PASSWORD)

    @allure.title("Метод кликает по кнопке видимости пароля")
    def make_password_visible(self):

        self.wait_and_click_element(SetNewPasswordPageLocators.SHOW_PASSWORD)

       # base_page = BasePage(self.driver)
       # base_page.wait_show_password_button()
       ## base_page.extra_wait()
       # self.find_element_located(SetNewPasswordPageLocators.SHOW_PASSWORD).click()

    @allure.title("Метод возвращает в ассерт подсвеченное поле ввода пароля")
    def check_field_highlighted_if_password_visible(self):

        field_highlighted = self.driver.find_element(*SetNewPasswordPageLocators.NEW_SELECTED_FIELD)
        return field_highlighted
