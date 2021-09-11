# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object

driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")

driver.get("http://www.google.com")

# get element
element = driver.find_element_by_link_text("cheese")

# print complete element
print(element)
