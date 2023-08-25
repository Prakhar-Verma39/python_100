import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import datetime as dt
import random
import pandas

# store and use environment variable from .env file
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

my_name = "Prakhar Verma"

# obtain current day of the week
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
with open("birthdays.csv", "r") as f:
    birthdays = pandas.read_csv(f)
for index, birthday in birthdays.iterrows():
    if birthday['month'] == month and birthday['day'] == day:

        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", 'r') as f:
            letter = f.read()
            letter = letter.replace("[Name]", birthday['name'])
            letter = letter.replace("[Your Name]", my_name)

        if letter:
            # create message object using EmailMessage class
            msg = EmailMessage()
            msg['Subject'] = "Birthday Wishes"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = birthday['email']
            msg.set_content(letter)

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
