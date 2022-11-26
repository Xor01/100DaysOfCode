import requests
from os import environ
SHEETY_PRICES_ENDPOINT = environ["SHEETY_PRICE_URL"]
SHEETY_USERS_ENDPOINT = environ["SHEETY_USERS_URL"]
SHEET_KEY = environ["SHEET_KEY"]


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = None
        self.header = {
            "Authorization": f"Bearer {SHEET_KEY}"
        }

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:

            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.header
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/2c2834b8f88d0aeecfbe77ccfdadfc95/flightDeals/users"
        response = requests.get(url=customers_endpoint, headers=self.header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
