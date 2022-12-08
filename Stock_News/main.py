import requests
import re, html
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "HS9K2ELB2HB0G27I"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e1ec30a3e26445af83f0f271c9e71350"

ACC_SID="ACd9d5a47d57620d8c41946422429f271f"
AUTH_TOKEN="04b8ed9891543693de69576b48495fd0"


NEWS_MSSG = ""

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_news(stock_per):
    global NEWS_MSSG

    if stock_per >= 0:
        NEWS_MSSG += f'''TSLA: 🔺{stock_per}%'''
    else:
        NEWS_MSSG += f'''TSLA: 🔻{abs(stock_per)}%'''

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_title = [n["title"] for n in response_news.json()["articles"][:3]]
    news_des = [html.unescape(cleanhtml(n["description"])) for n in response_news.json()["articles"][:3]]

    NEWS_MSSG += f'''
Headline: {news_title[0]}
Brief: {news_des[0]}
Headline: {news_title[1]}
Brief: {news_des[1]}
Headline: {news_title[2]}
Brief: {news_des[2]}'''


def send_mssg():
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=NEWS_MSSG,
        from_='+15612793820',
        to='+916395895736'
    )
    print(message.status)


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = list(response.json()["Time Series (Daily)"].values())[:2]
new_stock = float(data[0]["4. close"])
prev_stock = float(data[1]["4. close"])
stock_per = round(((new_stock - prev_stock) / new_stock) * 100, 2)

get_news(stock_per)
send_mssg()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
