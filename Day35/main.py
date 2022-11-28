from APIS import *
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": LAT,
    "lon": LON,
    "APPID": os.environ.get("OPEN_WEATHER_API"),
    "exclude": "daily,minutely,current",

}
response = requests.get(url=END_POINT, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☔️", from_="YOUR TWILIO VIRTUAL NUMBER",
                to="YOUR TWILIO VERIFIED REAL NUMBER")
    print(message.status)
