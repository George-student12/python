from typing import List
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.cart_page import CartPage


class InventoryPage:
    """
    Страница каталога товаров (Inventory Page) после авторизации.
    Содержит методы для ожидания загрузки, добавления товаров в корзину
    и перехода в корзину.
    """

    def __init__(self, driver):
        """
        Инициализация страницы каталога.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Дождаться отображения списка товаров")
    def wait_for_inventory_loaded(self):
        """
        Ожидает появления контейнера со списком товаров.
        Returns:
            InventoryPage: Текущий экземпляр страницы.
        """
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        return self

    @allure.step("Добавить товары в корзину: {items}")
    def add_items(self, items: List[str]):
        """
        Добавляет указанные товары в корзину по их идентификаторам.
        Args:
            items (List[str]): Список идентификаторов товаров
                               (например, "sauce-labs-backpack").
        Returns:
            InventoryPage: Текущий экземпляр страницы.
        """
        for item in items:
            with allure.step(f"Добавить товар '{item}'"):
                selector = f"[data-test='add-to-cart-{item}']"
                add_button = (By.CSS_SELECTOR, selector)
                self.driver.find_element(*add_button).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Нажимает на иконку корзины и переходит на страницу корзины.
        Returns:
            CartPage: Экземпляр страницы корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)
