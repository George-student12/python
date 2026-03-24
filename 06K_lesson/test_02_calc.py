import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()

    delay_input.send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    actual_result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert actual_result == "15", (f"Ожидался результат 15, но получен {actual_result}")
    print("Тест пройден: результат 15 получен после ожидания.")
    driver.quit()