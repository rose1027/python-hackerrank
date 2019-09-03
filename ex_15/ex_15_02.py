import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    print('dictionary = ', parms)
    #retrieve json
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    #read data from json
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        #loads method is turning json into python which is opposite of dumps method
        js = json.loads(data)
        #print(type(js))
        #print(js)
    except:
        js = None


    if not js or 'status' not in js or js['status'] != 'OK':
        print(js['status'])
        print('==== Failure To Retrieve ====')
        print(data)
        continue
#dump method is turning python to json
    #print(json.dumps(js, indent=4))

    placeId = js['results'][0]['place_id']
    print('placeID:', placeId)
