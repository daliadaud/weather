import requests
import logging

from .consts import WEATHER_API_BASE


logger = logging.getLogger(__name__)


def get_current_weather(latitute, long):
    data = request_weather(latitute, long)
    if data:
        current = data["properties"]["timeseries"][0]
        current_temp = {
            "temperature": current["data"]["instant"]["details"]["air_temperature"]
        }
        return current_temp
    return {}


def request_weather(latitute, long):
    weather_url = WEATHER_API_BASE.format(lat=float(latitute), long=float(long))
    try:
        r = requests.get(weather_url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logger.error("Error getting weather")
        logger.error(e)
        return None