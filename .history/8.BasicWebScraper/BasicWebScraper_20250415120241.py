# Step 1: Import the necessary libraries
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

#Verifying Request
if response == 200:
    print("Success!")
else:
    ("Failure Response")

soup = BeautifulSoup(response.text,html.parser)