# Date Entry Job Automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get

service = Service(executable_path="C:\\dev\\chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)


class RentRecordingAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def get_rent_data(self):
        get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22"
            "%3A%7B%22west%22%3A-123.66319640109919%2C%22east%22%3A-121.50438292453669%2C%22south%22%3A46"
            ".890610741573575%2C%22north%22%3A48.025206364095844%7D%2C%22mapZoom%22%3A9%2C%22isMapVisible%22%3Atrue"
            "%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C"
            "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22"
            "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A"
            "%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse"
            "%7D%7D%2C%22isListVisible%22%3Atrue%7D")
