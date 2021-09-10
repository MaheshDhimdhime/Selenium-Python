# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")

# enter keyword to search
keyword = "wyscout platform"


driver.get("https://platformrc.wyscout.com/app/")

# get element
element = driver.find_element_by_tag_name("head")

# print complete element
print(element)
