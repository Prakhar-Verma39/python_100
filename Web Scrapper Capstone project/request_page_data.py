import requests
import json
import time


class RequestPageData:

    # class methods are typically used to work with class-level attributes and perform operations that are related to
    # the class itself, rather than specific instances of the class.

    @classmethod
    def give_next_page_url(cls, page_num):
        if page_num == 1:
            url = "https://www.zillow.com/san-francisco-county-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue" \
                  "%2C%22mapBounds%22%3A%7B%22west%22%3A-124.628437265625%2C%22east%22%3A-120.827167734375%2C%22south%22" \
                  "%3A36.530751557520155%2C%22north%22%3A39.01825807941593%7D%2C%22mapZoom%22%3A8%2C%22usersSearchTerm%22" \
                  "%3A%22San%20Francisco%20County%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3227%2C" \
                  "%22regionType%22%3A4%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22" \
                  "%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22" \
                  "%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore" \
                  "%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A563426%7D%2C%22mp%22" \
                  "%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C" \
                  "%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B" \
                  "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D "
        else:
            url = f'https://www.zillow.com/san-francisco-county-ca/rentals/{page_num}_q/?searchQueryState=%7B%22mapBounds' \
                  f'%22%3A%7B%22north%22%3A38.39455781243456%2C%22south%22%3A37.170310860069144%2C%22east%22%3A-121' \
                  f'.68135474609375%2C%22west%22%3A-123.77425025390625%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco' \
                  f'%20County%20CA%22%2C%22mapZoom%22%3A9%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3227%2C' \
                  f'%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max' \
                  f'%22%3A563426%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22' \
                  f'%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse' \
                  f'%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B' \
                  f'%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse' \
                  f'%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C' \
                  f'%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%22currentPage%22%3A{page_num}%7D%7D'

        return url


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en,en-GB;q=0.9,en-US;q=0.8,hi;q=0.7",
}

# Define the number of pages you want to scrape
num_pages = 19

# Initialize an empty list to store data from each page
all_data = []

# Set up rate limiting parameters
requests_per_minute = 10  # Adjust as needed
time_interval = 60 / requests_per_minute  # Calculate the time interval

for page_number in range(1, num_pages + 1):

    try:
        response = requests.get(url=RequestPageData.give_next_page_url(page_number), headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Process the response (e.g., parse HTML or JSON)
        # Extract the listings or data from the response
        # This is a simplified example; adapt it for your use case
        data = {"page_number": page_number, "content": response.text}
        all_data.append(data)

        # Print the current page number and URL for reference
        print(f"Page {page_number}: {response.url}")

        # # Save the data to a JSON file after each page (optional)
        # with open(f"data_page_{page_number}.json", "w") as file:
        #     json.dump(data, file)

        # Implement rate limiting to avoid overloading the server
        time.sleep(time_interval)

    except requests.exceptions.RequestException as e:
        print(f"Error on page {page_number}: {e}")

if len(all_data) != 0:
    # Save all the data to a single JSON file
    with open("all_data.json", "w") as file:
        json.dump(all_data, file)

    print("Data storage complete.")
else:
    print("No Data gathered via url.")
