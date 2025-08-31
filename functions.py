import json

def cache_locations(name, lat, lon):
    data = {"name": name, "lat": lat, "lon": lon}
    with open("cache.json", "w") as cache:
        json.dump(data, cache)

