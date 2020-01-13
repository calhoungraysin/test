import pprint

import requests

city = input()
app_key = '9da81b09ab671d99202764fe681d24a6'

responce = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=3&appid={app_key}')

responce = responce.json()


print(pprint.pprint(responce))
