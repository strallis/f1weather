import requests
import json
from api_keys import OPENWEATHER_API_KEY
import f1_season_call

next_race = f1_season_call.f1_api_call()
race_info = f1_season_call.race_info_getter(next_race)
#print(race_info)
API_KEY = OPENWEATHER_API_KEY
COORDINATES = race_info["race_location"]
UNITS = 'metric'
QUERY = 'https://api.openweathermap.org/data/2.5/weather'

parameters = {
    "lat": COORDINATES["lat"],
    "lon": COORDINATES["long"],
    #"q": "Imola",
    "appid": API_KEY,
    "units": UNITS
}

response = requests.get(QUERY, parameters)
#print(response.status_code)

weather_info = response.json()
#print(weather_info)
#print(res_dict["weather"][0]["main"])
print(json.dumps(weather_info, sort_keys=True, indent=4))