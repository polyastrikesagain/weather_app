from weatherapi import WeatherApi

print("Choose country and city to show the weather")
while True:
    country = input("Enter country: ")
    city = input("Enter city: ")
    app = WeatherApi(country, city)
    result = app.get_weather(*app.get_coords())
    if not result:
        print("No result: make sure you're inputting correct country and city. Let's try again")
    else:
        break
print(result['current'])