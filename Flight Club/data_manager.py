import requests
URL = "https://api.sheety.co/dfcc8bd7bb14986c676944905ac8d2a3/flightDeals/prices"
class DataManager:
    def __init__(self):
        response = requests.get(url=URL)
        self.data = response.json()["prices"]

    def editrows(self):
        for rows in self.data:
            headers = {
                "Content-Type" : "application/json"
            }
            params = {
                "price":{
                "iataCode": rows["iataCode"]
                }
            }
            req = requests.put(url=f"{URL}/{rows['id']}", json=params, headers=headers)
            print(req.text)

