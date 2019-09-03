import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
newlist = list()

#read and extract data from http// .xml
address = input('Enter- ')
url = urllib.request.urlopen(address)
#print('Retrieving', url)
data = url.read()
#print('Retrieved', len(data), 'characters')

#from root to child to find child-parent node and put in the list
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
#print(len(results))

#parse the list find the count and put in the newlist
for item in results:
    newlist.append(item.find('count').text)
#print(newlist)
#put in the dictionary for it can be interger that can do sum!!
for index, item in enumerate(newlist):
    newlist[index] = int(item)
print(sum(newlist))

    
