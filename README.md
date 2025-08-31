# Table of contents
- [What is it?](#what-is-it)
- [What does it do?](#what-does-it-do)
    - [Description of some parameters](#description-of-some-parameters)
    - [Used units](#used-units)
- [Used libraries](#used-libraries)
- [Credits](#credits)

## What is it?
A simple Python-based console app for looking up weather using APIs and working with JSONs as a study project of mine. It's up to you to decide whether it's good or bad that I didn't use generative AI for this, but it is a study project after all.

## What does it do?
You get asked the name of the location to look up the coordinates through Geocoding API (https://geocode.maps.co/), for the 'city' you can try entering a city, a municipality in your city or any locality/settlement. The case doesn't matter and in a lot of ways shortened names can be accepted by Geocoding API as well.
If something goes wrong, you can try the search again.
If the location is found, but there is several of them that meet the location name you entered (for example, Otradnoe, Russia/Россия, Отрадное is a name that matches several locations in Russia in different parts of it), there will be a list of all available locations to choose from.
Then you can select:
[1] Current weather (Forecast time, type of weather, temperature, apparent temperature (what it feels like), relative humidity, wind speed, UV index)
[2] Tomorrow's weather (Forecast date, type of weather, highest temperature, lowest temperature, average temperature, precipitation sum, max wind speed, UV index)
[3] Full week forecast (Forecast date, type of weather, highest temperature, lowest temperature, average temperature, precipitation sum, max wind speed, UV index)
The selected parameters will call a query to the OpenMeteo API (https://open-meteo.com/) and then you will see the forecast for that location.

If there's no cache file in the folder of the project, it will be created after you succesfully choose a location, and if you use it afterwards, you will be shown this location and asked to either:
[1] See the forecast for the saved location
[2] See the forecast for the other location without deleting the saved data
[3] Delete the saved data

### Description of some parameters
- Type of weather — a description of the weather based on WMO codes that is pulled from the descriptions.json file, all credits for descriptions.json go to stellasphere (https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c)
- Precipitation sum — the sum value of precipitation during the period, including rain, snow, etc.
- UV index — the value of ultraviolet radiation index (for more information about UV index, please refer to WHO recommendations: https://www.who.int/news-room/questions-and-answers/item/radiation-the-ultraviolet-(uv)-index)

### Used units
Right now the units are predetermined this way:
- Temperature: Celcius
- Wind speed: m/s
Later there will be a possibility to change the units.

## Used libraries
1. requests
2. json
3. dotenv
4. os
5. sys
6. prettytable

## Credits
1. OpenMeteo API: https://open-meteo.com/
2. Geocoding API: https://geocode.maps.co/
3. descriptions.json by stellasphere https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c
