import requests
import os
import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to, price_to):
        self.END_POINT = "https://api.tequila.kiwi.com/v2/search"
        self.API_KEY = os.environ["TEQUILA_KEY"]
        self.header = {"apikey": self.API_KEY}
        self.flight_info = None
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_From": date_from,
            "date_to": date_to,
            "price_to": price_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        self.search_flight()

    def search_flight(self):
        response = requests.get(url=self.END_POINT, params=self.parameters, headers=self.header)
        if "data" not in response.json():
            return

        self.flight_info = response.json()["data"]
        try:
            arrival_time = str(self.flight_info[0]["utc_departure"]).split("T")
            arrival_time[1] = arrival_time[1].replace("Z", "")

            departure_time = str(self.flight_info[0]["utc_arrival"]).split("T")
            departure_time[1] = departure_time[1].replace("Z", "")

            print("City From: " + self.flight_info[0]["cityFrom"] + " - " + self.flight_info[0]["countryFrom"]["name"])
            print("City To: " + self.flight_info[0]["cityTo"] + " - " + self.flight_info[0]["countryTo"]["name"])

            print("Utc Arrival Time: " + departure_time[0] + " " + departure_time[1])
            print("Utc Departure Time: " + arrival_time[0] + " " + arrival_time[1])

            print("Price: " + str(self.flight_info[0]["price"]) + " EUR")
            print("-------------------------------------------")
        except KeyError:
            pass
        except IndexError:
            pass
