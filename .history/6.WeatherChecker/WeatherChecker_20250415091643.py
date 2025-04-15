import requests
import os

# Fetch the API key from environment variables
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Debugging Key (make sure the key is being fetched correctly)
print("API Key:", OPENWEATHER_API_KEY)

# Check if the API key exists
if not OPENWEATHER_API_KEY:
    print("API Key not found! Make sure you've set it correctly.")
    exit(1)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Allow the user to input the city name
city = input("Enter city name: ")

# Set up the parameters for the request
params = {
    'q': city,
    'appid': OPENWEATHER_API_KEY,  # Corrected to 'appid'
    'units': 'imperial'  # Using Fahrenheit
}

# Make the API request and get the response
response = requests.get(BASE_URL, params=params)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()  # Properly parse the response to JSON

    # Extract temperature and weather description
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    # Display the weather information
    print(f"The weather in {city} is {temp}°F with {description}.")
else:
    print("City Not Found. Try Again!")
    print('Response:', response.json())  # Print the error details from the API
