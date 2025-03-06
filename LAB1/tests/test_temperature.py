import unittest
from src.temperature import TemperatureConverter


class TemperatureConverterTest(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(50), 122)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(-10), 14)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(50), 10)
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(104), 40)
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(-22), -30)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(25), 298.15)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(200), 473.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(310.15), 37)
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(500), 226.85)


if __name__ == "__main__":
    unittest.main()