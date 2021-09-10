# import webdriver
from selenium import webdriver

# import Alert
from selenium.webdriver.common.alert import Alert

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")


driver.get("https://platformrc.wyscout.com/app/")

# create alert object
alert = Alert(driver)

# get alert text
print(alert.text)

alert.accept()

# accept the alert
alert.accept()
