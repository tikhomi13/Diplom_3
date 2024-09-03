from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOG_IN_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Вход')]")

    REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register' and (text()='Зарегистрироваться')]")

    EMAIL_FIELD = (By.XPATH, ".//div/label[contains(text(), 'Email')]/following-sibling::input[@type='text']")

    EMAIL_FIELD_2 = (By.XPATH, "//input[@name='name']")

    EMAIL_FIELD_3 = (By.XPATH, "//label[text()='Email']/following-sibling::input[1]")

    PASSWORD_FIELD = (By.XPATH, ".//fieldset//input[@name='Пароль']")

    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'button_button_size_medium')]")
