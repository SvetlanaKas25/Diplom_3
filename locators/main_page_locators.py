from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[.//p[contains(text(), "Конструктор")]]') 
    
    # Кнопка Лента заказов 
    ORDER_LIST_BUTTON = (By.XPATH, '//a[.//p[contains(text(), "Лента Заказов")]]')

    # Ингредиент "Флюоресцентная булка R2-D3"
    BUN_INGREDIENT = (By.CSS_SELECTOR, 'img[class^="BurgerIngredient_ingredient__image"][alt="Флюоресцентная булка R2-D3"]')
    #BUN_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]') 

    # Ингредиент "Соус Spicy-X"
    SAUCE_INGREDIENT = (By.CSS_SELECTOR, 'img[class^="BurgerIngredient_ingredient__image"][alt="Соус Spicy-X"]')

    # Окно с деталями об ингредиенте
    MODAL_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]" 

    # Модальное окно Детали ингредиента
    INGREDIENT_DETAILS_MODAL = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')  

    # Название ингредиента в Модальном окне
    INGREDIENT_NAME_MODAL = (By.CSS_SELECTOR, 'p.text.text_type_main-medium.mb-8')

    # Кнопка Крестик в Модальном окне
    CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")
    
    # Счетчик ингредиента "Флюоресцентная булка R2-D3"
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  

    # Корзина заказа (куда надо перетянуть булочку)
    ORDER_BASKET = (By.CSS_SELECTOR, ".constructor-element__row img[alt*='низ'] + span.constructor-element__text")
    #ORDER_BASKET = (By.XPATH, "//span[contains(@class, 'constructor-element__text') and text()='Перетяните булочку сюда (низ)']")

    # Кнопка Оформить заказ
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')

    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')

    # Номер заказа во всплывающем окне
    ORDER_NUMBER_IN_MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    