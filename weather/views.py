from django.shortcuts import render

from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseServerError,
    HttpResponse,
    JsonResponse
)
from .utils import get_current_weather

# Create your views here.

def location_weather(request):
    latitude = request.GET.get('lat')
    longitute = request.GET.get('long')

    #todo validation
    return JsonResponse(get_current_weather(latitude, longitute))
