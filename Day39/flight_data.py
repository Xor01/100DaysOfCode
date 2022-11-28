from flight_search import *
from data_manager import *
import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.data = DataManager()

        # Dates Control
        self.rows = self.data.get_sheet_data()
        self.tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        self.six_month_ago = datetime.datetime.now() + datetime.timedelta(days=6 * 30)
        self.six_month_ago = self.six_month_ago.strftime("%d/%m/%Y")

        # set data to search for from sheet api
        for row in self.rows:
            fly_from = "CDG"
            fly_to = row["iataCode"]
            date_from = self.tomorrow.strftime("%d/%m/%Y")
            date_to = self.six_month_ago
            # Here set the maximum price to search with
            price_to = row["lowestPrice"]
            # Get flights data
            self.flight_info = FlightSearch(fly_from, fly_to, date_from, date_to, price_to)
            # check if a flight is not empty


a = FlightData()
