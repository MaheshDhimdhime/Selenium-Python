# import necessary classes
from telnetlib import EC

from selenium import webdriver
# create driver object
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")

# A URL that delays loading
driver.get("http://somedomain / url_that_delays_loading")

try:
	# wait 10 seconds before looking for element
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	# else quit
	driver.quit()
