import requests
from twilio.rest import Client

WEATHER_API_KEY="000000000000000000000"
WEATHER_URL="https://api.openweathermap.org/data/2.5/onecall"

ACC_SID="00000000000000000000000000000"
AUTH_TOKEN="00000000000000000000"

parameters={
    "lat":29.502560,
    "lon":79.935600,
    "exclude":"current,minutely,daily",
    "appid":WEATHER_API_KEY
}

response=requests.get(url=WEATHER_URL,params=parameters)
response.raise_for_status()

data=response.json()["hourly"][:12]

def send_mssg():
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring your umbrella ☔🌂☂. It will rain 🌧⛈.",
        from_='+15612793820',
        to='+916395895736'
    )
    print(message.status)

for hour in data:
    if hour["weather"][0]["id"] <700:
        send_mssg()
        break
