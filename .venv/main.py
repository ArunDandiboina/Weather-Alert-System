import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

API_KEY=os.environ.get("YOUR_API_KEY")
LAT=os.environ.get("YOUR_LAT")
LON=os.environ.get("YOUR_LON")
URL="https://api.openweathermap.org/data/2.5/forecast"
weather_params={
    "lat":LAT,
    "lon":LON,
    "cnt":5,
    "appid":API_KEY
}

will_rain = False
response = requests.get(URL,params=weather_params)
response.raise_for_status()
weather_list = response.json()["list"]
for w_data in weather_list:
    code = w_data["weather"][0]["id"]
    if(code<700):
        will_rain = True
        break
if will_rain:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an Umbrella☂️",
        from_=os.environ.get("YOUR_TWILIO_NUMBER"),
        to=os.environ.get("YOUR_NUMBER")
    )

    print(message.status)
