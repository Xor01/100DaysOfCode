import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to):
        self.END_POINT = "https://api.tequila.kiwi.com/v2/search"
        self.API_KEY = os.environ["TEQUILE_KEY"]
        self.header = {"apikey": self.API_KEY}
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_From": date_from,
            "date_to": date_to,
        }

    def search_flight(self):
        response = requests.get(url=self.END_POINT, params=self.parameters, headers=self.header)
        print(response.json())


