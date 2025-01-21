import requests

# WeatherData class with location, date, wind, precip, and temp instance variables
class WeatherData:
    def __init__(self, latitude, longitude, year, month, day):
# Location and date instance attributes
        self.latitude = latitude
        self.longitude = longitude
        self.year = year
        self.month = month
        self.day = day
        self.api_url = "https://archive-api.open-meteo.com/v1/archive"

# Five-year weather attributes
        self.five_year_avg_temp = None
        self.five_year_min_temp = None
        self.five_year_max_temp = None
        self.five_year_avg_wind_speed = None
        self.five_year_min_wind_speed = None
        self.five_year_max_wind_speed = None
        self.five_year_sum_precip = None
        self.five_year_min_precip = None
        self.five_year_max_precip = None

# Get request to Open-Meteo API with parameters for specified date
    def get_weather_data(self, offset):
        date = f"{self.year - offset}-{self.month:02}-{self.day:02}"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": date,
            "end_date": date,
            "daily": [ "temperature_2m_max", "precipitation_sum",
                      "wind_speed_10m_max"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/Los_Angeles",
        }
# Returns JSON response if request was successful, raises error if unsuccessful
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Error fetching data: {response.status_code}")

# Methods to calculate min, max, and average values for the five-year period
    # Section C2 method to calculate mean temperature
    def set_mean_temp(self, temperatures):
        self.five_year_avg_temp = sum(temperatures) / len(temperatures)

    def set_min_temp(self, temperatures):
        self.five_year_min_temp = min(temperatures)

    def set_max_temp(self, temperatures):
        self.five_year_max_temp = max(temperatures)

    def set_avg_wind_speed(self, wind_speeds):
        self.five_year_avg_wind_speed = sum(wind_speeds) / len(wind_speeds)

    def set_min_wind_speed(self, wind_speeds):
        self.five_year_min_wind_speed = min(wind_speeds)

    # Section C2 method to calculate max wind_speed
    def set_max_wind_speed(self, wind_speeds):
        self.five_year_max_wind_speed = max(wind_speeds)

    # Section C2 method to calculate sum precipitation
    def set_sum_precip(self, precipitations):
        self.five_year_sum_precip = sum(precipitations)

    def set_min_precip(self, precipitations):
        self.five_year_min_precip = min(precipitations)

    def set_max_precip(self, precipitations):
        self.five_year_max_precip = max(precipitations)



