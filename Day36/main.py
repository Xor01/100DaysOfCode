from newsapi import NewsApiClient
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

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
before_yesterday = today - datetime.timedelta(days=2)

response = requests.get(url=url, params=stocks_params)
data = response.json()["Time Series (Daily)"]

days = [value for (day, value) in data.items()]

yesterday_stock = days[0]
before_yesterday_stock = days[1]
difference = float(yesterday_stock["4. close"]) - float(before_yesterday_stock["4. close"])

if (difference / float(yesterday_stock["4. close"])) * 100 > 5:
    print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_data = news.json()

articles = news_data["articles"][:3]
print(articles)
## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
