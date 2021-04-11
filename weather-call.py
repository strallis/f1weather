import requests
from api_keys import *

API_KEY = OPENWEATHER_API_KEY
CITY = 'Bergshamra'
UNITS = 'metric'
query = 'https://api.openweathermap.org/data/2.5/weather'

parameters = {
    "q": CITY,
    "appid": API_KEY,
    "units": UNITS
}
response = requests.get(query, parameters)
print(response.status_code)

res_dict = response.json()
print(res_dict)
print(res_dict["weather"][0]["main"])