import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter- ')
url = urllib.request.urlopen(address)
print('Retrieving', url)
data = url.read().decode('utf-8')
print(type(data))

#print(data)
#print('Retrieved', len(data), 'characters')
newlist = list()
number = 0
counternumber = 0
info = json.loads(data)
#print(type(info))
#print('user count:', info)
counter = 0
#find the positon of comments!!!!
for key in info:
    if(key == 'comments'):
        #start from key = 'comments', extract data from a dictionary of list
        while counter < 50:
            #print(info[key][counter])
            #put the list that has small dictionaries into a newlist
            newlist.append(info[key][counter])
            counter = counter + 1
            number = number + 1
#print(newlist)
#extract specific data from list
for item in newlist:
    counternumber = item['count'] + counternumber
print(counternumber)
#print('sum number =', number)
