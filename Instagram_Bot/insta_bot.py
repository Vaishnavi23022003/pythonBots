from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\VAAB-progm\Chrome driver\chromedriver.exe"


class InstaFollower:
    def __init__(self, id, password, acc):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.id = id
        self.password = password
        self.acc = acc

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        login_name=self.driver.find_element_by_name("username")
        login_name.send_keys(self.id)
        login_pass=self.driver.find_element_by_name("password")
        login_pass.send_keys(self.password)
        login=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        login.click()
        time.sleep(5)
        try:
            login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            login.click()
        except:
            pass

        try:
            login = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            login.click()
        except:
            pass
        time.sleep(2)

    def find_followers(self):
        search=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(self.acc)
        time.sleep(2)
        search=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        search.click()
        time.sleep(3)
        followers=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)

    def follow(self):
        followers=self.driver.find_elements_by_css_selector(".PZuss li button")
        for i in range(10):
            if i>=len(followers):
                break
            followers[i].click()

        self.driver.quit()

