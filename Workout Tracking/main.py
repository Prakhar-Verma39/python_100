import requests as requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("AAP_ID")
APP_KEY = os.getenv("APP_KEY")
WEBSITE_NUTRITIONIX = "https://trackapi.nutritionix.com/"
WEBSITE_SHEETY = "https://api.sheety.co/"
TOKEN = os.getenv("BEARER_TOKEN")
SHEETY_POST_ROUTE = f"edc23a5186b14dca9216aca0c94fad29/{os.getenv('PROJECT_NAME')}/"
SHEET_NAME = os.getenv("SHEET_NAME")
TIMEZONE = os.getenv("TIMEZONE")
GENDER = os.getenv("GENDER")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
AGE = os.getenv("AGE")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    # "x-remote-user-id": 0,
}

parameters = {
    "query": input("What's your workout today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
nlp_post_endpoint = f"{WEBSITE_NUTRITIONIX}v2/natural/exercise"
sheety_post_endpoint = f"{WEBSITE_SHEETY}{SHEETY_POST_ROUTE}{SHEET_NAME}"

response = requests.post(url=nlp_post_endpoint, json=parameters, headers=headers)
data = response.json()
print("MESSAGE FROM 'nutritionix.com': ", response)

bearer_headers = {
    "Authorization": TOKEN,
}

exercises = data["exercises"]
for i, exercise in enumerate(exercises):

    today = datetime.now()
    current_date = today.strftime("%d %B, %Y")
    current_time = today.strftime("%I:%M %p")
    # print(current_time, current_date)
    # print(exercise["user_input"], exercise["duration_min"], exercise["nf_calories"])
    parameters = {
        "workout": {
            "date": current_date,
            "time":  current_time,
            "exercise": exercise["user_input"],
            "duration":  f"{exercise['duration_min']} min",
            "calories":  exercise["nf_calories"],
        }
    }
    # print(parameters)
    response = requests.post(url=sheety_post_endpoint, json=parameters, headers=bearer_headers)
    print(f"MESSAGE FROM 'sheety.co' on updating exercise no. {i+1}: ", response)
