
import googlemaps
from datetime import datetime
import uuid
import json
import urllib2


def macAddress():
    mac_num = hex(uuid.getnode()).replace('0x', '')
    mac = ':'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
    return mac;

def create_json():
    data = {}
    mac = macAddress()
    data = {
        "considerIp": "true",
        "wifiAccessPoints": [
            {
                "macAddress": mac,
                "signalStrength": -43,
                "signalToNoiseRatio": 0
            }
            ]
            }
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def curling():
    create_json()
    curl -i https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCLeZmqNngLeJslWpZ1R_EUpI3GzaxV6JgY -d @data.json -H "Content-Type: application/json"


if __name__ == '__main__':
    create_json()
