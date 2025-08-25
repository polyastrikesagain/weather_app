from weatherapi import WeatherApi

app = WeatherApi("Russia", "Saint-Petersburg")
data = app.get_coords()
print(data)