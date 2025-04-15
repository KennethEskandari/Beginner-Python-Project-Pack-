# Step 1: Import the necessary libraries
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

#Verifying Request
if response.status_code == 200:
    print("Success!")
else:
    print('Failure Response',response.status_code)

#Parsing Thorugh Website
soup = BeautifulSoup(response.text,'html.parser')

#Getting Titles
title_spans = soup.find_all('span', class_='titleline')

#Printing Results
for i, title in enumerate (title_spans,1):
    headline = title.get_text().strip()
    print(f'{i}.{headline}')

