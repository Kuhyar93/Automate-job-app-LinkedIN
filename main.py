import selenium
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

username = "your-email"
password = "your-pass"

#url = "https://www.linkedin.com/jobs/search/?currentJobId=3747974943&f_AL=true&origin=JOB_SEARCH_PAGE_JOB_FILTER"
driver.get("https://www.linkedin.com/")
time.sleep(4)
username_field = driver.find_element(By.XPATH, '//*[@id="session_key"]')
username_field.send_keys(username)
password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]')
password_field.send_keys(password)
time.sleep(4)
singIn_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
singIn_btn.click()
time.sleep(4)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3748731002&distance=25&f_AL=true&geoId=92000000&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER")
time.sleep(4)
easy_apply_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span')
easy_apply_btn.click()
time.sleep(4)
phone_number_field = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3748731002-102992595-phoneNumber-nationalNumber"]')
phone_number_field.send_keys("123456789")
time.sleep(3)
Next_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
Next_btn.click()
time.sleep(3)


