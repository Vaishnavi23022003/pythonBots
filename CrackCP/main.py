from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

handle = []

chrome_driver_path = "C:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://codeforces.com/")

log_in_1="==========="
pass_1="=============="

log_in_2="==============="
pass_2="====================b"

time.sleep(2)

enter=driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
enter.click()

time.sleep(2)

print('done')

mail=driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
mail.send_keys(log_in_2)

passw=driver.find_element_by_xpath('//*[@id="password"]')
passw.send_keys(pass_2)

login=driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input')
login.click()


for i in handle:
    time.sleep(2)
    name=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[5]/form/input[2]')
    name.send_keys(i)
    name.send_keys(Keys.ENTER)
    try:
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/div[1]/div/a/img').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div[2]/div/h1/img').click()
    except:
        print(i)
        continue



