import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from URLs import URLs

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        
    @allure.step("Открываем страницу входа")
    def open_login_page(self):
        return self.open_page(URLs.LOGIN_PAGE)
    
        
    @allure.step("Заполняем поле Email")
    def send_keys_to_element_email(self, email):
        self.send_keys_to_element(LoginPageLocators.EMAIL_FIELD, email)
        return self
    

    @allure.step("Заполняем поле пароль")
    def send_keys_to_element_password(self, password):
        self.send_keys_to_element(LoginPageLocators.PASSWORD_FIELD, password)
        return self
    
        
    @allure.step("Клик по кнопке Войти")
    def click_login_button(self):
        self.click_element_js(LoginPageLocators.LOGIN_BUTTON)
        return self
    
    