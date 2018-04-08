from twilio.rest import Client
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()
# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()

#ble.run_mainloop_with(backend.why_are_you_looking_this_close)

# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)


# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.
def why_are_you_looking_this_close(trigger):
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
        received = uart.read(timeout_sec=60)
        if received is not None:
            # Received data, print it out.
            print('Received: {0}'.format(received))
            # Write a string to the TX characteristic.
            print("Sent 'Hello world!' to the device.")
            uart.write('Hello world!\r\n')
            trigger = True;
        else:
            # Timeout waiting for data, None is returned.
            print('Received no data!')




def send_sms(number,message):
    client.api.account.messages.create(
        to=number,
        from_="+13522928542",
        body=message)
