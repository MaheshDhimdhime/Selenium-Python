# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")


driver.get("https://platformrc.wyscout.com")

# get element
element = driver.find_element_by_css_selector("new-login-content")

# print complete element
print(element)
