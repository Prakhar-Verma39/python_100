import time
import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import os

# my place coordinates
MY_LAT = 25.443920
MY_LONG = 81.825027

# store and use environment variable from .env file
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')


def is_iss_overhead():
    """
    to get the position of ISS(International Space Station) and return true if iss is overhead
    """

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # check if my position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    """
    to get the sunrise and sunset time of my place and check if it is night time
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()

    # time in UTC format
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[:2]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[:2]

    # change into IST format
    UTC_to_IST = lambda a, b: [int(a) + 5, int(b) + 30]

    sunrise = UTC_to_IST(sunrise[0], sunrise[1])
    sunset = UTC_to_IST(sunset[0], sunset[1])

    # get current time
    time_now = datetime.now()

    # check if it is nighttime
    if (time_now.hour < sunset[0] and time_now.minute < sunset[1]) or (time_now.hour > sunrise[0] and time_now.minute > sunrise[1]):
        return True


while True:
    # sleep for some amount of time
    time.sleep(60)
    if is_iss_overhead() and is_night():

        # create message object using EmailMessage class
        msg = EmailMessage()
        msg['Subject'] = "Look Up"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content("The ISS is above you in the sky.")

        # establish connection
        with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
            connection.ehlo()
            # encrypt message
            connection.starttls()
            connection.ehlo()
            # logging in
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            # send message
            connection.send_message(msg)




