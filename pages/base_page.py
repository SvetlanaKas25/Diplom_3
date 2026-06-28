import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('"Открываем страницу {url}"')
    def open_page(self, url):
        self.driver.get(url)
        return self
    
    # Возвращает текущий URL страницы
    @property
    def url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание элемента {locator} и взаимодействие с ним")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Проверяем наличие элемента на странице по локатору {locator}')
    def is_element_exist(self, locator):
        return bool(self.driver.find_elements(*locator))
    
    @allure.step("Проверить отображение элемента {locator}")
    def is_element_displayed(self, locator):
        try:
            return self.wait_for_element(locator).is_displayed()
        except:
            return False
          
    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Клик по элементу {locator} через JavaScript")
    def click_element_js(self, locator):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return self

    @allure.step("Отправить текст '{keys}' в элемент {locator}")
    def send_keys_to_element(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст из элемента {locator}")
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step("Перетащить элемент {source_locator} на элемент {target_locator} с помощью JS")
    def drag_and_drop(self, source_locator, target_locator):
        wait = WebDriverWait(self.driver, 10)

        source_element = wait.until(EC.element_to_be_clickable(source_locator))
        target_element = wait.until(EC.presence_of_element_located(target_locator))

        ingredient_id = (
            source_element.get_attribute("data-id") or
            source_element.get_attribute("alt") or
            (source_element.text or "").strip() or
            "item-" + source_element.tag_name
        )

        js_script = """
            var source = arguments[0];
            var target = arguments[1];
            var payload = arguments[2];

            if (!source || !target) {
               throw new Error('Source or target element is null');
            }

            var dataTransfer = {
                data: {},
                files: [],
                setData: function(key, value) { this.data[key] = value; },
                getData: function(key) { return this.data[key]; },
                effectAllowed: "all",
                dropEffect: "move"
            };

            dataTransfer.setData("text/plain", payload);

            var evStart = new DragEvent('dragstart', { bubbles: true, cancelable: true, view: window });
            evStart.dataTransfer = dataTransfer;
            source.dispatchEvent(evStart);

            var evOver = new DragEvent('dragover', { bubbles: true, cancelable: true, view: window });
            evOver.dataTransfer = dataTransfer;
            target.dispatchEvent(evOver);

            var evDrop = new DragEvent('drop', { bubbles: true, cancelable: true, view: window });
            evDrop.dataTransfer = dataTransfer;
            target.dispatchEvent(evDrop);

            var evEnd = new DragEvent('dragend', { bubbles: true, cancelable: true, view: window });
            evEnd.dataTransfer = dataTransfer;
            source.dispatchEvent(evEnd);
        """

        self.driver.execute_script(js_script, source_element, target_element, ingredient_id)

        