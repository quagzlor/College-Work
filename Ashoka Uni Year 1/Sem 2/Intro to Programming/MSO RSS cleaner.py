import urllib
from bs4 import BeautifulSoup
doc = BeautifulSoup.BeautifulStoneSoup

with open("http://mangaseeonline.us/subscription-feed/") as fp:
	soup = BeautifulSoup(fp, "xml")

for item in soup.findAll('item'):
    for elt in item:
        if isinstance(elt,BeautifulSoup.Tag):
            print(elt)