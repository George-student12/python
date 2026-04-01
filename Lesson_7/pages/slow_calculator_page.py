from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        (self.driver.get("https://bonigarcia.dev/"
                         "selenium-webdriver-java/slow-calculator.html"))
        self.wait = WebDriverWait(self.driver, 50)
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, seconds):
        element = self.wait.until(EC.
                                  visibility_of_element_located
                                  (self._delay_input))
        element.clear()
        element.send_keys(str(seconds))
        return self

    def _click_number(self, number):
        locator = (By.XPATH, f"//span[text()='{number}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _click_operator(self, operator):
        locator = (By.XPATH, f"//span[text()='{operator}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _click_equals(self):
        locator = (By.XPATH, "//span[text()='=']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def calculate(self, num1, num2, operator="+"):
        self._click_number(num1)
        self._click_operator(operator)
        self._click_number(num2)
        self._click_equals()
        return self

    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(self._screen,
                                             str(expected_result))
        )
        return self

    def get_result(self):
        element = (self.wait.until(EC.
                                   visibility_of_element_located
                                   (self._screen)))
        return element.text
