import requests
import json
from datetime import datetime

def get_race_info() -> dict:
    next_race = f1_api_call()

    # Date time of race
    race_datetime = datetime.strptime(next_race["date"] + next_race["time"], "%Y-%m-%d%H:%M:%S%z")

    # Name of race
    race_name = next_race["raceName"]

    # The location of the race in latitude, longitude, country and locality
    race_location = next_race["Circuit"]["Location"]

    race_info =  {"race_datetime": race_datetime, "race_name": race_name, "race_location": race_location}
    #print(race_info)
    return race_info

def f1_api_call() -> dict:
    query = 'https://ergast.com/api/f1/2023/next.json'
    response = requests.get(query)
    #print(response.status_code)

    res_dict = response.json()
    next_race = res_dict["MRData"]["RaceTable"]["Races"][0]
    #print(json.dumps(next_race, sort_keys=True, indent=4))
    return next_race
