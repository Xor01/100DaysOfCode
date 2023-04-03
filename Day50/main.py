from selenium import webdriver
from os import getenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

username = getenv("username")
password = getenv("password")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.UP = 20
        self.DOWN = 100
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        service = Service(executable_path="C:\\dev\\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

    def get_internet_speed(self):
        try:
            self.driver.get("https://www.speedtest.net/")
            sleep(3)

            # start button
            self.driver.find_element(By.CSS_SELECTOR, '.start-button a').click()
            print("Checking your internet speed...")
            sleep(45)

            download_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                      '#container > div > div.main-content > div > div > div > '
                                                      'div.pure-u-custom-speedtest > div.speedtest-container.main-row >'
                                                      'div.main-view > div > div.result-area.result-area-test > div > '
                                                      'div >'
                                                      'div.result-container-speed.result-container-speed-active > '
                                                      'div.result-container-data > '
                                                      'div.result-item-container.result-item-container-align-center > '
                                                      'div >'
                                                      'div.result-data.u-align-left > span').text

            upload_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                    '#container > div > div.main-content > div > div > div > '
                                                    'div.pure-u-custom-speedtest > div.speedtest-container.main-row > '
                                                    'div.main-view > div > div.result-area.result-area-test > div > '
                                                    'div > div.result-container-speed.result-container-speed-active > '
                                                    'div.result-container-data > '
                                                    'div.result-item-container.result-item-container-align-left > div '
                                                    '> div.result-data.u-align-left > span').text
            print(f"Download speed: {download_speed}, Upload Speed: {upload_speed}")
            if (int(download_speed) < self.DOWN) or (int(upload_speed) < self.UP):
                self.tweet_at_provider(f"why my internet speed is not as our contract"
                                       f" ? {download_speed}down, {upload_speed}up not {self.DOWN} down, {self.UP} up")
        except Exception:
            print("Sorry we could not get your internet speed")

    def tweet_at_provider(self, message):
        try:
            self.driver.get("https://twitter.com/i/flow/login")

            sleep(2)
            # send username
            self.driver.find_element(By.CSS_SELECTOR, "input").send_keys(username)

            sleep(3)
            # click next
            self.driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > '
                                                      'div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r'
                                                      '-1xcajam.r-ipm5af.r'
                                                      '-g6jmlv > '
                                                      'div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r'
                                                      '-1pjcn9w.r-1279nm1.r'
                                                      '-htvplk.r-1udh08x > div > div > '
                                                      'div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > '
                                                      'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r'
                                                      '-13qz1uu > div > div >'
                                                      'div > div:nth-child(6)').click()

            sleep(3)
            # send password
            self.driver.switch_to.active_element.send_keys(password)

            sleep(3)
            # click next
            self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > "
                                                      "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r"
                                                      "-1xcajam.r-ipm5af.r"
                                                      "-g6jmlv > "
                                                      "div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r"
                                                      "-1pjcn9w.r-1279nm1.r"
                                                      "-htvplk.r-1udh08x > div > div > "
                                                      "div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > "
                                                      "div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r"
                                                      "-13qz1uu >"
                                                      "div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div "
                                                      "> div").click()
            sleep(5)
            self.driver.get("https://twitter.com/compose/tweet")
            sleep(3)
            self.driver.switch_to.active_element.send_keys(message)
            sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                               '2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div['
                                               '3]/div/div/div[2]/div['
                                               '4]').click()
            print("-------- Your Complaint has been sent -----------")
            sleep(5)
            self.driver.quit()

        except Exception:
            print("----- Something wrong happened we could not send your complaint -----")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
