import requests as requests
from prometheus_client.metrics_core import GaugeMetricFamily
from prometheus_client.registry import Collector


class CloudCollector(Collector):
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def collect(self):
        gauge_metric_family = GaugeMetricFamily('openweather_gauge', 'OpenWeather values')

        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&APPID={self.api_key}'
        response = requests.get(url)
        data = response.json()
        self.__add_samples__(gauge_metric_family, data)
        yield gauge_metric_family

    def __add_samples__(self, gauge_metric_family, data):
        labels = {'city': data['name']}
        gauge_metric_family.add_sample('openweather_temperature_kelvin', value=data['main']['temp'], labels=labels)
        gauge_metric_family.add_sample('openweather_humidity_percent', value=data['main']['humidity'], labels=labels)
