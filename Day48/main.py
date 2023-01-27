import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = "C:/dev/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

# Getting attributes ids
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
store_elements = [item.get_attribute("id") for item in store]

timeout = time.time() + 5
five_minutes = time.time() + 5*60

while True:

    cookie.click()
    if time.time() > timeout:
        # getting all prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store > div > b")
        item_prices = []

        user_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        # getting all prices individually in a list
        for element in all_prices:
            if element.text != "":
                item_prices.append(int(element.text.split("- ")[1].replace(",", "")))

        for i in range(len(item_prices)):
            randomInt = random.randint(0, 7)
            if user_money >= item_prices[randomInt]:
                all_prices[randomInt].click()
                break

        timeout = time.time() + 5

    # Reach the time limit so exit and give the result
    if timeout >= five_minutes:
        print(f"Your result is : {driver.find_element(By.ID, 'cps').text}")
        driver.close()
        break
