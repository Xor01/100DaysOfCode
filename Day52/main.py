# Date Entry Job Automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

service = Service(executable_path="C:\\dev\\chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("")
