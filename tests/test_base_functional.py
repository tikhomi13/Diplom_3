import time
from pages.main_page import MainPage
from pages.login_page import LoginPage


# думаю нужен не отдельный файл а просто удаление созланного юера в файле теста

# тут рассмотреть код из вебинара

# Удаление юзера реализовать здесь

class TestLoginPage: # переименовать

    def test_go_to_lk_both(self, driver): # перенести в метод

        time.sleep(1)  # узнать почему если убрать эту хрень получается ElementClickInterceptedException, хотя у нас стоит ожидание 10 15 сек
# тесты падают через раз

        go_to_main_page = MainPage(driver)
        go_to_main_page.click_go_to_account_button()  # метод клика по кнопке логина

        login_page = LoginPage(driver)

        time.sleep(2)

        assert login_page.get_vhod_text_on_login_page().is_displayed()

    def test_go_to_constructor(self, driver):

        go_to_constructor = MainPage(driver)
        go_to_constructor.go_to_constructor()

        assert go_to_constructor.assemble_the_burger_text().is_displayed()


        # Продолжить тут. Далее - метод перехода в ленту заказов
