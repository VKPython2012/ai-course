import os
import requests
import pandas as pd 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") # referene the api key without revealing the value

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {
        "q":city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    print(data)

get_weather("Ho Chi Minh City")