from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import secrets
import requests

DRIVER_PATH = '/Users/mouse/src/chromedriver'

response = requests.get('https://app.acuityscheduling.com/schedule.php?action=showCalendar&fulldate=1&owner=19763555&template=weekly')
# response = requests.get('https://app.acuityscheduling.com/schedule.php?action=confirm&ajax=1&owner=19763555&PHPSESSID=k879l9i69vvu9o9q1c9fsge80g&template=weekly')
print(response.__dict__)

# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")


# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://eosfitness.com/schedule-workout-select-club-ca/')

# time.sleep(3)
# WebDriverWait(driver, 20)

#* SELECT INPUT BOXED BY ID:
# select = Select(driver.find_element_by_id('input_74_1'))
# WebDriverWait(driver, 20)
# select by visible text
# select.select_by_visible_text('Los Angeles- Downtown LA/Cesar Chavez')
# time.sleep(3)
# form_element = driver.find_element_by_xpath("html/body/div//form/div[2]")
# l = form_element.get_attribute('innerHTML')

# button = driver.find_element_by_class_name('wpb_wrapper')
# oteh = driver.find_element_by_id("step-pick-appointment")
# print(l)

# select by value 
# select.select_by_value('1')
# inputElement = driver.find_element_by_id("username")
# inputElement.send_keys('purcell3a')

# time.sleep(3)

# inputElement = driver.find_element_by_id("password")
# inputElement.send_keys('L!0j26f13')
#* Now you can simulate hitting ENTER:
# time.sleep(3)

#* or if it is a form you can submit:

# inputElement.submit() 
# getting the button by class name
# button = driver.find_element_by_class_name("select-item-box select-item")
# loginButtonID = 'cta_button_4595896_6b7c46e1-50d8-4c3a-a056-3100a5436ba3'
# button = driver.find_element_by_id(loginButtonID)
# button = driver.find_element_by_id("step-pick-appointment")

# clicking on the button
# button.click()
# print ("###########################  Page URL ########################### ")
# # print(driver.current_url) #to get the current url (can be useful when there are redirections on the website and that you need the final URL)
# print ("###########################  Page Title ########################### ")
# # print(driver.title) #to get the page's title
# print ("###########################  Page Source ########################### ")
# # print(driver.page_source)   #will return and print the full page HTML code in terminal
# print ("###########################  END Scraping ########################### ")
# # driver.quit()
