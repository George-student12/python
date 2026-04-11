from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_info import CheckoutInfo
import allure


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку 'Checkout'")
    def proceed_to_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        return CheckoutInfo(self.driver)
