from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# this is the driver of Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/events/")

# driver.find_element(By.CLASS_NAME, value="")
# driver.find_element(By.NAME, value="")
# driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# driver.find_element(By.XPATH, value='see through inspect')

events_names = driver.find_elements(By.CSS_SELECTOR, value="ul.list-recent-events h3.event-title")
eventS_times = driver.find_elements(By.CSS_SELECTOR, value="ul.list-recent-events time")
events = {}

for i in range(len(events_names)):
    events[i] = {
        "time": eventS_times[i].get_attribute("datetime").split("T")[0],
        "name": events_names[i].text,
    }


print(events)

# closes the present tab
# driver.close()

# quit the entire browser
driver.quit()

