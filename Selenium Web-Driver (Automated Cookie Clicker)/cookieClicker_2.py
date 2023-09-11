from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a WebDriver instance
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#prompt #langSelect-EN").click()

timeout = time.time() + 5
five_min = time.time() + 60 * 5

def safe_click(element_locator):
    retries = 3
    while retries > 0:
        try:
            hand = driver.find_element(*element_locator)
            hand.click()
            break
        except StaleElementReferenceException:
            retries -= 1

def safe_text(element_locator):
    retries = 3
    while retries > 0:
        try:
            element = driver.find_element(*element_locator)
            return element.text
        except StaleElementReferenceException:
            retries -= 1
    return None

def upgrade_text(element_locator):
    retries = 3
    while retries > 0:
        try:
            element = driver.find_element(*element_locator)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            tooltip_element = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#tooltip .price'))
            )
            return tooltip_element.text
        except StaleElementReferenceException:
            retries -= 1
    return None

while time.time() < five_min:
    safe_click((By.ID, "bigCookie"))
    if time.time() > timeout:
        money = safe_text((By.ID, "cookies"))
        if money is not None:
            money = money.split(" ")[0].replace(",", "")
        else:
            break

        money_in_integer = int(money)
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
        upgrades_prices = [int(upgrade_text((By.ID, f"upgrade{i}")).replace(",", "")) for i in range(len(upgrades))]

        if len(upgrades_prices) > 0:
            max_upgrade_price = max(upgrades_prices)
            max_upgrade_price_index = upgrades_prices.index(max_upgrade_price)
            hand1 = driver.find_element(By.ID, f"upgrade{max_upgrade_price_index}")
            driver.execute_script("arguments[0].click();", hand1)

        products = driver.find_elements(By.CSS_SELECTOR, "#products .enabled .price")

        if len(products) > 0:
            products_prices = [int(product.text.replace(",", "")) for product in products]
            max_product_price = max(products_prices)
            max_product_price_index = products_prices.index(max_product_price)

            if max_product_price < money_in_integer:
                hand2 = driver.find_element(By.ID, f"product{max_product_price_index}")
                driver.execute_script("arguments[0].click();", hand2)

        timeout = time.time() + 5

time.sleep(1)
perSec = safe_text((By.ID, "cookiesPerSecond"))
print(perSec) if perSec is not None else print("Unable to retrieve text.")
driver.quit()
