import allure

from selenium.webdriver.common.by import By

class BasePageLocators:

    GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//p[(text()='Конструктор')]/ancestor::a[@href='/']")                     # Кнопка перехода в 'Конструктор' в хедере













