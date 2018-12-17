from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
driver.find_element_by_xpath("//input[@value='Log In']")

DestinationFileName = "C:\\Users\\c-deepak.jindal\\pythonscreenshots\\capture.png"

try:
    driver.save_screenshot(DestinationFileName)
    print("Screenshot taken")
except NotADirectoryError:
    print("Directory not found")

