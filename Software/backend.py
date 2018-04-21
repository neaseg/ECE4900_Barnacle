from twilio.rest import Client
from datetime import datetime
import uuid
import json
import urllib2
import requests


#ble.run_mainloop_with(backend.why_are_you_looking_this_close)

# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)

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

def gps_message(message):
    create_json()
    create_json()
    apt = curling()
    lat = apt['lat']
    lng = apt['lng']
    new_message = message + '\n Your loved one is located at \n Lat: ' + str(lat)+ '   Lng: ' + str(lng)
    print("we got here")
    return new_message

def send_sms(number,message):
    gps_m = gps_message(message)
    client.api.account.messages.create(
        to=number,
        from_="+13522928542",
        body=gps_m)
        
    client.calls.create(
    to="number",
    from_="+13522928542",
    url="http://raw.githubusercontent.com/ulnneverknow/temp/master/danger.xml"
)
