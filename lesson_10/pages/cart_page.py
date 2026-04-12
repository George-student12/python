import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.checkout_info import CheckoutInfo


class CartPage:
    """
    Страница корзины (Cart Page).

    Отображает добавленные товары и позволяет перейти к оформлению заказа.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку 'Checkout'")
    def proceed_to_checkout(self) -> CheckoutInfo:
        """
        Нажимает кнопку Checkout для перехода к вводу данных покупателя.

        Returns:
            CheckoutInfo: Экземпляр страницы ввода информации о покупателе.
        """
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
        return CheckoutInfo(self.driver)
