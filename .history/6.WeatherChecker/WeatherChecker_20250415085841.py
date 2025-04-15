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

response = requests.get(BASE_URL,parms=parms)
data = response.json

if response.status_code == 200:
    temp = ['main']['temp']
    description = data['weather'][0]['description']
    print(f'The weather in {city} is {temp}°F with {description}.')
else:
    print("Status Error!")

    

