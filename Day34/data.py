import requests

params = {
    "amount": 10,
    "type": "boolean"
}
dt = requests.get("https://opentdb.com/api.php", params=params)
dt.raise_for_status()

data = dt.json()["results"]

question_data = data
