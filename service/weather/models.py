from django.db import models


class WeatherModel(models.Model):
    weather_datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    high_under_ground = models.FloatField()
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_vector_direction = models.CharField(max_length=2)


