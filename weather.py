import json
import requests as req


def code_location(latitude, longitude, token_accu):
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' + \
                       f'{token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']
    return code


def weather(cod_loc, token_accu):
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey=' + \
                  f'{token_accu}&language=ru&metric=True'

    response = req.get(url_weather, headers={"APIKey": token_accu})
    json_data = json.loads(response.text)
    dict_weather = dict()
    dict_weather['link'] = json_data[0]['MobileLink']
    dict_weather['сейчас'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range(len(json_data)):
        time = 'через' + str(i) + 'ч'
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    return dict_weather
