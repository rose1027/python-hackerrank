import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

numberlist = list()
counts = 0
i = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# repeat count times
while count > 0: # loop based on count
    counts = 0
    tags = soup('a')
    # loop below is to find the position
    for tag in tags:
        if counts == position-1:
            #print(' position TRUE********')
            #print('URL:', tag.get('href', None))
            url = tag.get('href', None)
            #print('Contents:', tag.contents[0])
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            #print('new html****')
            #print('Contents:', tag.contents[0])
            #print('URL:', tag.get('href', None))
            break
        counts = counts + 1
    count = count - 1

print('Contents:', tag.contents[0])













# Retrieve all of the anchor tags
