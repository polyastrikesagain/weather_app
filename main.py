import sys
from prettytable import PrettyTable
from weatherapi import WeatherApi

#to ensure the input is correct and the location is found
print("Choose country and city to show the weather")
while True:
    country = input("Enter country: ")
    city = input("Enter city: ")
    app = WeatherApi(country, city)
    location_coords = app.get_coords()
    if not location_coords:
        print(f"We found nothing :( Are you sure {city}, {country} is a correct location?")
        print("Contact us if you think we're wrong.")
        if input("Want to continue? Press [y] if so. | ").lower() != "y":
            print("Buh-bye now!")
            sys.exit()
    else:
        break

#to choose a location if there's many of them by the same name
if len(location_coords) > 1:
    print(location_coords)
    print(f"Many different locations were found by the name {city}, {country}:")
    for i in range(len(location_coords)):
        print(f"[{i+1}]. {location_coords[i]['name']}")
    while True:
        number = input("Select the location's number: ")
        try:
            number = int(number)
        except ValueError:
            print("You have to input a number. Let's try again")
        if isinstance(number, int):
            if number > len(location_coords):
                print(f"You have to input a number of the location, and there's only {len(location_coords)} of them. Let's try again")
            elif number < 0:
                print(f"The number should be positive, silly! Let's try again")
            else:
                break
    chosen_location = location_coords[number - 1]
else:
    chosen_location = location_coords[0]

app.set_coords(chosen_location['lat'], chosen_location['lon'])

print("Choose the forecast's number:")
print("[1]. Current weather")
print("[2]. Weather tomorrow")
print("[3]. Next week forecast")
while True:
    number = input("Enter your choice: ")
    try:
        number = int(number)
    except ValueError:
        print("You have to input a number. Let's try again")
    if isinstance(number, int):
        if not (1 <= number <= 3):
            print("Only three options are available to see the weather. Let's try again")
        else:
            break

forecast_table = PrettyTable()
forecast_table.hrules = True
match number:
    case 1:
        forecast = app.get_weather(current=True)
        forecast_table.field_names = forecast[0]
        forecast = forecast[1:]
    case 2:
        forecast = app.get_weather(current=False)[:] #да такой же дейлик как и неделька, только срезик на каждую строку
        forecast_table.header = False
    case 3:
        forecast = app.get_weather(current=False)
        forecast_table.header = False



for row in forecast:
    forecast_table.add_row(row)
print(forecast_table)


##NOTES
##1.    FIX CASE 2 TO ONLY SHOW THE TOMORROWS PROGNOSIS

##2.    ADD CACHE FILE WITH COORDINATES THAT THE USER CHOSE WHEN EXECUTING THE CODE PREVIOUSLY
##WITH AN OPTION TO MAKE A NEW SEARCH

##3.    ADD UNITS!