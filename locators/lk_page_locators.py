import allure
from selenium.webdriver.common.by import By

class LkPageLocators:

    ORDER_STORY = (By.XPATH, ".//a[(text()='История заказов')]")

    EXIT_BUTTON = (By.XPATH, ".//button[(text()='Выход')]")   # Кнопка 'Выйти из аккаунта' - расположена в ЛК
