
class APIURL:
    BASE_API_URL = "https://stellarburgers.education-services.ru"
    
    # Ручка - Создание пользователя
    CREATE_USER_ENDPOINT = f"{BASE_API_URL}/api/auth/register"
    
    # Ручка - Авторизация пользователя
    LOGIN_USER_ENDPOINT = f"{BASE_API_URL}/api/auth/login"

    # Ручка - Удаление пользователя
    DELETE_USER_ENDPOINT = f"{BASE_API_URL}/api/auth/user"

