import requests
import os

SHEET_KEY = os.environ["SHEET_KEY"]
SHEET_URL = os.environ["SHEET_URL"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = None
        self.get_sheet_data()

    def get_sheet_data(self):
        header = {
            "Authorization": f"Bearer {SHEET_KEY}"
        }
        self.response = requests.get(url=SHEET_URL, headers=header)
        return self.response.json()["prices"]
