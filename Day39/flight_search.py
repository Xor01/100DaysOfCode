import requests
import os
import smtplib


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to, price_to):
        self.END_POINT = "https://api.tequila.kiwi.com/v2/search"
        self.API_KEY = os.environ["TEQUILA_KEY"]
        self.header = {"apikey": self.API_KEY}
        self.flight_info = None
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_From": date_from,
            "date_to": date_to,
            "price_to": price_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        self.search_flight()

    def search_flight(self):
        data = []
        response = requests.get(url=self.END_POINT, params=self.parameters, headers=self.header)
        if "data" not in response.json():
            return

        self.flight_info = response.json()["data"]
        try:
            arrival_time = str(self.flight_info[0]["utc_departure"]).split("T")
            arrival_time[1] = arrival_time[1].replace("Z", "")

            departure_time = str(self.flight_info[0]["utc_arrival"]).split("T")
            departure_time[1] = departure_time[1].replace("Z", "")

            data.append(self.flight_info[0]["cityFrom"])
            data.append(self.flight_info[0]["countryFrom"]["name"])

            data.append(self.flight_info[0]["cityTo"])
            data.append(self.flight_info[0]["countryTo"]["name"])

            data.append(departure_time[0])
            data.append(departure_time[1])

            data.append(arrival_time[0])
            data.append(arrival_time[1])
            data.append(str(self.flight_info[0]["price"]))

            try:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=os.environ["EMAIL"], password=os.environ["PASS"])
                    connection.sendmail(
                        from_addr=os.environ["EMAIL"],
                        to_addrs=os.environ["EMAIL"],
                        msg=f"Subject:Flight Alert for you\n\nCity From: {data[0]} - {data[1]}\nCity To: {data[2]} -"
                            f" {data[3]}\nUtc Departure time: {data[4]} - {data[5]}\nUtc Arrival time: {data[6]} -"
                            f" {data[7]}\nPrice: {data[8]}"
                    )
            except NameError:
                print("Check Variables exit in SMTPInfo.py.")

            except smtplib.SMTPAuthenticationError:
                print("Authentication Error: check your credentials.")

        except KeyError:
            return False
        except IndexError:
            return False
