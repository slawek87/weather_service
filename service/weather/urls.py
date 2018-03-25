from django.conf.urls import url

from weather import api_views

urlpatterns = [
    url(r'^upload$', api_views.UploadWeatherData.as_view(), name='create_weather_data'),
    url(r'^list$', api_views.ListWeatherData.as_view(), name='list_weather_data'),
]
