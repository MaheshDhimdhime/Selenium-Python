
# import webdriver
from selenium import webdriver

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")

driver.get("https://platformrc.wyscout.com/app/")

# get element
element = driver.find_element_by_id("gears-ui")

# print complete element
print(element)
