# Date Entry Job Automation
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

service = Service(executable_path="C:\\dev\\chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

ZILLOW_URL = f"https://www.zillow.com/NY/rentals/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                       "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br"
}

response = requests.get(url=ZILLOW_URL, headers=HEADER).text
soup = BeautifulSoup(response, "html.parser")

test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")

rent_data = json.loads(rent_data)

all_prices = []
all_addresses = []
all_links = []
for x in rent_data["cat1"]["searchResults"]["listResults"]:
    try:
        all_prices.append(x["price"])
    except KeyError:
        all_prices.append(x["units"][0]["price"])

    all_addresses.append(x["address"])

    all_links.append(x["detailUrl"])
    for i in range(len(all_links)):
        if not all_links[i].startswith("https"):
            all_links[i] = "https://www.zillow.com" + all_links[i]

# ------------------------------------ POSTING TO GOOGLE FORM ---------------------------------------#
for i in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdH5apHl7xI3_wRxm8gzzlZMoJDMOHR-yYAfIAmagnx1hmhPg/viewform"
               "?usp=sf_link")

    sleep(1)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    address.click()
    address.send_keys(all_addresses[i])
    sleep(1)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                          '1]/div/div[1]/input')
    price.click()
    price.send_keys(all_prices[i])
    sleep(1)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                         '1]/div/div[1]/input')
    link.click()
    link.send_keys(all_links[i])
    sleep(1)
    submit_form = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_form.click()

driver.quit()
