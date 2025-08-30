import requests, os
from dotenv import load_dotenv
from json import load

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
        return [{'name': res['display_name'], 'lat': res['lat'], 'lon': res['lon']} for res in response]

    def get_weather(self, current=False):
        if current:
            parameters = {'time': 'Forecast date',
                          'is_day': 'Time of day',
                          'weather_code': 'Weather',
                          'temperature_2m': 'Temperature',
                          'apparent_temperature': 'Feels like',
                          'relative_humidity_2m': 'Relative humidity',
                          'wind_speed_10m': 'Wind speed',
                          'uv_index': 'UV index'}
            fetch = "current"
        else:
            parameters = {'time': 'Forecast date',
                          'weather_code': 'Weather',
                          'temperature_2m_max': 'Highest temperature',
                          'temperature_2m_min': 'Lowest temperature',
                          'temperature_2m_mean': 'Average',
                          'precipitation_sum': 'Precipitation sum',
                          'wind_speed_10m_max': 'Wind speed',
                          'uv_index_max': 'UV index'}
            fetch = "daily"
        forecast_parameters = f"&{fetch}={",".join(list(parameters)[1:])}"
        json_query = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}" + forecast_parameters + "&timezone=auto&wind_speed_unit=ms"
        response = requests.get(json_query).json()

        units = response[f'{fetch}_units']
        response = response[fetch]

        # just for pulling up the weather description from the .json file
        day_or_night_json = "day"
        if 'is_day' in parameters:
            if not (parameters['is_day'] or fetch == 'daily'):
                day_or_night_json = "night"
            del parameters['is_day']

        result = list()
        for key in parameters:
            if key == 'weather_code':
                if not isinstance(response[key], list):
                    response[key] = [response[key]]
                with open('descriptions.json') as weather_codes_json:
                    weather_codes_json = load(weather_codes_json)
                    for i in range(len(response[key])):
                        response[key][i] = weather_codes_json[str(response[key][i])][day_or_night_json][
                            "description"]
            elif 'temperature' in key or 'humidity' in key or 'speed' in key or 'precipitation' in key:
                if isinstance(response[key], list):
                    response[key] = [f"{response[key][i]}{units[key]}" for i in range(len(response[key]))]
                else:
                    response[key] = f"{response[key]}{units[key]}"

            result.append((parameters[key], *response[key]) if isinstance(response[key], list) else (parameters[key], response[key]))
        return result

###IMPORTANT
##no LLMs or AI were used since the goal of this project was to learn to code, not to copy-paste
###