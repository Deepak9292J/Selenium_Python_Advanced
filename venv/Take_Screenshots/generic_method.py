from selenium import webdriver
import time

class screenshot():
    def base_method(self):
        from selenium import webdriver
        import time

        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        driver.find_element_by_xpath("//input[@value='Log In']")
        self.reusable_method(driver)

    def reusable_method(self, driver):
        filename = str(round(time.time() * 1000)) + ".png"
        directoryName = "C:\\Users\\c-deepak.jindal\\Capture"
        DestinationFileName = directoryName + filename
        try:
            driver.save_screenshot(DestinationFileName)
            print("Screenshot taken")
        except NotADirectoryError:
            print("Directory not found")

ff = screenshot()
ff.base_method()