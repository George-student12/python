from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

sleep(4)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

sleep(2)

flash_element = driver.find_element(By.CSS_SELECTOR, ".flash.success")
flash_text = flash_element.text

print("Текст зелёной плашки:", flash_text)

sleep(2)

driver.quit()
