import smtplib
import datetime as dt
from SMTPInfo import *
import random


def send_birthday_wish(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="tomesoh800@dicopto.com",
            msg=f"Subject: Good Morning\n\n{msg}"
        )