import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.inventory_page import InventoryPage


class Authorisation:
    """
    Страница авторизации (Login Page) интернет-магазина SauceDemo.
    Предоставляет методы для открытия страницы и выполнения входа в систему.
    """

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        Args:
            driver: Экземпляр WebDriver (Firefox, Chrome и т.д.)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открывает URL страницы авторизации в браузере.
        Returns:
            Authorisation: Текущий экземпляр страницы для цепочечных вызовов.
        """
        self.driver.get('https://www.saucedemo.com/')
        return self

    @allure.step("Ввести логин '{username}' и пароль")
    def login(self, username: str = 'standard_user') -> InventoryPage:
        """
        Выполняет вход в систему с указанным логином.
        Пароль загружается из переменной окружения TEST_PASSWORD
        или используется значение по умолчанию.

        Args:
            username (str): Имя пользователя. По умолчанию 'standard_user'.
        Returns:
            InventoryPage: Экземпляр страницы
            каталога товаров после успешного входа.
        """
        password = os.getenv('TEST_PASSWORD', 'secret_sauce')

        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        return InventoryPage(self.driver)
