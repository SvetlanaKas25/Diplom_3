from selenium.webdriver.common.by import By

class OrderListPageLocators:    
    
    # Количество заказов 'Выполнено за все время:'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]")

    # Количество заказов 'Выполнено за сегодня:'
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]")

    # Номера заказов "В работе"
    ORDERS_IN_PROGRESS = By.XPATH, "//*[contains(@class, '_orderListReady')]/li[contains(@class, 'digits')]"

