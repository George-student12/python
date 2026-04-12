import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutInfo:
    """
    Страница оформления заказа (Checkout Information и Overview).
    Позволяет заполнить данные покупателя,
    продолжить и проверить итоговую сумму.
    """

    def __init__(self, driver):
        """
        Инициализация страницы оформления.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.total_label = (By.CSS_SELECTOR, "[data-test='total-label']")

    @allure.step(
        "Заполнить данные покупателя: "
        "{first_name} {last_name}, индекс {postal_code}"
    )
    def fill_customer_info(
        self,
        first_name: str = 'Егор',
        last_name: str = 'Морозов',
        postal_code: str = '101010'
    ):
        """
        Заполняет поля First Name, Last Name и Postal Code.
        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.
        Returns:
            CheckoutInfo: Текущий экземпляр страницы.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self):
        """
        Нажимает кнопку Continue для перехода на страницу подтверждения заказа.
        Returns:
            CheckoutInfo: Текущий экземпляр страницы (уже на Overview).
        """
        self.driver.find_element(By.ID, "continue").click()
        return self

    @allure.step("Получить текст итоговой суммы")
    def get_total_text(self) -> str:
        """
        Ожидает появления элемента с итоговой суммой и возвращает его текст.
        Returns:
            str: Текст итоговой суммы (например, "Total: $58.29").
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return element.text.strip()

    @allure.step("Проверить, что итоговая сумма равна '{expected_total}'")
    def verify_total(self, expected_total: str):
        """
        Сравнивает фактическую итоговую сумму с ожидаемой.
        Args:
            expected_total (str): Ожидаемая строка с суммой
                                  (например, "Total: $58.29").
        Returns:
            CheckoutInfo: Текущий экземпляр страницы.
        Raises:
            AssertionError: Если фактическая сумма не совпадает с ожидаемой.
        """
        actual = self.get_total_text()
        assert actual == expected_total, (
            f"Ожидалось '{expected_total}', получено '{actual}'"
        )
        return self
