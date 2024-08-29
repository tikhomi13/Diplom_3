import allure
import requests

@allure.title('URL и ручки')
class Endpoints:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    CREATE_USER = f'{BASE_URL}api/auth/register' # POST Создание юзера

    LOGIN_USER = f'{BASE_URL}api/auth/login' # POST Авторизация

    LOGOUT_USER = f'{BASE_URL}api/auth/logout' # POST Выход из системы

    GET_USER_DATA = f'{BASE_URL}api/auth/user' # GET Получить данные польз.

    EDIT_USER_DATA = f'{BASE_URL}api/auth/user' # PATCH Изменение данных польз.

    CREATE_ORDER = f'{BASE_URL}api/orders' # POST Создание заказа

    GET_INGREDIENTS = f'{BASE_URL}api/ingredients' # GET получить данные об ингредиентах

    GET_ALL_ORDERS = f'{BASE_URL}api/orders/all' # GET Получить все заказы

    GET_ORDERS_OF_CURRENT_USER = f'{BASE_URL}api/orders' # GET Получить заказ пользоват.

    UPDATE_TOKEN = f'{BASE_URL}api/auth/token' # POST Обновление токена refreshToken

    DELETE_USER = f'{BASE_URL}api/auth/user' # DELETE Удаление польз.