from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from django_q.tasks import async, result

from weather.models import WeatherModel
from weather.serializers import WeatherSerializer
from weather.tasks import task_calculate_stats

task_calculate_stats()

class UploadWeatherData(generics.CreateAPIView):
    model = WeatherModel
    serializer_class = WeatherSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        task_id = async('weather.api_views.async_create_weather_data', request.data)
        result(task_id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def async_create_weather_data(data):
    serializer = WeatherSerializer(data=data)
    serializer.is_valid()
    serializer.save()


class ListWeatherData(generics.ListAPIView):
    model = WeatherModel
    serializer_class = WeatherSerializer
    queryset = WeatherModel.objects.all()
