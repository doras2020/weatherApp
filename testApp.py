from validations import TestsValidations
from weatherRequests import weatherPage as wp
import unittest
import variablesFile

class BaseTestCase(TestsValidations):

    def test_current_weather(self):
        weatherP = wp()
        # Validate response.status_code is 200 and return response
        current_weather = self.valiate_and_parse(
            weatherP.current_weather_request(variablesFile.zipcode, variablesFile.countrycode))

        #Extract the kelvin temperature and turn in to Celsius
        temp_kelvin = current_weather['main']['temp']
        temp_celsius = round((float(temp_kelvin) - 273.15), 2)

        #Verify city and country names are as expected
        self.assertEqual(current_weather['name'], variablesFile.city)
        self.assertEqual(current_weather['sys']['country'], variablesFile.countrycode)

        #Print temperature
        print(f"The current temperature in {variablesFile.city} is : {str(temp_celsius)} degrees Celsius")

if __name__ == '__main__':
    unittest.main()

