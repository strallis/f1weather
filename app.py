from flask import Flask, render_template
from weather_call import weather_info, race_info

app = Flask(__name__)

@app.route('/')
def index():
    data = {"race": race_info, "weather": weather_info}
    #print(race_info)
    #print(weather_info)
    return render_template("front.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)