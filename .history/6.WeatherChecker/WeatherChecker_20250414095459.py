import requests
import os

api_key = os.getenv("OPENWEATHER_API_KEY")

if api_key is None:
    raise ValueError("Cannot Find Key")