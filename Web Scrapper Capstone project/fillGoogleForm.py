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


def fill_form(all_links, all_addresses, all_prices):
    for n in range(len(all_links)):
        # Substitute your own Google Form URL here 👇
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScrJT1Ql4b_3mIvN0tsDGQitTZrRzafjvTwnaN34Mncpu6oFg/viewform")
        time.sleep(2)

        address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
        link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        address.send_keys(all_addresses[n])
        price.send_keys(all_prices[n])
        link.send_keys(all_links[n])
        submit_button.click()


class FillGoogleForms:

    def __init__(self, all_links, all_addresses, all_prices):
        self.all_links = all_links
        self.all_addresses = all_addresses
        self.all_prices = all_prices
        fill_form(self.all_links, self.all_addresses, self.all_prices)

