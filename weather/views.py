from django.shortcuts import render

from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseServerError,
    HttpResponse,
    JsonResponse
)
from .utils import get_my_cities_weather, get_forecast
from .consts import CITIES_INFO, DEFAULT_CITY

# Create your views here.

def current_weather(request):
    cities = request.GET.getlist('city', [DEFAULT_CITY])
    data = get_my_cities_weather(cities)
    print(data)
    return render(request, 'weather/index.html', {"weather": data})


def forecast_weather(request):
    city = request.GET.get('city', [DEFAULT_CITY])
    print("getting forecast **********")
    data = get_forecast(city)
    return render(request, 'weather/forecast.html', {"weather": data})

