import smtplib
import datetime as dt
from SMTPInfo import *
import random


def send_motivational_quote(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="tomesoh800@dicopto.com",
            msg=f"Subject: Good Morning\n\n{msg}"
        )


with open("quotes.txt") as file:
    data = file.readlines()
    quote = random.choice(data)
    if dt.datetime.now().weekday() == 4:
        send_motivational_quote(quote)
