from rest_framework import serializers
from weather.models import WeatherModel, WeatherStatsModel


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherModel
        fields = ('weather_datetime', 'latitude', 'longitude', 'high_under_ground',
                  'wind_speed', 'wind_vector_direction', 'temperature',)


class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStatsModel
        fields = ('avg_temperature', 'avg_wind_speed', 'most_windy_direction', 'created_at',)
