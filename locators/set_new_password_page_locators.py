from selenium.webdriver.common.by import By


class SetNewPasswordPageLocators:

    SAVE_NEW_PASSWORD_BUTTON = (By.XPATH, ".//button[contains(text(), 'Сохранить')]")

    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Введите новый пароль' and @type='password']")

    SHOW_PASSWORD = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[1]")

    NEW_SELECTED_FIELD = (By.XPATH, ".//label[contains(@class, 'input__placeholder-focused')]")

    PASSWORD_ENTERED = (By.XPATH, ".//input[@name='Введите новый пароль' and @value='350018']")

    ACTIVE_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
