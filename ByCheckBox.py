# Import selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Using chrome driver
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")


# Web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Selecting raido button
# Select male
driver.find_element_by_xpath(
	'//*[@id="q26"]/table/tbody/tr[1]/td/label').click()


# Selecting check box
# Select sunday
driver.find_element_by_xpath(
	'//*[@id="q15"]/table/tbody/tr[1]/td/label').click()


# Select monday
driver.find_element_by_xpath(
	'//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
