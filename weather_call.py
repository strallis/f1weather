import requests
import json
import os

from race_call import get_race_info

API_KEY = os.environ.get('WEATHER_API_KEY')

def get_weather_for_next_race():
    """
    Returns a dictionary with the current weather information for the next race
    """
    race_info = get_race_info()

    COORDINATES = race_info["race_location"]
    UNITS = 'metric'
    QUERY = 'https://api.openweathermap.org/data/3.0/onecall'

    parameters = {
        "lat": COORDINATES["lat"],
        "lon": COORDINATES["long"],
        "appid": API_KEY,
        "units": UNITS
    }

    response = requests.get(QUERY, parameters).json()

    weather_info = {
        "current_weather_main": response["current"]["weather"][0]["main"],
        "current_weather_description": response["current"]["weather"][0]["description"],
        "current_weather_temp": response["current"]["temp"],
        "current_weather_feels_like": response["current"]["feels_like"],
        "current_weather_humidity": response["current"]["humidity"],
        "current_weather_wind_speed": response["current"]["wind_speed"],
        "is_it_raining": True if response["current"]["weather"][0]["main"] in ["Rain","Drizzle","Thunderstorm","Snow"] else False,
        "weather_icon_url": "http://openweathermap.org/img/wn/" + response["current"]["weather"][0]["icon"] + ".png"
    }

    #print(json.dumps(weather_info, indent=2))

    return weather_info

