import requests
import datetime
import os

SHEET_KEY = os.environ["SHEET_KEY"]
SHEET_URL = os.environ["SHEET_URL"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        header = {
            "Authorization": f"Bearer {SHEET_KEY}"
        }
        response = requests.get(url=SHEET_URL, headers=header)
        print(response.json())

