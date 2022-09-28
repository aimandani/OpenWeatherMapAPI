import datetime as dt
import requests

BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "84d9e42ef52368504d80708c71bf45ff"

CITY = "Vienna"

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin -273.15
    fahrenheit = celcius * (9/5) +32

    return celcius , fahrenheit

url = BASE_URL+"appid="+API_KEY +"&q=" + CITY

response =requests.get(url).json()

temp_kelvin = response ['main']['temp']
temp_celcius , temp_fahrenheit  = kelvin_to_celcius_fahrenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celcius , feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)

humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

wind_speed = response['wind']['speed']


print(f"Temperature in {CITY}: {temp_celcius:.2f} C or {temp_fahrenheit:.2f} F")
print(f"Temperature in {CITY} feels like : {feels_like_celcius:.2f} C or {feels_like_fahrenheit:.2f} F")
print(f"Humidity in {CITY}: {humidity:.2f} %")
print(f"Windspeed in {CITY}: {wind_speed:.2f} m/s")
print(f"Sun Rises  in {CITY} at {sunrise_time} local time")
print(f"Sun sets  in {CITY} at {sunset_time} local time")



print(f" General Weather  in {CITY}: {description} ")





