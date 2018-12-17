from  selenium import webdriver
import time

driver = webdriver.Chrome()

# To open the brower using javascript, we do it like this-
driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")

#To enter text into the input box, we do it like-
element = driver.execute_script("return document.getElementById('name');")
element.send_keys("test")
