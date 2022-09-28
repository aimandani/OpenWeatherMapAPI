import datetime as dt
import requests

BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "84d9e42ef52368504d80708c71bf45ff"

CITY = "London"

url = BASE_URL+"appid="+API_KEY +"&q=" + CITY

response =requests.get(url).json()
print(response)