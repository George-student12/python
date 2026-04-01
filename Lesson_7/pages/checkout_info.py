from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInfo:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.total_label = (By.CSS_SELECTOR, "[data-test='total-label']")

    def fill_customer_info(self, first_name='Егор',
                           last_name='Морозов', postal_code='101010'):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total_text(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        return element.text.strip()

    def verify_total(self, expected_total):
        actual = self.get_total_text()
        assert actual == expected_total, \
            f"Ожидалось {expected_total}, получено {actual}"
        return self
