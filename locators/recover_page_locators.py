from selenium.webdriver.common.by import By

class RecoverPageLocators:

    RECOVER_BUTTON = (By.XPATH, ".//a[(text()='Восстановить пароль')]")             # Кнопка 'Восстановить пароль'

    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")                 # Поле ввода 'Email'

    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//button[(text()='Восстановить')]") # добавить ввод

    PASSWORD_VISIBILITY = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[1]")          # Кнопка видимости пароля в форме восстановления (проверить)

   # NEW_VISIB = (By.XPATH, ".//div[@class='input__placeholder-focused']")







