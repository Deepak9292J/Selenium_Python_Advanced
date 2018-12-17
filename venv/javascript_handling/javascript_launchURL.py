from  selenium import webdriver
import time

driver = webdriver.Chrome()

# To open the brower using javascript, we do it like this-

driver.execute_script("window.location = 'https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1';")