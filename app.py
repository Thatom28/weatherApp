from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather_data(city):
    """Fetch weather data for a given city."""
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route("/")
def index():
    # Get Cape Town weather by default
    city = "Cape Town"
    weather_data = get_weather_data(city)

    if weather_data:
        weather = {
            "city": weather_data["location"]["name"],
            "temperature": weather_data["current"]["temp_c"],
            "description": weather_data["current"]["condition"]["text"],
            "icon": weather_data["current"]["condition"]["icon"],
            "humidity": weather_data["current"]["humidity"],
            "wind": weather_data["current"]["wind_kph"],
        }
        return render_template("index.html", weather=weather)
    else:
        error = "Weather data for Cape Town is not available"
        return render_template("index.html", error=error)


@app.route("/weather", methods=["POST"])
def get_weather():
    city = request.form.get("city")
    print(f"City received: {city}")

    if city:
        weather_data = get_weather_data(city)

        if weather_data:
            weather = {
                "city": weather_data["location"]["name"],
                "temperature": weather_data["current"]["temp_c"],
                "description": weather_data["current"]["condition"]["text"],
                "icon": weather_data["current"]["condition"]["icon"],
                "humidity": weather_data["current"]["humidity"],
                "wind": weather_data["current"]["wind_kph"],
            }
            return render_template("index.html", weather=weather)
        else:
            error = "City not found"
            return render_template("index.html", error=error)
    else:
        error = "Please enter a city name"
        return render_template("index.html", error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
