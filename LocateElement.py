import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
driver.get('https://www.google.com')
# We can use any one of the ele to locate the element

element = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')

ele = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input')

element = driver.find_element_by_name('q')
element = driver.find_element_by_class_name('gLFyf gsfi')
