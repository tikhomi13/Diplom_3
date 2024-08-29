from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOG_IN_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//button[contains(@class, '1O7Bx') and (text()='Войти')][1]")            # Кнопка 'Войти' после нажатия на 'Личный кабинет'

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Вход')]")                        # Текст 'Вход' экрана авторизации (вызывать методом text)

    REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register' and (text()='Зарегистрироваться')]")             # Кнопка 'Зарегистрироваться' на экране логина

    NAME_FIELD = (By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input[@type='text']")                   # Поле "Имя"

    EMAIL_FIELD = (By.XPATH, ".//div/label[contains(text(), 'Email')]/following-sibling::input[@type='text']")            # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset//input[@name='Пароль']")                                                     # Поле 'Пароль'

    LOGIN_BUTTON_ACTIVE = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")
