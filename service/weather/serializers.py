from rest_framework import serializers
from weather.models import WeatherModel


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherModel
        fields = ('weather_datetime', 'latitude', 'longitude', 'high_under_ground',
                  'wind_speed', 'wind_vector_direction', 'temperature',)
