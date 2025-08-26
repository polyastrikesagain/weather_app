import requests, os
from dotenv import load_dotenv


class WeatherApi:
    def __init__(self, country, city):
        load_dotenv(dotenv_path='env_files/geocoding_api_key.env', verbose=True)
        self.geocoding_api_key = os.getenv("GEOCODING_API_KEY")
        self.country = country
        self.city = city
        self.lat, self.lon = None, None

    def set_coords(self, lat, lon):
        self.lat, self.lon = lat, lon

    def get_coords(self):
        json_query = f"https://geocode.maps.co/search?city={self.city}&country={self.country}&api_key={self.geocoding_api_key}"
        response = requests.get(json_query).json()
        return [{'name' : res['display_name'], 'lat' : res['lat'], 'lon' : res['lon']} for res in response]

    def get_weather(self, lat, lon):
        json_query = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,wind_speed_10m&timezone=auto&wind_speed_unit=ms"
        response = requests.get(json_query).json()
        return response