from selenium.webdriver.common.by import By



class SetNewPasswordPageLocators:

    SAVE_NEW_PASSWORD_BUTTON = (By.XPATH, ".//button[contains(text(), 'Сохранить')]")

    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Введите новый пароль' and @type='password']")

    SET_PASSWORD_VISIBLE = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[1]")

    PASSWORD_ENTERED = (By.XPATH, ".//input[@name='Введите новый пароль' and @value='350018']")

    ACTIVE_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")

    # с этим проблема


