import allure
from locators.set_new_password_page_locators import SetNewPasswordPageLocators
from pages.base_page import BasePage


class SetNewPasswordPage(BasePage):

    @allure.title("Кнопка Сохранить на экране восстановления (там где надо ввести новый пароль и кодь из письма")
    def save_new_password_button(self):

        save_password_button = self.find_element_located(SetNewPasswordPageLocators.SAVE_NEW_PASSWORD_BUTTON)
        return save_password_button

    @allure.title("Метод кликает по кнопке видимости пароля")
    def make_password_visible(self):

        self.wait_for_excess_element_2_to_disappear()
        self.wait_for_excess_element_to_disappear()
        self.wait_for_excess_element_1_to_disappear()

        self.wait_and_click_element(SetNewPasswordPageLocators.SHOW_PASSWORD)

    @allure.title("Метод возвращает в ассерт подсвеченное поле ввода пароля")
    def check_field_highlighted_if_password_visible(self):

        field_highlighted = self.driver.find_element(*SetNewPasswordPageLocators.NEW_SELECTED_FIELD)
        return field_highlighted
