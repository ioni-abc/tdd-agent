import unittest


import unittest

class AgentTest_set_city(unittest.TestCase):

    def test_set_city_1(self):
        weather_system = WeatherSystem('New York')
        weather_system.set_city('Beijing')
        self.assertEqual(weather_system.city, 'Beijing')

    def test_set_city_2(self):
        weather_system = WeatherSystem('New York')
        result = weather_system.set_city('Beijing')
        self.assertIsNone(result)

    def test_set_city_3(self):
        weather_system = WeatherSystem('New York')
        weather_system.set_city('Beijing')
        weather_system.set_city('Paris')
        self.assertEqual(weather_system.city, 'Paris')

    def test_set_city_4(self):
        weather_system = WeatherSystem('New York')
        weather_system.set_city('Beijing')
        self.assertNotEqual(weather_system.city, 'New York')

    def test_set_city_5(self):
        weather_system = WeatherSystem('New York')
        weather_system.set_city('Los Angeles')
        self.assertEqual(weather_system.city, 'Los Angeles')

import unittest

class AgentTest_celsius_to_fahrenheit(unittest.TestCase):

    def test_celsius_to_fahrenheit_1(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 27
        self.assertAlmostEqual(weather_system.celsius_to_fahrenheit(), 80.6)

    def test_celsius_to_fahrenheit_2(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 0
        self.assertAlmostEqual(weather_system.celsius_to_fahrenheit(), 32)

    def test_celsius_to_fahrenheit_3(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 100
        self.assertAlmostEqual(weather_system.celsius_to_fahrenheit(), 212)

    def test_celsius_to_fahrenheit_4(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = -40
        self.assertAlmostEqual(weather_system.celsius_to_fahrenheit(), -40)

    def test_celsius_to_fahrenheit_5(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 0
        result = weather_system.celsius_to_fahrenheit()
        self.assertIsInstance(result, float)

import unittest

class AgentTest_fahrenheit_to_celsius(unittest.TestCase):

    def test_fahrenheit_to_celsius_1(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 80.6
        self.assertAlmostEqual(weather_system.fahrenheit_to_celsius(), 26.999999999999996)

    def test_fahrenheit_to_celsius_2(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 32
        self.assertAlmostEqual(weather_system.fahrenheit_to_celsius(), 0)

    def test_fahrenheit_to_celsius_3(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 212
        self.assertAlmostEqual(weather_system.fahrenheit_to_celsius(), 100)

    def test_fahrenheit_to_celsius_4(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = -40
        self.assertAlmostEqual(weather_system.fahrenheit_to_celsius(), -40)

    def test_fahrenheit_to_celsius_5(self):
        weather_system = WeatherSystem('New York')
        weather_system.temperature = 32
        result = weather_system.fahrenheit_to_celsius()
        self.assertIsInstance(result, float)

class AgentTest_query(unittest.TestCase):

    def test_query_1(self):
        weather_system = WeatherSystem('New York')
        weather_list = {
            'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'},
            'Beijing': {'weather': 'cloudy', 'temperature': 23, 'temperature units': 'celsius'}
        }
        self.assertEqual(weather_system.query(weather_list), (27, 'sunny'))

    def test_query_2(self):
        weather_system = WeatherSystem('New York')
        weather_system.set_city('Beijing')
        weather_list = {
            'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'},
            'Beijing': {'weather': 'cloudy', 'temperature': 23, 'temperature units': 'celsius'}
        }
        self.assertEqual(weather_system.query(weather_list), (23, 'cloudy'))

    def test_query_3(self):
        weather_system = WeatherSystem('New York')
        weather_list = {
            'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'}
        }
        temperature, weather = weather_system.query(weather_list, 'fahrenheit')
        self.assertAlmostEqual(temperature, 80.6)
        self.assertEqual(weather, 'sunny')

    def test_query_4(self):
        weather_system = WeatherSystem('New York')
        weather_list = {
            'New York': {'weather': 'sunny', 'temperature': 80.6, 'temperature units': 'fahrenheit'}
        }
        temperature, weather = weather_system.query(weather_list, 'celsius')
        self.assertAlmostEqual(temperature, 27)
        self.assertEqual(weather, 'sunny')

    def test_query_5(self):
        weather_system = WeatherSystem('New York')
        weather_list = {
            'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'}
        }
        result = weather_system.query(weather_list, 'celsius')
        self.assertEqual(result, (27, 'sunny'))