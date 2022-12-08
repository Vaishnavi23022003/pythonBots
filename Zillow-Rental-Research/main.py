from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\VAAB-progm\Chrome driver\chromedriver.exe"

LINK_TO_FORM = "https://forms.gle/aRoekr5dgQWbqdy18"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
}
url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.79725111914063%2C%22east%22%3A-122.06940688085938%2C%22south%22%3A37.513774015169346%2C%22north%22%3A38.03588708503589%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(selector=".list-card-top a")
links=[link.get("href") for link in links]

prices=soup.select(selector=".list-card-price")
prices=[price.getText() for price in prices]

address=soup.select(selector=".list-card-addr")
address=[add.getText() for add in address]
print(soup.prettify())
for i in range(len(links)):

    if links[i][0] != "h":
        links[i] = "https://www.zillow.com" + links[i]
    print(prices[i],address[i],links[i])

    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(LINK_TO_FORM)

    time.sleep(2)

    try:
        ques = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ques.send_keys(address[i])

        ques = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ques.send_keys(prices[i])

        ques = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ques.send_keys(links[i])

        submit = driver.find_element_by_class_name("exportButtonContent")
        submit.click()

    except:

        continue

    driver.quit()
