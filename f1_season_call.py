import requests
import json
from datetime import datetime

def f1_api_call():
    query = 'https://ergast.com/api/f1/2021/next.json'

    response = requests.get(query)
    #print(response.status_code)

    res_dict = response.json()
    next_race = res_dict["MRData"]["RaceTable"]["Races"][0]
    print(json.dumps(next_race, sort_keys=True, indent=4))
    return next_race

def race_info_getter(next_race):
    # Time to race!
    race_datetime = next_race["date"] + " " + next_race["time"].strip("Z")
    race_datetime = datetime.strptime(race_datetime, "%Y-%m-%d %H:%M:%S")

    time_to_race = str(race_datetime - datetime.utcnow()).split(".")[0]

    # Name of race
    race_name = next_race["raceName"]

    # The location of the race in latitude, longitude, country and locality
    race_location = next_race["Circuit"]["Location"]

    race_info =  {"time_to_race": time_to_race, "race_name": race_name, "race_location": race_location}
    print(race_info)
    return race_info
