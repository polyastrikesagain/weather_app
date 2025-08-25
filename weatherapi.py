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
        self.set_coords(response[0]['lat'], response[0]['lon'])
        return self.lat, self.lon