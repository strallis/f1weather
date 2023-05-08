from flask import Flask, render_template
import threading
import time
from datetime import datetime, timezone
from weather_call import get_weather_for_next_race
from race_call import get_race_info

app = Flask(__name__)

time_to_race_formatted = None

def update_time_to_race():
    global time_to_race_formatted
    while True:
        # Date time of race
        race_datetime = get_race_info()["race_datetime"]

        # Calculate the time to race here and update the global variable
        time_to_race = race_datetime - datetime.now(timezone.utc)
        seconds = time_to_race.total_seconds()
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        time_to_race_formatted = f"{int(days)} days {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"

        # Sleep for a shorter duration between updates
        time.sleep(0.1) # Sleep for 0.1 seconds

@app.route('/')
def index():
    global time_to_race_formatted

    race_info = get_race_info()
    weather_info = get_weather_for_next_race()

    data = {"race": race_info,
             "weather": weather_info}
    #print(data)
    #print(data["race"])
    #print(data["weather"])
             
    return render_template("front.html", data=data, time_to_race=time_to_race_formatted)


if __name__ == "__main__":
    # Start the background thread to update the time to race
    thread = threading.Thread(target=update_time_to_race)
    thread.daemon = True
    thread.start()
    app.run(debug=True)
