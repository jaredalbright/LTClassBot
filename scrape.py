from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import LT_Login as auth

def go_to_day(driver, endpoint, curr_day):
    d = datetime.timedelta(days=7)
    two_weeks = curr_day + d
    driver.get(f'https://{endpoint}/clubs/ny/sky-manhattan/classes.html?selectedDate={two_weeks}&mode=week&showFilters=true&interest=Pickleball&location=Sky+%28Manhattan%29')

def scrape_classes(driver, curr_day):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'day')))
    days = driver.find_elements(By.CLASS_NAME, "day")
    
    output = {}
    day_count = 0

    for day in days:
        class_arr = []
        classes = day.find_elements(By.CLASS_NAME, "planner-entry")
        for clss in classes:
            class_text = {}
            
            title = clss.find_element(By.CLASS_NAME, 'planner-entry-title')
            link = title.find_element(By.TAG_NAME, 'a').get_attribute('href')
            class_text['link'] = link
            
            text = title.find_element(By.TAG_NAME, 'span').get_attribute('innerHTML')
            class_text['name'] = text
            
            start = clss.find_element(By.CLASS_NAME, 'time-start').get_attribute('innerHTML')
            finish = clss.find_element(By.CLASS_NAME, 'time-end').get_attribute('innerHTML')
            class_text['start'] = start
            class_text['finish'] = finish

            class_arr.append(class_text)
        
        day_text = curr_day + datetime.timedelta(days=day_count)
        output[day_text] = class_arr
        day_count += 1

    return output

def main():
    os.environ['PATH'] += "C:/Chromedriver"

    endpoint = os.getenv("SITE_PREFIX")

    driver  = webdriver.Chrome()

    today = datetime.date.today()

    print(f"Logging into {endpoint}")
    auth.login(driver, endpoint)
    print(f"Grabbing Data")
    go_to_day(driver, endpoint, today)
    print(scrape_classes(driver, today))

if __name__ == "__main__":
    main()

