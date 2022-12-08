from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\VAAB-progm\Chrome driver\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com")

try:
    log_in=driver.find_element_by_link_text("LOG IN")
except:
    log_in=driver.find_element_by_link_text("Log In")

log_in.click()

time.sleep(1)

try:
    log_in=driver.find_element_by_xpath('//*[@id="q456187828"]/div/div/div[1]/div/div[3]/span/button')
    log_in.click()
except:
    pass

log_in=driver.find_element_by_xpath('//*[@aria-label="Log in with Facebook"]')
print(log_in.text)
log_in.click()

