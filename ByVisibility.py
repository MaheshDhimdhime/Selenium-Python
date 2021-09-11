# importing the modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# using chrome driver

driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# find id of option
x = driver.find_element_by_id('RESULT_RadioButton-9')
drop=Select(x)

# select by visible text
drop.select_by_visible_text("Afternoon")
time.sleep(4)
driver.close()
