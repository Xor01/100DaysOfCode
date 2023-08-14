# ISS overheard Notifier
import requests
from datetime import datetime
from time import sleep
import smtplib
from os import getenv
MY_LAT = 41.5707  # Your latitude
MY_LONG = -152.5490  # Your longitude


def is_iss_near_me():
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


def is_it_dark():
    return my_hour >= sunset and my_hour >= sunrise


iss_response = requests.get(url="https://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
my_hour = time_now.hour


while True:
    if is_iss_near_me() and is_it_dark():
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=getenv('EMAIL'), password=getenv('PASSWORD'))
                connection.sendmail(
                    from_addr=getenv('EMAIL'),
                    to_addrs="tomesoh800@dicopto.com",
                    msg="Subject: Look UP\n\nISS Is above you."
                )
        except NameError:
            print("Check Variables exit in SMTPInfo.py.")

        except smtplib.SMTPAuthenticationError:
            print("Authentication Error: check your credentials.")
    sleep(60)
