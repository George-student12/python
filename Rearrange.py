from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "newButtonName")))
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

updated_button_text = driver.find_element(By.ID, "updatingButton").text

print(updated_button_text)

driver.quit()
