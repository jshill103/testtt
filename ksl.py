#!/usr/bin/python
# import our libs to navigate to a website
import requests
import json 
from bs4 import BeautifulSoup

# pages to check prices
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
html = requests.get("https://classifieds.ksl.com/search?category[]=Toys&subCategory[]=&keyword=funko&priceFrom=&priceTo=&zip=84651&miles=50&sellerType[]=&marketType[]=Sale&hasPhotos[]=&postedTimeFQ[]=", headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')

        # Webpage uses a javascript data structure to hold ad info
for script in soup.find_all('script'):
    if "listings: " in str(script):
                # reduce script to just json structure
                # Looks something like this right now:
                #  window.renderSearchSection({ listings: [{"id" . . .
                #  ...
                #  })
                # So we just need to grab stuff between outer parens
        list_json = (script.contents[0].split('(', 1)[-1].rsplit(')', 1)[0])
                # Put double quotes around property name
        list_json = list_json.replace('listings: ', '"listings": ')
        list_json = "\n".join(list_json.split("\n")[:2])
        list_json = list_json.rstrip(',') + "}"
                # Turn the json into a dict and grab the list of listings
        listings = json.loads(list_json)['listings']
        for ad_box in listings:
            if 'featured' in ad_box['listingType']:
                continue

            print ad_box['city'], ad_box['title'], ad_box['description']