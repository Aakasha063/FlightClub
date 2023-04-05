from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from  notification_manager import NotificationManager

sheet_data = DataManager()

# for cities in sheet_data.data:
#     fls = FlightSearch()
#     cities["iataCode"] = fls.add_iatavalues(cities["city"])

# sheet_data.editrows()

for cities in sheet_data.data:
    fd = FlightData()
    details = fd.search_flights(cities["iataCode"])
    if details == None:
        pass
    else:
        if cities['lowestPrice'] > int(details["Price"]):
            nf = NotificationManager()
            nf.sendNotification(details)

