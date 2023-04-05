import requests
import datetime as dt
from datetime import timedelta
from pprint import pprint

URL = "https://tequila-api.kiwi.com/v2/search"
class FlightData:
    def search_flights(self,city):
        headers = {
            "apikey": "g0KbgWoIbHVyRsz2-rrxYHzY_vKbJjDK"
        }
        date_from = str(dt.datetime.now().strftime("%d/%m/%Y"))
        date_to = str((dt.datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y"))
        params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 1
        }
        response = requests.get(url=URL, params=params, headers=headers)
        data = response.json()
        if len(data["data"]) != 0:
             flight_details = data["data"][0]
             if len(flight_details["route"]) == 2:
                 outbound_date = flight_details["route"][0]["local_departure"].split("T")[0]
                 inbound_date = flight_details["route"][-1]["local_departure"].split("T")[0]
                 details = {
                     "Price": flight_details["price"],
                     "Departure City Name": flight_details["cityFrom"],
                     "fly from": flight_details["flyFrom"],
                     "fly to": flight_details["flyTo"],
                     "Arrival City Name": flight_details["cityTo"],
                     "Arrival City Code": flight_details["cityCodeTo"],
                     "outbound date": outbound_date,
                     "inbound date": inbound_date,
                 }
             else:
                 outbound_date = flight_details["route"][0]["local_departure"].split("T")[0]
                 inbound_date = flight_details["route"][2]["local_departure"].split("T")[0]
                 details = {
                     "Price": flight_details["price"],
                     "Departure City Name": flight_details["cityFrom"],
                     "fly from": flight_details["flyFrom"],
                     "fly to": flight_details["flyTo"],
                     "Arrival City Name": flight_details["cityTo"],
                     "Arrival City Code": flight_details["cityCodeTo"],
                     "outbound date": outbound_date,
                     "inbound date": inbound_date,
                     "via_city": flight_details["route"][0]["cityTo"]
                 }
             return details
        else:
             return None


