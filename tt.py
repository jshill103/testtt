#!/usr/bin/python
# import our libs to navigate to a website
import requests
import json 
from bs4 import BeautifulSoup
import time
starttime=time.time()

while True:
# pages to check prices
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    html = requests.get("https://launch.toytokyo.com/password", headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    text = soup.findAll("span", {"class": "default-text"})
    print text
    time.sleep(10)