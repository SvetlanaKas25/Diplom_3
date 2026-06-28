from selenium.webdriver.common.by import By

class LoginPageLocators:    
    
    # Поле «Email» 
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
   
    # Поле «Пароль» 
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']") 
   
    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") 
