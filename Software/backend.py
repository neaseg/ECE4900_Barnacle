from twilio.rest import Client
from datetime import datetime
import uuid
import json
import urllib2
import requests
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

mario = []
# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()
# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()



# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.
def main():
    # Clear any cached data because both bluez and CoreBluetooth have issues with
    # caching data and it going stale.
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    print('Using adapter: {0}'.format(adapter.name))

    # Disconnect any currently connected UART devices.  Good for cleaning up and
    # starting from a fresh state.
    print('Disconnecting any connected UART devices...')
    UART.disconnect_devices()

    # Scan for UART devices.
    print('Searching for UART device...')
    try:
        adapter.start_scan()
        # Search for the first UART device found (will time out after 60 seconds
        # but you can specify an optional timeout_sec parameter to change it).
        device = UART.find_device()
        if device is None:
            raise RuntimeError('Failed to find UART device!')
    finally:
        # Make sure scanning is stopped before exiting.
        adapter.stop_scan()

    print('Connecting to device...')
    device.connect()  # Will time out after 60 seconds, specify timeout_sec parameter
                      # to change the timeout.

    # Once connected do everything else in a try/finally to make sure the device
    # is disconnected when done.

    beta = True;
    while beta:
        try:
        # Wait for service discovery to complete for the UART service.  Will
        # time out after 60 seconds (specify timeout_sec parameter to override).
            print('Discovering services...')
            UART.discover(device)
        # Once service discovery is complete create an instance of the service
        # and start interacting with it.
            uart = UART(device)
            beta = False;
        finally:
            print('Didnt connect initally. Trying again')


    while 1:
        # Now wait up to one minute to receive data from the device.
        print('Waiting up to 60 seconds to receive data from the device...')
        received = uart.read(timeout_sec=20)
        if received is not None:
            # Received data, print it out.
            print('Received: {0}'.format(received))
            # Write a string to the TX characteristic.
            print("Sent 'Hello world!' to the device.")
            uart.write('Hello world!\r\n')
            file = open("testfile.txt","w")
            file.write(received)
            file.close
        else:
            # Timeout waiting for data, None is returned.
            print('Received no data!')

def run():
    ble.run_mainloop_with(main)



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
    to=number,
    from_="+13522928542",
    url="http://raw.githubusercontent.com/ulnneverknow/temp/master/danger.xml"
)
