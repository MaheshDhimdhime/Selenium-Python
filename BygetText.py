# Importing necessary modules
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
# WebDriver Chrome
class ChromeDriverManager:
    pass
# Target URL
driver.get("https://platformrc.wyscout.com/app/")

# print(driver.title)

# Printing the whole body text
print(driver.find_element_by_xpath("/html/body").text)

# Closing the driver
driver.close()