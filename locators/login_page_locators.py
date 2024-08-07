import allure
from selenium.webdriver.common.by import By

class LkPageLocators:

    LOG_IN_BUTTON_LK_SCREEN = (By.XPATH, ".//button[contains(@class, '1O7Bx') and (text()='Войти')][1]")                  # Кнопка 'Войти' после нажатия на 'Личный кабинет'

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Вход')]")                        # Текст 'Вход' экрана авторизации (вызывать методом text)



