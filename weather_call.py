import requests
import json
from api_keys import OPENWEATHER_API_KEY
from f1_season_call import race_info

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
print(response.status_code)

res_dict = response.json()
#print(res_dict)["precipitation"]
#print(res_dict["weather"][0]["main"])
print(json.dumps(res_dict, sort_keys=True, indent=4))