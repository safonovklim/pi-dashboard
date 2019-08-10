import requests

WEATHER_API_KEY = 'd449ddc6b9dd3bce331e507181dbad81'
WEATHER_API_ROUTE = 'http://api.openweathermap.org/data/2.5/weather'

COINMARKET_API_ROUTE = 'https://api.coinmarketcap.com/v1/ticker/bitcoin'


def is_response_ok(response):
    return response.status_code == requests.codes.ok


def api_get(route, options = {}):
    headers = options['headers'] if 'headers' in options else {}
    query = options['query'] if 'query' in options else {}

    return requests.get(route, params=query, headers=headers)


def get_weather(city = 'Moscow,RU'):
    options = {
        'query': {
            'q': city,
            'APPID': WEATHER_API_KEY,
            'units': 'metric'  # "metric" is celsius, "imperial" is fahrenheit
        }
    }

    return api_get(WEATHER_API_ROUTE, options)


def get_crypto():
    return api_get(COINMARKET_API_ROUTE)