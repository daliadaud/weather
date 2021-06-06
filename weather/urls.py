from django.urls import path

from . import views

urlpatterns = [
    path('', views.current_weather, name="current"),
    path('forecast', views.forecast_weather, name = "forecast")
]
