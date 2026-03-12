from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

waiter = WebDriverWait(driver, 16)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))
images = driver.find_elements(By.TAG_NAME, "img")
third_image_src = images[2].get_attribute("src")

print(f"Атрибут src 3-й картинки: {third_image_src}")

driver.quit()
