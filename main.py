from weather_data import WeatherData
from weather_db import WeatherDataDB, Session

# Initialize WeatherData instance
weather = WeatherData(latitude=36.175, longitude=-115.1372, year=2024, month=7, day=7)

# Initialize lists to hold the weather data for the last 5 years
temperatures = []
wind_speeds = []
precipitations = []

# Creates the session
session = Session()

# Loop to fetch and store yearly data for the last 5 years
for offset in range(5):
    year_data = weather.get_weather_data(offset)
    print(year_data)  #debugging: prints each year's data to verify
    temp = year_data["daily"]["temperature_2m_max"][0]
    wind = year_data["daily"]["wind_speed_10m_max"][0]
    precip = year_data["daily"]["precipitation_sum"][0]

# Weather data is added to their respective lists
    temperatures.append(temp)
    wind_speeds.append(wind)
    precipitations.append(precip)

print("All yearly data has been successfully added to the database.")

## Calls to calculate mean, max , min temp, precip, and wind speeds and print results
weather.set_mean_temp(temperatures)
print(f"Five-year Average Temperature: {weather.five_year_avg_temp:.2f} fahrenheit")

# Calls the min and max temps method and display their results
weather.set_min_temp(temperatures)
print(f"Five-year Min Temperature: {weather.five_year_min_temp} fahrenheit")
weather.set_max_temp(temperatures)
print(f"Five-year Max Temperature: {weather.five_year_max_temp}fahrenheit")

# Calls the average wind speed and display results
weather.set_avg_wind_speed(wind_speeds)
print(f"Five-year Average Wind Speed: {weather.five_year_avg_wind_speed:.2f} mph")

# Calls the min and max wind speeds and display their results
weather.set_min_wind_speed(wind_speeds)
print(f"Five-year Min Wind Speed: {weather.five_year_min_wind_speed} mph")
weather.set_max_wind_speed(wind_speeds)
print(f"Five-year Max Wind Speed: {weather.five_year_max_wind_speed} mph")

# Calls the sum precip and display results
weather.set_sum_precip(precipitations)
print(f"Five-year Total Precipitation: {weather.five_year_sum_precip} inches")

# Calls the min and max precip methods and display their results
weather.set_min_precip(precipitations)
print(f"Five-year Min Precipitation: {weather.five_year_min_precip} inches")

weather.set_max_precip(precipitations)
print(f"Five-year Max Precipitation: {weather.five_year_max_precip} inches")

# Stores the computed data for this specific year into the database
db_weather = WeatherDataDB(
    year=weather.year,
    month=weather.month,
    day=weather.day,
    latitude=weather.latitude,
    longitude=weather.longitude,
    mean_temp=weather.five_year_avg_temp,
    min_temp=weather.five_year_min_temp,
    max_temp=weather.five_year_max_temp,
    avg_wind_speed=weather.five_year_avg_wind_speed,
    min_wind_speed=weather.five_year_min_wind_speed,
    max_wind_speed=weather.five_year_max_wind_speed,
    sum_precip=weather.five_year_sum_precip,
    min_precip=weather.five_year_min_precip,
    max_precip=weather.five_year_max_precip,
    )
session.add(db_weather)
# Commits changes and populates the database
session.commit()


# Query the database for all records to confirm insertion
for result in session.query(WeatherDataDB).all():
    print("--------------------------------------------")
    print(f"ID: {result.id}")
    print(f"Year: {result.year}, Month: {result.month}, Day: {result.day}")
    print(f"latitude: {result.latitude}, longitude: {result.longitude}")
    print(f"Avg Temp: {result.mean_temp:.2f}")
    print(f"Min Temp: {result.min_temp:.2f}")
    print(f"Max Temp: {result.max_temp:.2f}")
    print(f"Avg Wind Speed: {result.avg_wind_speed:.2f}")
    print(f"Min Wind Speed: {result.min_wind_speed:.2f}")
    print(f"Max Wind Speed: {result.max_wind_speed:.2f}")
    print(f"Sum Precip: {result.sum_precip}")
    print(f"Min Precip: {result.min_precip}")
    print(f"Max Precip: {result.max_precip}")

# Closes the database
session.close()
