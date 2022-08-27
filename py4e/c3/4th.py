# Using the ord function -
print('For letter H the ASCII vale is - ')
print(ord('H'))

# 3rd week ka kaam in a easy way -
import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

count = dict()
for lines in fhandle:
    words = lines.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

# Web Scraping - Browsing through the net and extracting information
# from different web pages.These programs are called web crawlers.

input()
