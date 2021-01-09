# https://github.com/csparpa/pyowm
# https://home.openweathermap.org/api_keys
from _2_config import token
from pyowm import OWM

owm = OWM(token)
mgr = owm.weather_manager()

city = input('Please enter the city: ')

# Search for current weather in London (Great Britain) and get details
try:
    observation = mgr.weather_at_place(city)  # London,GB
except:
    print('You enter incorrect data. I take the city: lol. Sorry.')
    observation = mgr.weather_at_place('lol')
w = observation.weather

print('clouds:', w.detailed_status)  # 'clouds'
print('wind:', w.wind())  # {'speed': 4.6, 'deg': 330}
print('humidity:', w.humidity)  # 87
# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print('temperature:', w.temperature('celsius'))
# print(w.rain)  # {}
# print(w.heat_index)  # None
print('?:', w.clouds)  # 75
# print(w)
# print('observation:', observation)
