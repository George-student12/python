from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
import allure

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Дождаться отображения списка товаров")
    def wait_for_inventory_loaded(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        return self

    @allure.step("Добавить товары в корзину: {items}")
    def add_items(self, items):
        for item in items:
            add_button = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{item}']")
            self.driver.find_element(*add_button).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)
