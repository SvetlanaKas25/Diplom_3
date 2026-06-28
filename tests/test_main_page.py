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
