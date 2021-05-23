from django.urls import path

from . import views

urlpatterns = [

    # url(
    #     r'^location/',
    #     views.location_weather,
    #     name='location-weather'
    # )
    path('location/<str:latitude>/<str:longitute>/', views.location_weather)
]
