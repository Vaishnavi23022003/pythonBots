from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path="C:\VAAB-progm\Chrome driver\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_JT=I&geoId=&keywords=python%20developer&location=India")

sign_in=driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

time.sleep(1)

login=driver.find_element_by_id("username")
login.send_keys("vaishnavibadony@gmail.com")

login=driver.find_element_by_id("password")
login.send_keys("internshipthenjob")

login.send_keys(Keys.ENTER)

time.sleep(1)

apply_jobs=driver.find_elements_by_css_selector(".job-card-container__link")

for job in apply_jobs:

    job.click()

    time.sleep(1)

    try:
        apply = driver.find_element_by_class_name("jobs-apply-button")
        apply.click()

        time.sleep(1)

        number = driver.find_element_by_name(
            "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2671770733,32056523,phoneNumber~nationalNumber)")
        number.send_keys("6395895736")

        apply = driver.find_element_by_xpath('//*[@aria-label="Continue to next step"]')
        apply.click()

        time.sleep(1)

        apply = driver.find_element_by_xpath('//*[@aria-label="Continue to next step"]')
        apply.click()

        time.sleep(1)

        form_fill = driver.find_elements_by_css_selector(".jobs-easy-apply-form-section__grouping input")

        for input in form_fill:
            print(1)
            input.send_keys("1")
            input.send_keys(Keys.TAB)

        apply = driver.find_element_by_xpath('//*[@aria-label="Review your application"]')
        apply.click()

        time.sleep(1)

        apply = driver.find_element_by_xpath('//*[@aria-label="Submit application"]')
        apply.click()

    except NoSuchElementException:
        continue

    else:
        print("Successfully applied to a job")
        break