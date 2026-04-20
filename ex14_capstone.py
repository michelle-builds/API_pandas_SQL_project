

import sqlite3
import requests
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("weather_cities.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY,
        city TEXT,
        date TEXT,
        time TEXT,
        temp_c INTEGER,
        feels_like_c INTEGER,
        conditions TEXT,
        wind_kmph INTEGER,
        uv_index INTEGER
    )
""")
conn.commit()
print("Table created.")

cities = ["Edmonton", "Vancouver", "Toronto", "Calgary", "Montreal"]

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M")

for city in cities:
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    data = response.json()
    current = data["current_condition"][0]
    
    temp = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    conditions = current["weatherDesc"][0]["value"]
    wind = current["windspeedKmph"]
    uv = current["uvIndex"]
    
    cursor.execute("""
        INSERT INTO weather (city, date, time, temp_c, feels_like_c, conditions, wind_kmph, uv_index)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (city, date, time, temp, feels_like, conditions, wind, uv))

conn.commit()
print("Weather data stored.")

df = pd.read_sql_query("SELECT * FROM weather", conn)
print(df)

print("\n=== COLDEST CITY RIGHT NOW ===")
print(df.sort_values("temp_c").iloc[0][["city", "temp_c", "conditions"]])

print("\n=== AVERAGE TEMP ACROSS CITIES ===")
print(df["temp_c"].mean())

print("\n=== CITY SUMMARY ===")
print(df[["city", "temp_c", "feels_like_c", "conditions", "wind_kmph"]].sort_values("temp_c"))

df[["city", "temp_c", "feels_like_c", "conditions", "wind_kmph", "uv_index"]].sort_values("temp_c").to_csv("weather_report.csv", index=False)
print("Report exported to weather_report.csv")