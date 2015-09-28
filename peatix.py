from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Firefox()
driver.get("https://peatix.com/signin")
time.sleep(5)
element = driver.find_element_by_xpath('//div[@class = "content-main-box"]')
element2 = element.find_element_by_xpath("//div[@class = 'third-party-box']")
element3 = element2.find_element_by_tag_name("a")
element3.click()
time.sleep(5)
element = driver.find_element_by_name('username')
element.send_keys('sharad.shubham@gmail.com')
time.sleep(1)
element = driver.find_element_by_xpath("//input[@name = 'username']/following::input[1]")
element.send_keys('urwonderful')
element = driver.find_element_by_name('signin_Peatix')
element.click()
driver.get('http://peatix.com/event/create')
time.sleep(10)
element = driver.find_element_by_name('name')
element.send_keys('Tes tEven tFo rTestin g')
element = driver.find_element_by_name('country')
element.send_keys('')

