## Overview
The WeatherData class in weather_data.py provides methods to fetch weather data from the API 
and compute statistics.

Running the main.py file will also call the methods created for the WeatherData class in the 
weather_data.py file to print the average, minimum, and maximum values 
for temperature, wind speed, and precipitation for July 7th 2020-2024

Unittest was used to ensure correctness in the test.py file, including tests 
to verify that a WeatherData object initialized correctly with the provided latitude, longitude, and date,
check that the API fetches keys as expected, and ensure that a record is correctly inserted into the database, 
retrieves it, and verifies its value

## Weather data analysis and storage
This project fetches historical data from a weather API for a specific location and day over a five-year period,
calculates some weather statistics and stores them in a SQLite database using SQLAlchemy 

## Usage
Running the script from main.py will retrieve the weather data, compute the stats, 
and store the data in the database called weather.db.
The stored data can be viewed by querying the database directly. 
