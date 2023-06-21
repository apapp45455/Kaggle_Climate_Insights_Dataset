# This file will crawl countries in different area.

import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/geography/how-many-countries-in-asia/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

logo_tag_object = soup.find('a', {'id': 'logo'})
# logo_tag_object_list = soup.findAll('a', {'id': 'logo'})
logo_tag_object_list = soup.findAll('a', id='logo')

print(logo_tag_object)
print(logo_tag_object_list)

logo_tag_object = soup.select_one('a[id="logo"]')
logo_tag_object_list = soup.select('a#logo')