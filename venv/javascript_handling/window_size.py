from  selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://learn.letskodeit.com/p/practice")
#Get the size of the window using JS.

height = driver.execute_script("return window.innerHeight ;")
width = driver.execute_script("return window.innerWidth ;")
print("Before maximising, the height and width are")
print(height)
print(width)

driver.maximize_window()
print("After maximising, the height and width are")
height = driver.execute_script("return window.innerHeight ;")
width = driver.execute_script("return window.innerWidth ;")
print(height)
print(width)
