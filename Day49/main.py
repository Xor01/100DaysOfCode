from selenium import webdriver
from os import getenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path="C://dev//chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
email = getenv("EMAIL")
password = getenv("PASS")

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3468021938&f_LF=f_AL&geoId=100459316&keywords=programming+intern&location=Saudi+Arabia&refresh=true")

# sign in button in the jobs page
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()
driver.implicitly_wait(3)

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)


# for sign in
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
driver.implicitly_wait(3)
# jobs_list = driver.find_element(By.CSS_SELECTOR, ".job-card-container")
# jobs_list.click()

driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button').click()
