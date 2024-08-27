from selenium.webdriver.common.by import By


class RegisterPageLocators:

    NAME_FIELD = (By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input[@type='text']")                    # Поле "Имя"

    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")                 # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]//input[@name='Пароль']")                                                   # Поле 'Пароль'

    REGISTER_BUTTON = (By.XPATH, ".//button[contains(@class,'33qZ0') and (text()='Зарегистрироваться')]")                  # Кнопка "Зарегистрироваться" в окне регистрации
