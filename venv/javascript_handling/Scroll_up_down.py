from  selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")

#Scroll Down
# ScrollBy method takes two params - one for pixels in horizontal, and other for pixels vertically
driver.execute_script("window.scrollBy(0,2000);")
time.sleep(3)

#Scroll Up
#Scroll Up works the same as scrolling down, we just have to make the vertical pixel height to Minus
driver.execute_script("window.scrollBy(0, -2000);")
time.sleep(3)

#Scroll somewhere to the middle of the page, or the desired view.
elementInFocus = driver.find_element_by_id("mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", elementInFocus)
driver.execute_script("window.scrollBy(0,-100);")

time.sleep(3)
driver.quit()