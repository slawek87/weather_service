import pandas as pd

from client.libs.registry import default_reader_registry, register_reader


class WeatherReader(object):
    SHEET_NAME = 0
    COLUMNS = ['date', 'time', 'geoposition_coordinates', 'high_under_ground', 'temperature',
               'wind_speed', 'wind_vector_direction']

    DATA_TEMPLATE = {
        'weather_datetime': None,
        'latitude': None,
        'longitude': None,
        'high_under_the_ground': None,
        'temperature': None,
        'wind_speed': None,
        'wind_vector_direction': None,
        'row_number': None
    }

    data = []

    DATE_STRING = "%Y-%m-%d"
    TIME_STRING = "%H:%M:%S"

    def __init__(self, weather_xls):
        self.weather_xls = weather_xls

    def read(self):
        """Reads data from Excel file. Reads only new rows."""
        skiprows = self.skiprows()
        sheet = pd.read_excel(self.weather_xls, sheet_name=self.SHEET_NAME,
                              skiprows=skiprows, names=self.COLUMNS, header=0)

        for index, row in sheet.iterrows():
            row['row_number'] = index + skiprows
            self.set_data(row)

    def set_data(self, row):
        """Uses DATA_TEMPLATE to set correct data."""
        parse_data = self.DATA_TEMPLATE.copy()

        parse_data['weather_datetime'] = "{date_string}T{time_string}".format(
            date_string=row['date'].strftime(self.DATE_STRING), time_string=row['time'].strftime(self.TIME_STRING))
        parse_data['latitude'], parse_data['longitude'] = row['geoposition_coordinates'].split(',')
        parse_data['high_under_ground'] = row['high_under_ground']
        parse_data['temperature'] = row['temperature']
        parse_data['wind_speed'] = row['wind_speed']
        parse_data['wind_vector_direction'] = row['wind_vector_direction'].upper()
        parse_data['row_number'] = row['row_number']

        self.data.append(parse_data)

    def skiprows(self):
        """Returns how many rows should be skipped."""
        with open(default_reader_registry) as reader_registry:
            lines = reader_registry.readlines()
            if not lines:
                return 1

            return int(lines[-1]) + 1
