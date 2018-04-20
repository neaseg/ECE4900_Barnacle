
import googlemaps
from datetime import datetime
import uuid
import json
import urllib2
import requests


def macAddress():
    mac_num = hex(uuid.getnode()).replace('0x', '')
    mac = ':'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
    return mac;

def create_json():
    data = {}
    mac = macAddress()
    data = {"considerIp": "true",
        "wifiAccessPoints": [
            {"macAddress": mac,
             "signalStrength": -43,
             "signalToNoiseRatio": 0}
            ]
            }
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def curling():


    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('key', 'AIzaSyCXrUK0aCj9ISl41ZjLf84qEizFZf5FRvU'),
    )

    data = open('data.json')
    response = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', headers=headers, params=params, data=data)

    with open('location.json', 'w') as outfile:
        json.dump(response.content, outfile)

    location = json.loads(response.content)
    return location['location']

if __name__ == '__main__':
    create_json()
    apt = curling()
    lat = apt['lat']
    lng = apt['lng']
    print lat
    print lng
