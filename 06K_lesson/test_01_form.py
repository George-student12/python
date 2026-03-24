import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "first-name"))
)
first_name.send_keys("Иван")

last_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "last-name"))
)
last_name.send_keys("Петров")

address = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "address"))
)
address.send_keys("Ленина, 55-3")

city = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "city"))
)
city.send_keys("Москва")

zip_code = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "zip-code"))
)
zip_code.send_keys("")

country = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "country"))
)
country.send_keys("Россия")

# Поле E-mail
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "e-mail"))
)
email.send_keys("test@skypro.com")

phone = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "phone"))
)
phone.send_keys("+7985899998787")

job_position = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "job-position"))
)
job_position.send_keys("Qa")

company = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "company"))
)
company.send_keys("SkyPro")

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
submit_button.click()

test_zip_result = driver.find_element(By.CSS_SELECTOR, "#zip-code")
if "alert-danger" in test_zip_result.get_attribute("class"):
    print("Поле Zip-code заполнено красным цветом")

test_fields_to_check = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone"]
for field_id in test_fields_to_check:
    element = driver.find_element(By.CSS_SELECTOR, f"#{field_id}")
    classes = element.get_attribute("class")
    if "alert-success" in classes:
        print(f" Поле {field_id} заполнено зелёным цветом.")