# Command-Line Weather App

A simple Python command-line tool to fetch and display current weather information for any city or ZIP code using the OpenWeatherMap API.

## Features
- Fetches **temperature**, **humidity**, and **weather conditions**
- Supports **city names** and **ZIP codes**
- Uses **OpenWeatherMap** (free API)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-cli-app.git
cd weather-cli-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your API key
- Go to [OpenWeatherMap](https://openweathermap.org/api)
- Sign up and generate an API key
- Replace `YOUR_API_KEY` in `weather_app.py` with your key

## Usage
```bash
# Run interactively
python weather_app.py
# OR pass city/ZIP as argument
python weather_app.py London
python weather_app.py "New York"
python weather_app.py 10001
```

## Example Output
```
Weather in London, GB:
Temperature: 18°C
Humidity: 65%
Condition: Clear sky
```

## License
MIT License
