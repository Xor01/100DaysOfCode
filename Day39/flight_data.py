from flight_search import *
from data_manager import *
import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.data = DataManager()

        # Dates Control
        self.rows = self.data.get_sheet_data()
        self.today = datetime.datetime.now()
        self.six_month_ago = self.today - datetime.timedelta(days=60)
        self.six_month_ago = self.six_month_ago.strftime("%d:%m:%Y")

        # set data to search for from sheet api
        for row in self.rows:
            fly_from = "HND"
            fly_to = row["iataCode"]
            date_from = self.today.strftime("%d:%m:%Y")
            date_to = self.six_month_ago
            # Here set the maximum price to search with
            price_to = row["lowestPrice"]

            # Get flights data
            self.flight_info = FlightSearch(fly_from, fly_to, date_from, date_to, price_to).flight_info

            # check if a flight is not empty
            if self.flight_info:
                self.flight_info = self.flight_info[0]
                print(f"From: {self.flight_info['cityFrom']}, {self.flight_info['countryFrom']['name']}")
                print(f"To: {self.flight_info['cityTo']}, {self.flight_info['countryTo']['name']}")
                print(f"Price: {self.flight_info['price']}")
                print("-----------------------------------------")


a = FlightData()
