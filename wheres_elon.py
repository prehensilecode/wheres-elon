#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

icao = 'A835AF'
url = f'https://adsbexchange-com1.p.rapidapi.com/v2/icao/{icao}/'

with open('APIKEY.txt', 'r') as f:
    api_key = str(f.read()).strip()

print(api_key)

headers = {
	"X-RapidAPI-Key": f"{api_key}",
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
