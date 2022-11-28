# Habit Tracker using Pixela
import requests
import datetime
import os

USERNAME = "xor01"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_PIXL_API = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/g1"
TODAY_DATE = datetime.datetime.today().strftime("%Y%m%d")
HEADERS = {
        "X-USER-TOKEN": os.environ["PIXELA_TOKEN"]
    }


def create_account():
    create_account_json = {
        "token": os.environ["PIXELA_TOKEN"],
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    account_creat_response = requests.post(url=PIXELA_ENDPOINT, json=create_account_json)
    print(account_creat_response.text)


def create_graph(graph_id, graph_name, uint, data_type, color):
    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": uint,
        "type": data_type,
        "color": color,
    }

    creat_graph_response = requests.put(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(creat_graph_response.text)


def add_pixl(quantity):
    pixl_json = {
        "date": TODAY_DATE,
        "quantity": quantity,
    }
    response = requests.post(url=PIXELA_PIXL_API, json=pixl_json, headers=HEADERS)
    print(response.text)


# TODO 1: Update this using **kwargs
def update_pixl(graph_id, date, quantity):
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}"

    update_json = {
        "quantity": str(quantity)
    }
    update_response = requests.put(url=update_endpoint, json=update_json, headers=HEADERS)
    print(update_response.text)


def delete_pixl(graph_id, date):
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}"
    delete_response = requests.delete(url=delete_endpoint, headers=HEADERS)
    print(delete_response.text)
