from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager
import LT_Login as auth

def get_res(driver, endpoint, event_id, member_id):
    url = f'https://{endpoint}/account/reservations.html?eventId={event_id}&memberId={member_id}'
    
    driver.get(url) 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-indicator'))).click()
    finish = driver.find_elements(By.CLASS_NAME, 'btn-primary')

    for f in finish:
        innerHTML = str(f.get_attribute('innerHTML'))
        print(innerHTML)
        if "Finish" in innerHTML:
            print("Confirmed Reservation")
            f.click()
            time.sleep(5)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'reservation')))

def main():
    os.environ['PATH'] += "C:/Chromedriver"

    driver  = webdriver.Chrome()

    print(sys.argv)

    endpoint = os.getenv("SITE_PREFIX")

    auth.login(driver, endpoint)
    get_res(driver, endpoint, sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()