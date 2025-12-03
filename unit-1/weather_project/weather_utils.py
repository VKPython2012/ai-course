import os
import requests
import pandas as pd 
from dotenv import load_dotenv
from datetime import datetime

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

    return data["list"] # list of 3 hours interval forecast entries over 5 days

def convert_to_df(data): # Raw json → pd dataframe
    records = []
    for entry in data:
        records.append({
            "datetime": pd.to_datetime(entry["dt_txt"]),
            "temp": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "wind": entry["wind"]["speed"],
        })
    
    df = pd.DataFrame(records)
    return df

df = convert_to_df(get_weather("Ho Chi Minh City"))
df.to_csv("test_data.csv")

def filter_by_date(df,start,end): # Filter df by a datetime range
    mask = (df["datetime"] >= start) & (df["datetime"] <= end)
    return df.loc[mask] # Return row(s) in start/end range

df_filtered = filter_by_date(df, datetime(2025,12,4,0,0,0), datetime(2025,12,5,18,0,0))
df_filtered.to_csv("filtered_data.csv")

def compute_stats(df, metric):
    max_val = df[metric].max()
    min_val = df[metric].min()
    mean_val = df[metric].mean()
    percentage_change = ((df[metric].iloc[-1] - df[metric].iloc[0]) / df[metric].iloc[0]) * 100
    
    max_time = df.loc[df[metric] == max_val, "datetime"].iloc[0]
    min_time = df.loc[df[metric] == min_val, "datetime"].iloc[0]

    return {
        "max": round(max_val, 2),
        "min": round(min_val, 2),
        "mean": round(mean_val, 2),
        "percent_change": round(percentage_change, 2),
        "max_time": max_time,
        "min_time": min_time,
    }

print(compute_stats(df, "temp"))
print(compute_stats(df_filtered, "temp"))