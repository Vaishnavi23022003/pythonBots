from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\VAAB-progm\Chrome driver\chromedriver.exe"

EMAIL="killuak722@gmail.com"
PASSWORD="CzZki92i7kjJTqb"

class InternetSpeedTwitterBot():
    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(180)
        self.down=float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up=float(self.driver.find_element_by_class_name("upload-speed").text)
        return(self.down,self.up)

    def tweet_at_provider(self,promissed_up,promissed_down):
        self.driver.close()
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        login=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label')
        login.send_keys(EMAIL)
        password=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
        password.send_keys(PASSWORD)
        login_button=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_button.click()
        time.sleep(5)
        post=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(f"Hello world!! {promissed_down} {promissed_up}")
        post=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        post.click()
