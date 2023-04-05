import requests

URL = "https://tequila-api.kiwi.com/locations/query"
class FlightSearch:
    def __init__(self):
        self.iatavalue = "testing"

    def add_iatavalues(self, city):
        headers = {
            "apikey": "g0KbgWoIbHVyRsz2-rrxYHzY_vKbJjDK"
        }
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=URL, params=params, headers=headers)
        data = response.json()
        return data["locations"][0]["code"]




