import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import generate_user_create_data
from locators.main_page_locators import  MainPageLocators
from pages.login_page import LoginPage
from API_URLs import APIURL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        drv = webdriver.Chrome()
    
    elif browser == "firefox":
        drv = webdriver.Firefox()
    
    yield drv
    
    drv.quit()


# Создание нового пользователя через API, удаление пользователя после теста
@pytest.fixture(scope="function")
def create_user():
    user_data = generate_user_create_data()
    create_resp = requests.post(url=APIURL.CREATE_USER_ENDPOINT, json=user_data)
    login_pass = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    
    
    yield login_pass
    
    login_resp = requests.post(APIURL.LOGIN_USER_ENDPOINT, json=login_pass)
    login_json = login_resp.json()
    token = login_json.get("accessToken")
    headers = {'Authorization': token}

    requests.delete(APIURL.DELETE_USER_ENDPOINT, headers=headers)
    

# Авторизация пользователя
@pytest.fixture(scope="function")
def login_user(driver, create_user):
    email = create_user["email"]
    password = create_user["password"]
    
    page = LoginPage(driver)
    page.open_login_page()
    
    page.send_keys_to_element_email(email)
    page.send_keys_to_element_password(password)
    page.click_login_button()
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        
    return driver

