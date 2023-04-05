import requests
URL = "https://api.sheety.co/dfcc8bd7bb14986c676944905ac8d2a3/flightDeals/users"
f_name = input("What is your first name? ")
l_name = input("What is your Lastname? ")
email = input("Enter your email ")
confirm_email = input("Enter your email")
if email == confirm_email:
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "user":{
            "firstName": f_name,
            "lastName": l_name,
            "email": email
        }
    }
    response = requests.post(url=URL, json=params, headers=headers)
