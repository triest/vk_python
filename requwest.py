from bs4 import BeautifulSoup as BS

import requests
from html.parser import HTMLParser

response = requests.get('https://vk.com/albums-121385113')

#print(response.text)

#soup = BS(response.text)

soup = BS(response.text)

#import requests
#from bs4 import BeautifulSoup as BS
#r = requests.get('https://vk.com/albums-12138511', verify=True)
#soup = BS(r.text)
#mydivs = soup.findAll("div", {"class": "stylelistrow"})