import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving: ", url)
xml = urllib.request.urlopen(url, context = ctx).read()
print("Retrived", len(xml), " characters")

stuff = ET.fromstring(xml)
counts = stuff.findall('.//count')
sum = 0
n = 0
for count in counts:
    sum += int(count.text)
    n += 1
print("Count: ", n)
print("Sum: ", sum)
