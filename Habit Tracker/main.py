import requests
from datetime import datetime

USERNAME = 
TOKEN = 


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphID = "graph1"

graph_config = {
    "id": graphID,
    "name": "Study Hours",
    "unit": "Hrs",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graphID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours you study today? "),
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# <yyyyMMdd> format
date = 20230901
update_data = {
    "quantity": "20",
}
# response = requests.put(url=f"{pixel_endpoint}/{date}", json=update_data, headers=headers)
# print(response.text)

# <yyyyMMdd> format
date = 20230901

# response = requests.delete(url=f"{pixel_endpoint}/{date}", headers=headers)
# print(response.text)

update_profile_data = {
    "pinnedGraphID": graphID,
    "displayName": USERNAME,
    "timezone": "Asia/Kolkata",

}

# update user profile
response = requests.put(url=f"https://pixe.la/@{USERNAME}", json=update_profile_data, headers=headers)
print(response.text)
