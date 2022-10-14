# Birthday wisher
import smtplib
import datetime as dt
from SMTPInfo import *
import random
import pandas


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv :Done

# 2. Check if today matches a birthday in the birthdays.csv :Done
def get_birthday():
    try:
        data = pandas.read_csv("birthdays.csv")
    except FileNotFoundError:
        print("No birthdays.csv file found.")
    except pandas.errors.EmptyDataError:
        print("birthday.csv is empty.")
    else:
        for (index, row) in data.iterrows():
            if row.month == dt.datetime.now().month and row.day == dt.datetime.now().day:
                pick_rand_template(row["name"])


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv :Done
def pick_rand_template(name):
    template_num = random.randint(1, 3)
    try:
        with open(f"letter_templates/letter_{template_num}.txt") as file:
            content = file.read()
            msg = content.replace("[NAME]", name)
            send_birthday_wish(msg)

    except FileNotFoundError:
        print(f"Templates with name letter_templates/letter_{template_num}.txt was not found.")


# 4. Send the letter generated in step 3 to that person's email address. :Done
def send_birthday_wish(msg):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="tomesoh800@dicopto.com",
                msg=f"Subject: Happy Birthday\n\n{msg}"
            )
    except NameError:
        print("Check Variables exit in SMTPInfo.py.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication Error: check your credentials.")


get_birthday()
