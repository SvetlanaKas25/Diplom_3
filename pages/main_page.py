import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import  MainPageLocators
from pages.base_page import BasePage
from URLs import URLs

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        return self.open_page(URLs.MAIN_PAGE)

    @allure.step("Клик по кнопке Конструктор")
    def click_constructor_button(self):
        self.click_element_js(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self
    
    @allure.step("Клик по кнопке Лента заказов")
    def click_order_list_button(self):
        self.click_element_js(MainPageLocators.ORDER_LIST_BUTTON)
        return self

    @allure.step("Клик по кнопке выбор булки: Флюоресцентная булка R2-D3")
    def click_on_bun(self):
        self.click_element_js(MainPageLocators.BUN_INGREDIENT)
        return self
    
    @allure.step('Ожидаем появления модального окна с деталями ингредиента')
    def wait_for_modal_to_open(self):
        self.is_element_displayed(MainPageLocators.INGREDIENT_DETAILS_MODAL)
        return self

    @allure.step('Получаем название ингредиента в модальном окне')
    def ingredient_name_in_modal(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_NAME_MODAL)
    
    @allure.step("Клик по кнопке Крестик в модальном окне с деталями ингредиента")
    def click_on_close_button(self):
        self.click_element_js(MainPageLocators.CLOSE_BUTTON)
        return self
    
    @allure.step('Проверяем наличие всплывающего окна с деталями ингредиента')
    def find_modal_window(self):
        return self.is_element_exist(MainPageLocators.MODAL_WINDOW)
    
    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
    
    @allure.step("Перетащить элемент Флюоресцентная булка R2-D3 на элемент Корзина заказа")
    def drag_and_drop_bun(self):
        return self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step("Перетащить элемент Соус Spicy-X на элемент Корзина заказа")
    def drag_and_drop_sauce(self):
        return self.drag_and_drop(MainPageLocators.SAUCE_INGREDIENT, MainPageLocators.ORDER_BASKET)
    
    @allure.step("Клик по кнопке Оформить заказ")
    def click_place_order_button(self):
        self.click_element_js(MainPageLocators.PLACE_ORDER_BUTTON)
        return self
    
    @allure.step("Ожидание кнопки Крестик")
    def wait_for_close_button(self):
        self.wait_for_element(MainPageLocators.CLOSE_BUTTON)
        return self

    @allure.step("Ожидание кнопки Кнопка Оформить заказ")
    def wait_for_order_button(self):
        self.wait_for_element(MainPageLocators.PLACE_ORDER_BUTTON)
        return self

    @allure.step("Собираем бургер и оформляем заказ")
    def create_order(self):
        self.create_burger()
        self.wait_for_close_button()
        self.click_on_close_button()
        return self
    
    @allure.step("Собираем бургер")
    def create_burger(self):
        self.open_main_page()
        self.click_constructor_button()
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce()
        self.click_place_order_button()
        return self
    
    @allure.step('Получаем реальный номер заказа (ждем замены заглушки 9999)')
    def get_order_number_modal(self):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5)
        element = wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_IN_MODAL_WINDOW))
        wait.until(lambda d: (element.text.strip() != "9999"))
        
        return element.text.strip()
    
