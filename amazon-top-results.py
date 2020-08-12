import requests
from bs4 import BeautifulSoup

payload = {'k' : 'mouse guard roleplaying game'};
page = requests.get("https://www.amazon.com/s", params=payload)

soup = BeautifulSoup(page);
