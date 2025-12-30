# weather_service.py
# Fetch current or forecast weather based on time window

import requests

API_KEY = "362927f85081412182c152653253012"


def get_weather_data(query, time_window):
    url = "https://api.weatherapi.com/v1/forecast.json"

    # Decide forecast hour
    hour_index = 0
    if time_window == "Next 3 Hours":
        hour_index = 3
    elif time_window == "Next 6 Hours":
        hour_index = 6
    elif time_window == "Next Morning":
        hour_index = 9

    params = {
        "key": API_KEY,
        "q": query,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    # SAFETY CHECK
    if "forecast" not in data:
        return None

    forecast_hour = data["forecast"]["forecastday"][0]["hour"][hour_index]

    return {
        "temperature": forecast_hour.get("temp_c"),
        "humidity": forecast_hour.get("humidity"),
        "wind_speed": forecast_hour.get("wind_kph"),
        "rainfall": forecast_hour.get("precip_mm"),

        "city": data["location"].get("name"),
        "region": data["location"].get("region"),
        "country": data["location"].get("country")
    }


    return weather
