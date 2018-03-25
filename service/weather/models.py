from django.db import models


class WeatherModel(models.Model):
    weather_datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    high_under_ground = models.FloatField()
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_vector_direction = models.CharField(max_length=2)


class WeatherStatsModel(models.Model):
    last_id = models.IntegerField()
    record_numbers = models.IntegerField()

    sum_temperature = models.FloatField()
    sum_wind_speed = models.FloatField()

    avg_temperature = models.FloatField()
    avg_wind_speed = models.FloatField()

    north_direction = models.IntegerField()
    south_direction = models.IntegerField()
    west_direction = models.IntegerField()
    east_direction = models.IntegerField()
    north_east_direction = models.IntegerField()
    north_west_direction = models.IntegerField()
    south_east_direction = models.IntegerField()
    south_west_direction = models.IntegerField()

    most_windy_direction = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)


def calculate_stats():
    last_stats = WeatherStatsModel.objects.last()
    last_id = getattr(last_stats, 'last_id', 0)

    new_stats = WeatherStatsModel(
        record_numbers=getattr(last_stats, 'record_numbers', 0),
        sum_temperature=getattr(last_stats, 'sum_temperature', 0),
        sum_wind_speed=getattr(last_stats, 'sum_wind_speed', 0),
        north_direction=getattr(last_stats, 'north_direction', 0),
        south_direction=getattr(last_stats, 'south_direction', 0),
        east_direction=getattr(last_stats, 'east_direction', 0),
        west_direction=getattr(last_stats, 'west_direction', 0),
        north_east_direction=getattr(last_stats, 'north_east_direction', 0),
        north_west_direction=getattr(last_stats, 'north_west_direction', 0),
        south_east_direction=getattr(last_stats, 'south_east_direction', 0),
        south_west_direction=getattr(last_stats, 'south_west_direction', 0),
    )

    set_wind_direction = {
        'N': 'north_direction',
        'S': 'south_direction',
        'W': 'west_direction',
        'E': 'east_direction',
        'NW': 'north_west_direction',
        'NE': 'north_east_direction',
        'SW': 'south_west_direction',
        'SE': 'south_east_direction'
    }

    if not WeatherModel.objects.filter(id__gt=last_id).exists():
        return None

    for record in WeatherModel.objects.filter(id__gt=last_id):
        new_stats.last_id = record.id
        new_stats.record_numbers += 1
        new_stats.sum_temperature += record.temperature
        new_stats.sum_wind_speed += record.wind_speed

        setattr(new_stats,
                set_wind_direction[record.wind_vector_direction],
                getattr(new_stats, set_wind_direction[record.wind_vector_direction]) + 1)

    wind_directions = ['north_direction', 'south_direction', 'west_direction', 'east_direction','north_west_direction',
                       'north_east_direction', 'south_west_direction', 'south_east_direction']

    most_windy_direction = dict()
    for wind_direction in wind_directions:
        most_windy_direction[wind_direction] = getattr(new_stats, wind_direction)

    new_stats.most_windy_direction, _ = sorted(most_windy_direction.items(), key=lambda wind_speed: wind_speed[1])[-1]

    new_stats.avg_temperature = new_stats.sum_temperature / new_stats.record_numbers
    new_stats.avg_wind_speed = new_stats.sum_wind_speed / new_stats.record_numbers
    new_stats.save()
