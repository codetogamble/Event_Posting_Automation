from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def meraevent(Event_Post):
	driver = webdriver.Firefox()
	driver.get("http://www.meraevents.com/Login")
	time.sleep(5)
	element = driver.find_element_by_name('UserNmae')
	element.send_keys(Event_Post.login_id)
	element = driver.find_element_by_name('UPassword')
	element.send_keys(Event_Post.password)
	element = driver.find_element_by_name('submit')
	element.click()
	driver.get("http://www.meraevents.com/dashboard-account")
	driver.find_element_by_xpath('//a[@href = "dashboard-cEvent?addEvent=1"]').click()
	time.sleep(5)
	driver.find_element_by_xpath('//*[@type = "radio" and @value = "freeevent"]').click()
	element = driver.find_element_by_name('event_title')
	element.send_keys(Event_Post.event_title)
	element = driver.find_element_by_name('event_url')
	element.send_keys(Event_Post.event_title)
	sdate = str(Event_Post.start_date[3:5]) + "-" + str(Event_Post.start_date[0:2]) + "-" + str(Event_Post.start_date[6:])
	driver.execute_script('document.getElementById("datepickerstart").value = "'+ sdate +'"')	
	#element.send_keys('10-10-2015')
	element = driver.find_element_by_id('startHour')
	element.send_keys(Event_Post.start_time[0:2])
	element = driver.find_element_by_id('startMin')
	element.send_keys(Event_Post.start_time[3:5])
	element = driver.find_element_by_id('startAmPm')
	element.send_keys(Event_Post.start_time[5:7].upper())	
	edate = str(Event_Post.end_date[3:5]) + "-" + str(Event_Post.end_date[0:2]) + "-" + str(Event_Post.end_date[6:])
	driver.execute_script('document.getElementById("datepickerstart").value = "'+ edate +'"')
	element = driver.find_element_by_id('endHour')
	element.send_keys(Event_Post.end_time[0:2])
	element = driver.find_element_by_id('endMin')
	element.send_keys(Event_Post.start_time[3:5])
	element = driver.find_element_by_id('endAmPm')
	element.send_keys(Event_Post.start_time[5:7].upper()) 
	driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
	elem = driver.find_element_by_xpath('/html/body') 
	elem.send_keys((Event_Post.event_description).decode('utf-8'))
	driver.switch_to_default_content()
	element = driver.find_element_by_name('Category')
	for x in element.find_elements_by_tag_name('option'):
		if x.text == 'Professional':
			x.click()
			break
	time.sleep(10)
	element = driver.find_element_by_name('SubCategory')
	for x in element.find_elements_by_tag_name('option'):
		if x.text == 'Technology':
			x.click()
			break
	element = driver.find_element_by_name('evtNxtBut')
	element.click()
	element = driver.find_element_by_id('venue')
	element.send_keys(str(Event_Post.venue) + ', ' +str(Event_Post.address_line_1) + ', ' + str(Event_Post.address_line_2)) 
	element = driver.find_element_by_id('profile_country')
	element.send_keys(Event_Post.country)
	element = driver.find_element_by_id('profile_pstate')
	element.send_keys(Event_Post.state)
	element = driver.find_element_by_id('profile_pcity')
	element.send_keys(Event_Post.city)
	
	driver.find_element_by_name('venueNxtBut').click()
	element = driver.find_element_by_name('txtName')
	element.send_keys(Event_Post.event_title)
	driver.find_element_by_xpath('//input[@value = "Save Ticket"]').click()	
	driver.find_element_by_xpath('//input[@id = "tktNxtBut"]').click()
	driver.find_element_by_xpath('//input[@value = "Publish"]').click()
#driver.execute_script('document.getElementById("Category").value = "2"')
#driver.execute_script('document.getElementById("Category").class = "mediuminput11 valid"')
#time.sleep(5)()
#driver.execute_script('document.getElementById("SubCategory").value = "139"')
#driver.execute_script('document.getElementById("SubCategory").class = "mediuminput11"')

