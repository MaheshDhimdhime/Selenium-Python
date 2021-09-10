# Python program to demonstrate
# selenium

# import webdriver
import login as login
from selenium import webdriver

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")

driver.get("http://google.com")

# get element
element = driver.find_element_by_css_selector("input[title=search]")

# print complete element
print(element)
