import allure
from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:

    VOSSTANOVLENIE_PAROLYA = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Восстановление пароля')]")

    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")

    RECOVER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Восстановить')]")
