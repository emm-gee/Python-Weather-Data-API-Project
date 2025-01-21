import unittest
from weather_data import WeatherData
from weather_db import WeatherDataDB, Session


class TestWeatherApp(unittest.TestCase):
# Verifies that a WeatherData object initialized correctly with the provided latitude, longitude, and date
    def test_weather_initialization(self):
        weather = WeatherData(latitude=36.175, longitude=-115.1372, year=2024, month=7, day=7)
        self.assertEqual(weather.latitude, 36.175)
        self.assertEqual(weather.longitude, -115.1372)
        self.assertEqual(weather.year, 2024)
        self.assertEqual(weather.month, 7)
        self.assertEqual(weather.day, 7)


# Checks that the API fetches keys as expected
    def test_weather_api_response(self):
        weather = WeatherData(latitude=36.175, longitude=-115.1372, year=2024, month=7, day=7)
        response = weather.get_weather_data(offset=0)
        self.assertIn("daily", response)
        self.assertIn("temperature_2m_max", response["daily"])
        self.assertIn("wind_speed_10m_max", response["daily"])
        self.assertIn("precipitation_sum", response["daily"])

# Ensures that a record is correctly inserted into the database, retrieves it, and verifies its value
    def test_database_record_insertion(self):
        session = Session()
        new_entry = WeatherDataDB(
            year=2024, month=7, day=7, latitude=36.175, longitude=-115.1372,
            mean_temp=108.96, min_temp=104.2, max_temp=117.1,
            avg_wind_speed=16.78, min_wind_speed=12.8, max_wind_speed=22.6,
            sum_precip=0.0, min_precip=0.0, max_precip=0.0
    )
        session.add(new_entry)
        session.commit()

        result = session.query(WeatherDataDB).filter_by(year=2024).first()

        self.assertEqual(result.year, 2024)
        self.assertEqual(result.month, 7)
        self.assertAlmostEqual(result.mean_temp, 108.96, places=2)

        session.query(WeatherDataDB).delete()
        session.commit()
        session.close()


if __name__ == '__main__':
    unittest.main()
