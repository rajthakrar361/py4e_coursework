import urllib.request, urllib.parse, urllib.error
import json

count = 0

address = input("Enter Location: ")
url = address
print("retrieving URL", url)
uh = urllib.request.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	count += int(item["count"])
print(count)
