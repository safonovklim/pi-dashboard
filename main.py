import time
from datetime import datetime
from api import display, data

# Configuration
WEATHER_CITY = 'Moscow,RU'  # format is {city},{country_code}. example: "New York,US"
UPDATE_WEATHER_IN = 3600  # offset in seconds
UPDATE_BTC_RATE_IN = 600  # offset in seconds


def get_brightness():
    d = datetime.now()
    hour = int(d.strftime("%I"))
    if 23 <= hour < 7: return 0.2
    if 7 <= hour < 18: return 0.8
    if 18 <= hour < 23: return 0.5
    return 1


def get_date():
    d = datetime.now()
    month = d.strftime("%B")[:3]
    return d.strftime("%d " + month)


def get_timestamp():
    return int(datetime.now().timestamp())


def get_weather():
    api_call = data.get_weather(WEATHER_CITY)
    if data.is_response_ok(api_call):
        return api_call.json()


def get_crpyto():
    api_call = data.get_crypto()
    if data.is_response_ok(api_call):
        return api_call.json()


def can_update_weather(previous_ts):
    current_ts = get_timestamp()

    return (current_ts - previous_ts) > UPDATE_WEATHER_IN


def can_update_crypto(previous_ts):
    current_ts = get_timestamp()

    return (current_ts - previous_ts) > UPDATE_BTC_RATE_IN


def format_weather(weather_data):
    value = int(weather_data['main']['temp'])
    value_str = str(value)
    if value > 0:
        return "+" + value_str + '°C'
    return value_str + '°C'


def format_weather_city(weather_data):
    return weather_data['name']


def print_text(string, timeout = 2):
    display.print_string(string)
    time.sleep(timeout)
    display.reset()


# Initial procedures
brightness = get_brightness()
print('Brightness changed to ', brightness)
display.set_brightness(brightness)

ts = get_timestamp()
timestamps = {
    'weather': ts,
    'crypto': ts
}

weather = get_weather()
crypto = get_crpyto()

while True:
    # print_text(format_weather_city(weather))
    # print_text(format_weather(weather))

    for item in crypto:
        print_text('1 ' + item['symbol'])
        print_text('$' + item['price_usd'])

    print_text(get_date())

    display.show_time()
    display.reset()

    temp_brightness = get_brightness()
    if temp_brightness != brightness:
        print('Brightness changed to ', brightness)
        brightness = temp_brightness
        display.set_brightness(brightness)

    if can_update_weather(timestamps['weather']):
        print('Weather updated')
        weather = get_weather()
        timestamps['weather'] = get_timestamp()

    if can_update_crypto(timestamps['crypto']):
        print('Crypto updated')
        crypto = get_crpyto()
        timestamps['crypto'] = get_timestamp()