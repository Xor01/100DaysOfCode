# Instagram following bot
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from os import environ


class InstagramBot:
    def __init__(self):
        service = Service(executable_path="C:\\dev\\chromedriver.exe")
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.maximize_window()

    def log_in(self, username):
        try:
            self.driver.get("https://instagram.com")
            sleep(5)
            # Username input
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
                environ['username'])

            # Password input

            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
                environ['password'])
            sleep(2)

            # log in button
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

            sleep(10)
            self.driver.get(f"https://instagram.com/{username}/followers/")
            sleep(5)

            users_list = self.driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas')

            for user in users_list:
                sleep(1)
                user.click()
        except Exception:
            print("Sorry Something bad happened...")


bot = InstagramBot()
bot.log_in("friends")
