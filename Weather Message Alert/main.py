import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
sent_to_number = os.getenv("SENT_TO_PHONE_NUMBER")
api_key = os.getenv("OPEN_WEATHER_API_KEY")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_parameters = {
    "lat": 25.443920,
    "lon": 81.825027,
    "exclude": "",
    "appid": api_key,
    "lang": "hi"
}

response = requests.get(OWM_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
next_24_hours_data_in_gap_of_3 = weather_data["list"][:8]

will_rain = False

for data_3_hours in next_24_hours_data_in_gap_of_3:
    condition_code = data_3_hours["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

customized_message = "Hey buddy, get your umbrella ☔, it's going to rain."

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=customized_message,
            from_=twilio_phone_number,
            to=sent_to_number
    )
    print(message.status)
