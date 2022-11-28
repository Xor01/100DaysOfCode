import flight_search
import flight_data
import requests
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_email(self, message):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="EMAIL", password="PASSWORD")
                connection.sendmail(
                    from_addr="EMAIL",
                    to_addrs="tomesoh800@dicopto.com",
                    msg=f"Subject:\n\n{message}"
                )
        except NameError:
            print("Check Variables exit in SMTPInfo.py.")

        except smtplib.SMTPAuthenticationError:
            print("Authentication Error: check your credentials.")
