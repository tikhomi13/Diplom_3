from selenium.webdriver.common.by import By


class RecoverPageLocators:

    RECOVER_BUTTON = (By.XPATH, ".//a[(text()='Восстановить пароль')]")

    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")

    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//button[(text()='Восстановить')]")

    PASSWORD_VISIBILITY = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[1]")
