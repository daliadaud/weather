import requests
from .consts import WEATHER_API_BASE

def get_current_weather(lat, long):
    weather_url = WEATHER_API_BASE.format(lat=lat, long=long)
    try:
        r = requests.get(weather_url)
        r.raise_for_status()
        data = r.json()
        current = data["properties"]["timeseries"][0]
        current_temp = {
            "temperature": current["data"]["instant"]["details"]["air_temperature"]
        }
        return current_temp
    except Exception as e:
        print(e)
        return {}