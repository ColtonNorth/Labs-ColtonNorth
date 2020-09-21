from urllib import request
from urllib.request import urlopen
import requests
import json

def read_data_thingspeak():
    URL = 'https://api.thingspeak.com/channels/1152316/fields/1.json?api_key=MHR94BNTWZFHQGBT&results2'
    KEY = 'MHR94BNTWZFHQGBT'
    HEADER = '&results=2'
    NEW_URL = URL+KEY+HEADER
    print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    print(get_data)
    channel_id = getdata['channel']['id']

    field_1 = get_data['feeds']
    print(field_1)

    t = []
    for x in field_1:
        print(x['field_1'])
        t.append(x['field_1'])

if __name__ == '__main__':
    read_data_thingspeak()
