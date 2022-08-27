import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a url - ")
html = urllib.request.urlopen(url, context = ctx).read()
# .read() will read the whole file as one string.
soup = BeautifulSoup(html, 'html.parser')

# Retriving all the anchor tags from the page -
tags = soup('span') # This will make a list of anchor tags.
summation = list()
for tag in tags:
    summation.append(int(tag.contents[0]))
print(sum(summation))

input()
