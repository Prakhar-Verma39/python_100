import json
import os.path
from bs4 import BeautifulSoup
from fillGoogleForm import FillGoogleForms
from request_page_data import RequestPageData

"""
    Automating a data-entry job where the data needs to-be scrapped from house rent site using beautifulsoup 
    and requests modules. The data scrapped is passed on to selenium webdriver to fill in a google form and 
    that each data is submitted to a google sheet linked manually.  
"""

can_continue = False

if os.path.exists('all_data.json'):
    can_continue = True
    print("Ok! Get Ready for scraping.")
else:
    print("Oh No! Got no data to continue.")

if can_continue:

    # using data saved in a single JSON file
    with open("all_data.json", "r") as file:
        all_pages_data = json.load(file)

    for page_data in all_pages_data:

        soup = BeautifulSoup(page_data["content"], "html.parser")
        houses_listings = soup.find_all("li", class_='ListItem-c11n-8-84-3__sc-10e22w8-0 '
                                                     'StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl')

        website_url = "https://www.zillow.com"
        addresses_list = []
        links_list = []
        prices_list = []

        for h in houses_listings:
            addresses = h.find("address")
            prices = h.find("span", {"data-test": "property-card-price"})
            links = h.find("a")

            if addresses is not None and prices is not None and links is not None:
                addresses_list.append(addresses.text)
                prices_list.append(prices.text)

                if website_url in links['href']:
                    links_list.append(links['href'])
                else:
                    links_list.append(f"{website_url}{links['href']}")

        FillGoogleForms(links_list, addresses_list, prices_list)
