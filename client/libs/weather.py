import requests

from client.libs.reader import WeatherReader
from client.libs.registry import register_reader

API_ENDPOINT = "http://0.0.0.0:8000/api/v1/weather/upload"


def upload(weather_xls):
    """
    upload weather data to external API.
    """
    reader = WeatherReader(weather_xls)
    reader.read()

    for record in reader.data:
        response = requests.post(API_ENDPOINT, data=record)

        if response.status_code == 201:
            print("added: ", record)
            register_reader(record['row_number'])

