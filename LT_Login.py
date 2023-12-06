from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from webdriver_manager.chrome import ChromeDriverManager

def login(driver, endpoint):
    driver.get(f'https://{endpoint}/login.html')

    user_link = driver.find_element(By.ID, "account-username")
    user = os.getenv("LT_USER")
    user_link.send_keys(user)

    pass_link = driver.find_element(By.ID, "account-password")
    password = os.getenv("LT_PASS")
    pass_link.send_keys(password)
    driver.find_element(By.ID, "login-btn").click()