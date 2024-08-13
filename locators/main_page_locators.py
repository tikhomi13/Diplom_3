import allure
from selenium.webdriver.common.by import By

class MainPageLocators:

    LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[(text()='Войти в аккаунт')]")          # Кнопка 'Войти в аккаунт' на главной

    STELLAR_BURGERS_LOGO_CSS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")                                        # Логотип Stellar Burgers (CSS селектор)

    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")                                              # Кнопка 'Оформить заказ'

    EXCESS_ELEMENT = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")  # этого быть не должно

    GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//p[(text()='Конструктор')]/ancestor::a[@href='/']")       # Кнопка перехода в 'Конструктор' в хедере

    GO_TO_ACCOUNT_FROM_HEADER = (By.XPATH, "//p[(text()='Личный Кабинет')]/ancestor::a[@href='/account']")       # Кнопка 'Личный кабинет' в хедере

    ASSEMBLE_THE_BURGER_TEXT_IN_CONSTRUCTOR = (By.XPATH, ".//h1[(text()='Соберите бургер')]")               #  Текст "Соберите бургер" в конструкторе

    GO_TO_FEED = (By.XPATH, ".//a[@href='/feed']")

    LENTA_ZAKAZOV_PHRASE_IN_ORDERS_FEED = (By.XPATH, ".//h1[(text()='Лента заказов')]")

    BUN_IN_CONSTRUCTOR = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")

    DETALI_INGREDIENTA_PHRASE = (By.XPATH, ".//h2[(text()='Детали ингредиента')]")

    KREST = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//div/button[contains(@class, 'close')]")

    IDENTIFITATOR = (By.XPATH, ".//p[(text()='идентификатор заказа')]")

    BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    COUNTER_INCREASED = (By.XPATH, ".//p[(text()='1976')]")






















