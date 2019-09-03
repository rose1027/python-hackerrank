import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

numberlist = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #print(tag.contents[0])
    numberlist.append(tag.contents[0])

for index, item in enumerate(numberlist):
    numberlist[index] = int(item)
#print(numberlist)
print(sum(numberlist))
