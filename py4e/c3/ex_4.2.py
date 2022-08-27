import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
count = input('Enter count: ')
position = input('Enter position: ')
print("Retrieving: ", url)
n = int(count)
link = url
while n > 0:
    html = urllib.request.urlopen(link, context = ctx).read()
    # .read() will read the whole file as one string.
    soup = BeautifulSoup(html, 'html.parser')
    # Retriving all the anchor tags from the page -
    tags = soup('a') # This will make a list of anchor tags.
    link = tags[int(position) - 1].get('href', None)
    print("Retrieving: ", link)
    n -= 1
input()
