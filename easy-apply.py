from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
import time

chromedriver_path = 'C:\\Users\\Utkarsh\\Downloads\\chromedriver_win32'
webdriver = webdriver.Chrome()

constants.init()

webdriver.get('https://www.linkedin.com/')

signin =webdriver.find_element_by_xpath('/html/body/nav/a[3]')
signin.click()

username = WebDriverWait(webdriver, 3).until(
    EC.presence_of_element_located((By.ID, 'username')))

password = WebDriverWait(webdriver, 3).until(
    EC.presence_of_element_located((By.ID, 'password')))

username.send_keys(constants.USERNAME)
password.send_keys(constants.PASSWORD)

signin = WebDriverWait(webdriver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app__container"]/main/div/form/div[3]/button')))

signin.click()


jobs = WebDriverWait(webdriver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="jobs-nav-item"]')))

jobs.click()

searchJobs = WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[starts-with(@id, "jobs-search-box-keyword-id-")]')))

searchBtn = WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[starts-with(@class,"jobs-search-box")]/button')))


searchJobs.send_keys(constants.SEARCHTEXT)
searchBtn.click()

time.sleep(8)

# Apply Filters
linkedInFeatures = WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-controls,"linkedin-features-facet-values")]')))

linkedInFeatures.click()

easyApply = WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//label[contains(@for,"f_LF-f_AL")]')))
easyApply.click()

applyBtn = WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/section[1]/header/div/div/div[3]/div/div/ul/li[2]/form/div/fieldset/div/div/div/button[2]')))

applyBtn.click()
# WebDriverWait(webdriver, 10).until(
#     EC.element_to_be_clickable((By., '//button[contains(@class,"apply-button")]')))
# applyBtn.click()



#webdriver.close())