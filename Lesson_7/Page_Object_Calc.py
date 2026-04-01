from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.slow_calculator_page import SlowCalculatorPage


def test_slow_calculator():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    try:
        calculator = SlowCalculatorPage(driver)
        calculator.set_delay(45).calculate(7, 8).wait_for_result(15)
        actual_result = calculator.get_result()
        assert actual_result == "15", \
            f"Ожидался результат 15, но получен {actual_result}"
        print("Тест пройден: результат 15 получен после ожидания.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
