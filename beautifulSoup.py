import requests
import os
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent

# url = "https://www.propertyguru.com.sg/"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) edge/120.0.0.0 Safari/537.36 Edg/120.0.0.0'} 
url = 'https://www.propertyguru.com.sg'
HEADERS = {'User-Agent': 
           'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
ua = UserAgent()
user_agent = ua.random
response = requests.get(url, headers=HEADERS)
 
if response.status_code == 200:
    with open('output.html', 'w', encoding = 'utf-8') as f:
        f.write(response.text)
    print(response.text)  # Print the content of the response
else:
    print(f'Request failed with status code: {response.status_code}')
