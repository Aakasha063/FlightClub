import requests
import os
from twilio.rest import Client
import smtplib
URL = "https://api.sheety.co/dfcc8bd7bb14986c676944905ac8d2a3/flightDeals/users"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

class NotificationManager:
    def sendNotification(self, details):
        if "via_city" in details:
            msg = f"LOW PRICE ALERT! Only £{details['Price']} from {details['Departure City Name']}-{details['fly from']} to {details['Arrival City Name']}-{details['fly to']}, from {details['outbound date']} to {details['inbound date']} Flight has 1 stopover from{details['Departure City Name']} to {details['via_city']}"
        else:
            msg = f"LOW PRICE ALERT! Only £{details['Price']} from {details['Departure City Name']}-{details['fly from']} to {details['Arrival City Name']}-{details['fly to']}, from {details['outbound date']} to {details['inbound date']}"
        account_sid = "AC7e8f4996c90159f48a37bede6a558f9c"
        auth_token = "620e347c3cdaed69cf07a3880bec2c333b"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg,
            from_='+16074008358',
            to='+918685851664'
        )
        print(message.sid)
        response = requests.get(url=URL)
        data = response.json()
        for users in data["users"]:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user="axbydz1029@gmail.com", password="abcd12!@")
                connection.sendmail(from_addr="axbydz1029@gmail.com", to_addrs=users["email"], msg=f"Subject:FLight Deals\n\n{msg}\nhttps://www.google.co.uk/flights?hl=en#flt={details['fly from']}.{details['fly to']}.{details['outbound date']}*{details['fly to']}.{details['fly from']}.{details['inbound date']}".encode("utf-8"))





