import requests
import os 

API_KEY = os.getenv('OPEMNWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city=input("Enter city name: ")

parms = {
    'q': city,
    'addid':API_KEY,
    'units': 'imperial'
}

response = requests.get(parms,BASE_URL)