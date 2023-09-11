from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# this is the driver of Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

search = driver.find_element(By.NAME, "fName")
search.send_keys("Fake")
search = driver.find_element(By.NAME, "lName")
search.send_keys("Master")
search = driver.find_element(By.NAME, "email")
search.send_keys("fake.mastery@fakeittillmakeit.com")
driver.find_element(By.CSS_SELECTOR, value=".form-signin button").click()

time.sleep(10)

driver.quit()