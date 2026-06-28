import allure

from pages.main_page import MainPage
from pages.order_list_page import OrderListPage


class TestOrderListPage:

    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_all_order_counter_increases(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        orders_page = OrderListPage(driver)
        
        orders_page.open_order_list_page()
        counter_before = int(orders_page.get_count_for_all_time_value())
        
        main_page.create_order()

        orders_page.open_order_list_page()
        counter_after = int(orders_page.get_count_for_all_time_value())

        assert counter_after >= counter_before + 1, (
            f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"
        )


    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_order_counter_increases(self, driver,  create_user, login_user):
        main_page = MainPage(driver)
        orders_page = OrderListPage(driver)
        
        orders_page.open_order_list_page()
        counter_before = int(orders_page.get_count_today_value())
        
        main_page.create_order()

        orders_page.open_order_list_page()
        counter_after = int(orders_page.get_count_today_value())
        assert counter_after >= counter_before + 1, (
            f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"
        )

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе «В работе»")
    def test_user_order_display(self, driver,  create_user, login_user):
        
        main_page = MainPage(driver)
        orders_page = OrderListPage(driver)
        
        main_page.create_burger()
        
        
        order_number_modal = main_page.get_order_number_modal()

        main_page.wait_for_close_button()    
        main_page.click_on_close_button()
        
        orders_page.open_order_list_page()
        order_numbers_in_progress = orders_page.get_order_number_in_progress()

        assert order_number_modal in order_numbers_in_progress, \
                f'Номер заказа {order_number_modal} не найден в разделе «В работе»'
        
        