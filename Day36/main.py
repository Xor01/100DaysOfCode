# Stock Trading News Alert
from twilio.rest import Client
import requests
import os
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
url = 'https://www.alphavantage.co/query'
stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("ALPHA_KEY"),

}

news_params = {
    "q": "Tesla Inc",
    "apikey": os.environ.get("NEWS_API"),
    "language": "en"
}


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
before_yesterday = today - datetime.timedelta(days=2)

response = requests.get(url=url, params=stocks_params)
data = response.json()["Time Series (Daily)"]

days = [value for (day, value) in data.items()]

yesterday_stock = days[0]
before_yesterday_stock = days[1]
difference = float(yesterday_stock["4. close"]) - float(before_yesterday_stock["4. close"])

difference_percentage = round((difference / float(yesterday_stock["4. close"])) * 100, 2)

if abs(difference_percentage) >= 5:
    up_down = None
    if difference > 0:
        up_down = "📈"
    else:
        up_down = "📉"

    news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news.json()

    articles = news_data["articles"][:3]
    formatted_articles = [
        f"{STOCK}: {up_down}{difference_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in articles
    ]

    for article in formatted_articles:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_=os.environ['TWILIO_NUMBER'],
            to=os.environ['MY_NUMBER']
        )
        print(message.status)
