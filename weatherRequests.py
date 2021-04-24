import requests

class weatherPage:
    # Get the response and return it
    def current_weather_request(self, zipcode, countrycode):

        url = f"https://community-open-weather-map.p.rapidapi.com/weather?zip={zipcode},{countrycode}"

        headers = {
            'x-rapidapi-key': "e52a9b5c64msh1f1b677ce59a27cp1c520ajsn5b52e4ccd06d",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        return response