# API_pandas_SQL_project
My most technically comprehensive project to date, combining APIs, pandas, and SQL into a single automated pipeline.

## What It Does

Fetches live weather data for multiple Canadian cities via API, stores results in a SQLite database, and generates analytical reports including:

- Current conditions per city (temperature, wind, UV index)
- Coldest city ranking
- Average temperature across all cities
- Full city summary sorted by temperature
- CSV report export for further use

## Skills Demonstrated

- Live API calls with requests
- SQLite database creation and storage
- pandas analysis: sorting, filtering, calculated columns
- pd.read_sql_query connecting SQL and pandas
- Automated CSV export
- Full data pipeline: API → SQL → pandas → CSV

## How to Run

1. Run `python ex14_capstone.py`
2. `weather_cities.db` and `weather_report.csv` will be generated automatically

## Tech Stack

- Python 3
- requests
- SQLite3 (built-in)
- pandas
