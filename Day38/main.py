# Workout Tracker using Google Sheets
from datetime import date, datetime
from requests import post
from os import environ

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_KEY = environ["SHEET_KEY"]
SHEET_URL = environ["SHEET_URL"]
APP_ID = environ["APP_ID"]
APP_KEY = environ["API_KEY"]


def send_to_exercise_api(query):
    header = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }
    params = {
        "query": query,
    }
    response = post(url=EXERCISE_ENDPOINT, json=params, headers=header)
    return response.json()


def send_to_sheet():
    query = input("Enter what exercise/exercises you've complete: ")
    exercises = send_to_exercise_api(query)["exercises"]
    for exercise in exercises:
        params = {
            "workout": {
                "date": date.today().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%X"),
                "exercise": exercise["user_input"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        header = {
            "Authorization": f"Bearer {SHEET_KEY}"
        }
        response = post(url=SHEET_URL, json=params, headers=header)
        print(response.status_code)


send_to_sheet()
