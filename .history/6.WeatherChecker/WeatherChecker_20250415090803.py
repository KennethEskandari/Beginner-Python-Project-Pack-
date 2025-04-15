import requests
import os 

OPENWEATHER_API_KEY = os.getenv('OPEMNWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Debugging Key 
print(os.getenv(OPENWEATHER_API_KEY))
#Allows you to input the city
city=input("Enter city name: ")

#Setting Up Params For the Response
params = {
    'q': city,
    'addid':OPENWEATHER_API_KEY,
    'units': 'imperial'
}

#Getting JSON and Showing it 
response = requests.get(BASE_URL,params=params)
data = response.json

#Parsing Through JSON
if response.status_code == 200:
    temp = ['main'],['temp']
    description = data['weather'][0]['description']
    print(f'The weather in {city} is {temp}°F with {description}.') #Shows weather
else:
    print("City Not Found. Try Again!")
    print('Response',data)





