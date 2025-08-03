import requests
import sys

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    try:
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unable to fetch weather data.')}")
            return

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        location = input("Enter city or ZIP code: ")
    else:
        location = " ".join(sys.argv[1:])
    get_weather(location)
