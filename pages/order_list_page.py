import allure

from locators.order_list_page_locators import  OrderListPageLocators
from pages.base_page import BasePage
from URLs import URLs

class OrderListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу Лента заказов")
    def open_order_list_page(self):
        return self.open_page(URLs.FEED_PAGE)

    @allure.step('Получаем значение счетчика заказов за все время')
    def get_count_for_all_time_value(self):
        return self.get_text_from_element(OrderListPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME)
    
    @allure.step('Получаем значение счетчика заказов за сегодня')
    def get_count_today_value(self):
        return self.get_text_from_element(OrderListPageLocators.COUNTER_COMPLETED_TODAY)
    
        
    @allure.step('Получаем номер заказа из списка В работе')
    def get_order_number_in_progress(self):
        return self.get_text_from_element(OrderListPageLocators.ORDERS_IN_PROGRESS)
    
    