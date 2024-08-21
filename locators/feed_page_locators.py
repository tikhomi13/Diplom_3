import allure
from selenium.webdriver.common.by import By

class FeedPageLocators:

    FIRST_ORDER_IN_FEED = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')][1]")

    ORDER_WINDOW_GET_NUMBER = (By.XPATH, ".//p[contains(@class, 'text text_type_digits-default mb-10 mt-5')]")

    ORDER_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')][1]")

    OVERALL_COUNTER = (By.XPATH, ".//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]")

    TODAY_COUNTER = (By.XPATH, ".//p[(text()='Выполнено за сегодня:')]/following-sibling::p")

    SOSTAV = (By.XPATH, ".//p[(text()='Cостав')]")

    ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text text_type_digits-default')]") # в работе

    GO_TO_CONSTRUCTOR = (By.XPATH, ".//p[(text()='Конструктор')]/ancestor::a[@href='/']")








    NOMER_ZAKAZA_V_RAZDELE_V_RABOTE = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8" and contains(text(), "7")]')
    # ИЗМЕНИТЬ !!!
    # Либо: - тоже изменить
    ORDER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")

