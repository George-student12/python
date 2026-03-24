import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def test_shopping_total():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    items = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    for item in items:
        add_button = driver.find_element(
            By.CSS_SELECTOR, f"[data-test='add-to-cart-{item}']"
        )
        add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    driver.find_element(By.ID, "first-name").send_keys("Егор")
    driver.find_element(By.ID, "last-name").send_keys("Морозов")
    driver.find_element(By.ID, "postal-code").send_keys("101010")
    driver.find_element(By.ID, "continue").click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text.strip()

    expected_total = "Total: $58.29"
    assert total_text == expected_total, \
        f"Ожидалось {expected_total}, получено {total_text}"

    print("Тест пройден: Стоимость товаров соответствует 58.29$.")
    driver.quit()