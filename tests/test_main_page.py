import allure

from pages.main_page import MainPage
from URLs import URLs


class TestBasicFunctionality:

    @allure.title("Проверка перехода при нажатии на кнопку Конструктор")
    def test_constructor_button_navigate(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_list_button()
        main_page.click_constructor_button()

        expected_url = URLs.MAIN_PAGE
        actual_url = main_page.url
        
        assert expected_url == actual_url, (f"Ожидался URL: {expected_url}, но получен: {actual_url}")

    
    @allure.title("Проверка перехода при нажатии на кнопку Лента заказов")
    def test_order_list_button_navigate(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_list_button()
        
        expected_url = URLs.FEED_PAGE
        actual_url = main_page.url
        
        assert expected_url == actual_url, (f"Ожидался URL: {expected_url}, но получен: {actual_url}")


    @allure.title("Проверка появления всплывающего окна Детали ингридиента при клике на Ингредиент")
    def test_click_ingredient_shows_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_bun()
        main_page.wait_for_modal_to_open()
        actual_name = main_page.ingredient_name_in_modal()
        expected_name = "Флюоресцентная булка R2-D3"
        assert actual_name == expected_name, (f"Ожидался ингредиент: {expected_name}, но получен: {actual_name}")


    @allure.title("Проверка всплывающее окно Детали ингридиента закрывается кликом по крестику")
    def test_modal_window_closes_on_cross_click(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_bun()
        main_page.wait_for_modal_to_open()
        main_page.click_on_close_button()
        assert not main_page.find_modal_window()

    
