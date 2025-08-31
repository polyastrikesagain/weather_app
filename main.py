import json
import sys, os
from prettytable import PrettyTable
from weatherapi import WeatherApi
from functions import cache_locations

#to ensure the input is correct and the location is found
print("Choose country and city to show the weather")

ignore_cache = False

while True:
    if os.path.exists('cache.json') and not ignore_cache:
        with open('cache.json', 'r') as cache:
            data = json.load(cache)
            location = data['name']
            location_coords = [{'lat' : data['lat'], 'lon' : data['lon']}]
        while True:
            print(f"\nWe have found your previous weather search regarding {location}.")
            print("Would you like to continue this search?")
            print("[1]. Yes")
            print("[2]. I want to make a new search but save the previous one")
            print("[3]. I want to delete my previous search")
            number = input("Enter your choice: ")
            match number:
                case '1':
                    app = WeatherApi()
                    break
                case '2':
                    app = WeatherApi()
                    ignore_cache = True
                    break
                case '3':
                    os.remove('cache.json')
                    break
                case _:
                    print("Wrong input. Let's try again")
                    continue
        if os.path.exists('cache.json') and not ignore_cache:
            break
    else:
        country = input("\nEnter country: ")
        city = input("Enter city: ")
        app = WeatherApi()
        location_coords = app.get_coords(country, city)
        print(location_coords)
        if not location_coords:
            print(f"\nWe found nothing :( Are you sure {city}, {country} is a correct location?")
            print("Contact us if you think we're wrong.")
            if input("Want to continue? Press [y] if so. | ").lower() != "y":
                print("Buh-bye now!")
                sys.exit()
        else:
            break

#to choose a location if there's many of them by the same name
if len(location_coords) > 1:
    print(f"\nMany different locations were found by the name {city}, {country}:")
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

if not os.path.exists('cache.json'):
    cache_locations(**chosen_location)

app.set_coords(chosen_location['lat'], chosen_location['lon'])

print("\nChoose the forecast's number:")
print("[1]. Current weather")
print("[2]. Weather tomorrow")
print("[3]. Full week forecast")
while True:
    number = input("Enter your choice: ")
    try:
        number = int(number)
    except ValueError:
        print("You have to input a number. Let's try again")
    if isinstance(number, int):
        if not (1 <= number <= 3):
            print("Only three options are available to see the weather. Let's try again\n")
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
        forecast = [(days[0], days[2]) for days in app.get_weather(current=False)]
        forecast_table.header = False
    case 3:
        forecast = app.get_weather(current=False)
        forecast_table.header = False



for row in forecast:
    forecast_table.add_row(row)
print("\n", forecast_table,sep="")


##NOTES
##1.    FIX CASE 2 TO ONLY SHOW THE TOMORROWS PROGNOSIS | READY

##2.    ADD CACHE FILE WITH COORDINATES THAT THE USER CHOSE WHEN EXECUTING THE CODE PREVIOUSLY
##WITH AN OPTION TO MAKE A NEW SEARCH | READY

##3.    ADD UNITS! | READY

###IMPORTANT
##no LLMs or AI were used since the goal of this project was to learn to code, not to copy-paste
###