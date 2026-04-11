from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage
import allure


class Authorisation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get('https://www.saucedemo.com/')
        return self

    @allure.step("Ввести логин '{username}' и пароль")
    def login(self, username='standard_user', password='secret_sauce'):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(By.ID, "login-button").click()

        return InventoryPage(self.driver)
