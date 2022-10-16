import requests

params = {
    "amount": 10,
    "type": "boolean"
}
try:
    dt = requests.get("https://opentdb.com/api.php", params=params)
    dt.raise_for_status()
except:
    print("Something happened, could not fetch data.")
else:
    data = dt.json()["results"]
    question_data = data
