import allure
from pages.recover_page import RecoverPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.set_new_password_page import SetNewPasswordPage


class TestRecoverPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_go_to_recover_page_by_recover_button_success_transition(self, driver):

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()
        recover = ForgotPasswordPage(driver)

        assert recover.return_phrase().text == 'Восстановление пароля'

    @allure.title("Ввод почты и клик по кнопке Восстановить")
    def test_enter_email_and_click_recover_button_success_transition(self, driver):

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()

        recover = ForgotPasswordPage(driver)
        recover.click_recover_button()

        set_password = SetNewPasswordPage(driver)
        set_password.save_new_password_button()

        assert set_password.save_new_password_button().text == 'Сохранить'

    @allure.title("При нажатии на кнопку 'показать/скрыть пароль' поля ввода делается активным (поле 'Пароль')")
    def test_visibility_of_password_on_after_click_password_is_visible(self, driver):

        go_to_recover_page = RecoverPage(driver)
        go_to_recover_page.go_to_recover_page()

        recover = ForgotPasswordPage(driver)
        recover.click_recover_button()

        set_password = SetNewPasswordPage(driver)
        set_password.make_password_visible()

        assert set_password.check_field_highlighted_if_password_visible().is_displayed()
