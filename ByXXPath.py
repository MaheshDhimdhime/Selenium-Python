# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")


driver.get("https://platformrc.wyscout.com")

# get element
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div")

# print complete element
print(element)
