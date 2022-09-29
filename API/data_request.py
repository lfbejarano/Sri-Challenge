import urllib.request
import json
from datetime import datetime, timedelta


class requester:
    """
    This class is to request the timestamp and weather stock_info from the API
    and return it as a dictionary validating for date interval or sending
    yesterday information
    """

    def __init__(self) -> None:
        " Defining the url for the API"
        self.__url = "https://api.weather.gov/stations/KBFL/observations"

    def get_weather_report(self, start: str, end: str) -> dict:
        "Method that returns the information when start and end date is provided"
        try:
            st = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
            e = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")
            if e < st:
                return "start date is greater than end date"
        except ValueError:
            return 'Incorrect start or end data format, /n \
                    format should be "%Y-%m-%dT%H:%M:%SZ"'

        api_request = self.__url + '?start=' + start + '&end=' + end
        response = urllib.request.urlopen(api_request)
        data: bytes = response.read()
        station_info: dict = json.loads(data)
        result = self.__timestamp_temp(station_info)
        return result

    def yesterday_weather_report(self) -> dict:
        "Method that returns the information for yesterday"
        today = datetime.now().strftime("%Y-%m-%d")
        today = datetime.strptime(today, "%Y-%m-%d")
        yesterday = today - timedelta(days=1)
        start = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")
        end = today.strftime("%Y-%m-%dT%H:%M:%SZ")
        api_request = self.__url + '?start=' + start + '&end=' + end
        response = urllib.request.urlopen(api_request)
        data: bytes = response.read()
        station_info: dict = json.loads(data)
        result = self.__timestamp_temp(station_info)
        return result

    def __timestamp_temp(self, station_info: dict) -> list:
        "Method that returns a list with only timestamp and temperature \
         receiving the station_info from the API converted to dict"
        result = []
        for record in station_info['features']:
            result.append((record['properties']['timestamp'],
                           record['properties']['temperature']['value']))
        return result[::-1]
