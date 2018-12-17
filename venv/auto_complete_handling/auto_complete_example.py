from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.southwest.com/")
driver.find_element_by_xpath("//input[@id='air-city-departure']").send_keys("new")
all_suggestions = driver.find_elements_by_xpath("//ul[@id='air-city-departure-menu']/li")
for desired_result in all_suggestions:
    if desired_result.text =="Manchester,gfd NH - MHT":
        desired_result.click()
        break
    else:
        print("Result not found")