import argparse
import time
from prometheus_client import start_http_server, REGISTRY
from openweather.CloudCollector import CloudCollector

parser = argparse.ArgumentParser(
    prog='openweather-exporter',
    description='Exports data from OpenWeather API')
parser.add_argument('--api-key')
parser.add_argument('--city')
args = parser.parse_args()

REGISTRY.register(CloudCollector(args.api_key, args.city))

if __name__ == '__main__':
    start_http_server(8001)
    print('Now listening on port 8001')
    while True:
        time.sleep(60)
