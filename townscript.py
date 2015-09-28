from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains as ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get("https://www.townscript.com/signin")
time.sleep(5)
element = driver.find_element_by_name('email')
element.send_keys('sharad.shubham@gmail.com')
element = driver.find_element_by_name('password')
element.send_keys('dendidendi')
element = driver.find_element_by_xpath('//form[@name = "signInForm"]')
element2 = element.find_element_by_tag_name('button')
element2.click()
time.sleep(5)
driver.get("https://www.townscript.com/dashboard/#addevent")
time.sleep(30)
#driver.execute_script('document.getElementsByClassName("GI51XYLDLGB").style = "display: block;"')
driver.execute_script('document.getElementsByClassName("GI51XYLDLGB")[0].click();')
time.sleep(2)
element = driver.find_element_by_xpath('//input[@placeholder = "Event Name"]')
element.send_keys('test_event')
element = driver.find_element_by_xpath('//input[@placeholder = "eventcode"]')
element.send_keys('wtf_event_and_how_weereew')
driver.execute_script('document.getElementsByClassName("dashboard-suggestbox")[0].innerHTML = "09:00";')
driver.execute_script('document.getElementsByClassName("dashboard-suggestbox")[1].innerHTML = "22:00";')
driver.execute_script('document.getElementsByClassName("GI51XYLDAIB")[0].textContent= "02-10-2015";')
driver.execute_script('document.getElementsByClassName("GI51XYLDAIB")[1].textContent= "03-10-2015";')

element = driver.find_element_by_xpath('//input[@placeholder = "venue address details"]')
element.send_keys("1427, 6th cross, kodihalli")
element = driver.find_element_by_xpath('//div[@class = "basic_field_half_panel_style basic_field_panel_style"]')
element2 = element.find_element_by_xpath('.//input[@class = "dashboard-suggestbox"]')

element2.send_keys("Bangalore")
#driver.execute_script('document.getElementsByClassName("dashboard-suggestbox")[2].innerHTML = "Bangalore";')
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
elem = driver.find_element_by_xpath('/html/body') 
elem.send_keys("test test test test test test test test test test test test test test test test test test test test test test ")
driver.switch_to_default_content()
driver.execute_script('document.getElementsByClassName("GI51XYLDLFB")[0].click();')
time.sleep(10)
element = driver.find_element_by_xpath('//input[@placeholder = "Eg. Early Bird"]')
element.send_keys("Test Tickets")
element = driver.find_element_by_xpath('//input[@placeholder = "Eg. 100"]')
element.send_keys("100")
driver.execute_script('document.getElementsByClassName("GI51XYLDAFB")[0].click();')
time.sleep(5)
driver.execute_script('document.getElementsByClassName("GI51XYLDEEB")[0].click();')

