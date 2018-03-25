from os import path
from client.libs.schedule import setup

dir_path = path.dirname(path.abspath(__file__))


if __name__ == '__main__':
    """Run weather client."""
    weather_xls = path.join(dir_path, 'weather.xlsx')
    setup(weather_xls=weather_xls)
