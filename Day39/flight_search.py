import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to, price_to):
        self.flights_info = None
        self.END_POINT = "https://api.tequila.kiwi.com/v2/search"
        self.API_KEY = os.environ["TEQUILA_KEY"]
        self.header = {"apikey": self.API_KEY}
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_From": date_from,
            "date_to": date_to,
            "price_to": price_to,
        }
        self.search_flight()

    def search_flight(self):
        response = requests.get(url=self.END_POINT, params=self.parameters, headers=self.header)
        self.flights_info = response.json()["data"]
        self.flights_info = [value for value in self.flights_info if "price" in value]
