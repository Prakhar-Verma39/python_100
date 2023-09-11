from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# this is the driver of Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# wait for page to load completely
time.sleep(1)

# click on the sign in tab
driver.find_element(By.XPATH, '//*[@id="frb-form"]/div[1]/button[1]').click()

# search through link text and click it
# driver.fine_element_by_link_text("All portals").click()

# search = driver.find_element_by_name("search")
# search.send_keys("search It!")
# search.send_keys(Keys.ENTER)

count_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(count_articles.text)

driver.quit()