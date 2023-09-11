from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# this is the driver of Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, value="#prompt #langSelect-EN").click()

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes


# Handle Stale Elements in a More Robust Way
def safe_click(element_locator):
    retries = 3
    while retries > 0:
        try:
            hand = driver.find_element(*element_locator)
            hand.click()
            break
        except StaleElementReferenceException:
            # Handle the exception by decrementing retries or other actions
            retries -= 1


# Handle Stale Elements in a More Robust Way
def safe_text(element_locator):
    retries = 3
    while retries > 0:
        try:
            element = driver.find_element(*element_locator)
            return element.text
        except StaleElementReferenceException:
            # Handle the exception by decrementing retries or other actions
            retries -= 1
    return None  # Return None if retries are exhausted


def upgrade_text(element_locator):
    retries = 3
    while retries > 0:
        try:
            element = driver.find_element(*element_locator)

            # Create an ActionChains object
            actions = ActionChains(driver)

            # Hover over the element
            actions.move_to_element(element).perform()

            # Retrieve the value in two steps:

            #  Wait for the tooltip to appear and then take the value
            tooltip_element = WebDriverWait(driver, 3).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, '#tooltip .price'))
            )

            return tooltip_element.text
        except StaleElementReferenceException:
            # Handle the exception by decrementing retries or other actions
            retries -= 1
    return None  # Return 0 if retries are exhausted


while time.time() < five_min:
    safe_click((By.ID, "bigCookie"))
    if time.time() > timeout:

        money = safe_text((By.ID, "cookies"))
        if money is not None:
            money = money.split(" ")[0].replace(",", "")
        else:
            # print("Unable to retrieve text.")
            break

        money_in_integer = int(money)
        # print("money: ", money_in_integer)

        # choose max upgrade available and affordable
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#upgrades .enabled")
        upgrades_prices = [int(upgrade_text((By.ID, f"upgrade{i}")).replace(",", "")) for i in range(len(upgrades))]
        if len(upgrades_prices) > 0:
            max_upgrade_price = max(upgrades_prices)
            max_upgrade_price_index = upgrades_prices.index(max_upgrade_price)
            # print("upgrade max price: ", max(upgrades_prices))
            # print("clicked", max_upgrade_price_index)
            hand1 = driver.find_element(By.ID, f"upgrade{max_upgrade_price_index}")
            driver.execute_script("arguments[0].click();", hand1)

        # choose max product available and affordable
        products = driver.find_elements(By.CSS_SELECTOR, value="#products .enabled .price")
        if len(products) > 0:
            products_prices = [int(product.text.replace(",", "")) for product in products]
            max_product_price = max(products_prices)
            max_product_price_index = products_prices.index(max_product_price)

            # print("product max price: ", max_product_price)
            if max_product_price < money_in_integer:
                # print("clicked", max_product_price_index)
                hand2 = driver.find_element(By.ID, f"product{max_product_price_index}")
                driver.execute_script("arguments[0].click();", hand2)

                'arguments[0] refers to the first argument passed to the JavaScript function, which is our element in '
                'this case.'
                '.click() is a JavaScript method that simulates a click event on the element.'

                'By using JavaScript to trigger the click event, we bypass some of the normal click event handling that'
                'might be causing the ElementClickInterceptedException. This method can be more robust in scenarios '
                'where standard Selenium clicks are intercepted or blocked by other elements, such as overlays or '
                'popups.'

                'Remember to use this approach judiciously, as it might not be as human-like as a regular Selenium '
                'click. It\'s typically used when other methods fail to interact with the element due to various '
                'reasons, including web page design and interactivity.'

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

time.sleep(1)
perSec = safe_text((By.ID, "cookiesPerSecond"))
if perSec is not None:
    print(perSec)
else:
    print("Unable to retrieve text.")

driver.quit()
