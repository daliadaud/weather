import requests
import logging

from django.conf import settings

from .consts import WEATHER_API_BASE, CITIES_INFO, WEATHER_API_FORECAST


logger = logging.getLogger(__name__)


def get_my_cities_weather(cities):
    
    cities = [city.upper() for city in cities]
    data = []
    for city in cities:
        res = get_weather(CITIES_INFO[city]["lat"], CITIES_INFO[city]["lng"], 'current')
        res['key'] = city
        data.append(res)
    return data


def get_forecast(city):
    return get_weather(CITIES_INFO[city]["lat"], CITIES_INFO[city]["lng"], 'forecast')


def get_weather(lat, lon, weather_type):
    if weather_type == 'current':
        weather_url = WEATHER_API_BASE.format(lat=float(lat), lon=float(lon), api_key=settings.WEATHER_MAP_API_KEY)
    elif weather_type == 'forecast':
        weather_url = WEATHER_API_FORECAST.format(lat=float(lat), lon=float(lon), api_key=settings.WEATHER_MAP_API_KEY)
    try:
        r = requests.get(weather_url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logger.error("Error getting weather")
        logger.error(e)
        return None


def get_my_cities():
    return [city.lower() for city in CITIES_INFO.keys()]