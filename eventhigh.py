from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get("https://www.eventshigh.com/login")
time.sleep(5)
element = driver.find_element_by_name('username')
element.send_keys('sharad.shubham@gmail.com')
element = driver.find_element_by_name('password')
element.send_keys('dendidendi')
element = driver.find_element_by_xpath('//input[@name = "password"]/following::button[1]')
element.click()
driver.get("https://www.eventshigh.com/add_event")

