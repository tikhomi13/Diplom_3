import allure
from selenium.webdriver.common.by import By

class MainPageLocators:

    LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[(text()='Войти в аккаунт')]")          # Кнопка 'Войти в аккаунт' на главной

    STELLAR_BURGERS_LOGO_CSS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")                                        # Логотип Stellar Burgers (CSS селектор)

    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")                                              # Кнопка 'Оформить заказ'

    EXCESS_ELEMENT = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")  # этого быть не должно





