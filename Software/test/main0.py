#!/usr/bin/python
#import sys
#import os.path
#sys.path.append('/Users/allisonmack')
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
import backend
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART
import threading

# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()
# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()

Builder.load_string("""
<HomePage>:
	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.25
			text: "Contacts"
			on_release: app.root.current = 'other1'
			pos_hint: {"right":1, "top":0.75}

	FloatLayout:
		Label:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.7,1
			text: "Welcome to TIMBER!"
			pos_hint: {"left":1, "top":1}


	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.25
			text: "Dial 911"
			on_release: app.root.current = 'other2'
			pos_hint: {"right":1, "top":0.25}

	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.25
			text: "Text Options"
			on_release: app.root.current = 'other4'
			pos_hint: {"right":1, "top":0.50}

	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.25
			text: "User Info"
			on_release: app.root.current = 'other3'
			pos_hint: {"right":1, "top":1}

<Contact>:

	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.5,0.2
			text: "Home"
			on_release: app.root.current = "main"
			pos_hint: {"left":0, "bottom":1}

	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.5,0.2
			text: "Next"
			on_release: app.root.current = "c_input"
			pos_hint: {"right":1, "bottom":1}

	FloatLayout:
		Label:
			color: 1,1,1,1
			font_size: 20
			size_hint: 1,0.3
			text: "Press 'Next' to enter up to four emergency "
			pos_hint: {"right":1, "top":1}
		Label:
			color: 1,1,1,1
			font_size: 20
			size_hint: 1,0.5
			text: "contacts or press 'Home' to go back."
			pos_hint: {"right":1, "top":1}

<Dial>:
	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 1,0.2
			text: "Back Home"
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "bottom":1}

	FloatLayout:
		IntentButton:
			color: 1,1,1,1
			font_size: 75
			size_hint: 1,0.8
			text: "DIAL 911"
			on_release:  self.send_text_message()
			pos_hint: {"right":1, "top":1}


<User>:
	user_firstname: firstname.text
	user_lastname: lastname.text

	FloatLayout:
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "First Name:"
			size_hint: 0.5,0.33
			pos_hint: {"right":0.5, "top":1}
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "Last Name:"
			size_hint: 0.5,0.33
			pos_hint: {"right":0.5, "top":0.66}
		TextInput:
			id: firstname
			text: root.user_firstname
			multiline: False
			size_hint: 0.5,0.33
			pos_hint: {"right":1, "top":1}
		TextInput:
			id: lastname
			text: root.user_lastname
			multiline: False
			size_hint: 0.5,0.33
			pos_hint: {"right":1, "top":0.66}
		UserInput_HomeButon:
			color: 1,1,1,1
			font_size: 25
			size_hint: 1,0.33
			text: "Back Home"
			on_press: root.update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "bottom":1}

<Text>:
	FloatLayout:
		Label:
			color: 1,1,1,1
			font_size: 20
			size_hint: 1,0.8
			text: "Press 'Next' to to select your emergency message or press 'Home' to go back."
			pos_hint: {"right":1, "top":1}
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.5,0.2
			text: "Next"
			on_release: app.root.current = "t_input"
			pos_hint: {"right":1, "bottom":1}
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.5,0.2
			text: "Home"
			on_release: app.root.current = "main"
			pos_hint: {"right":0.5, "bottom":1}
<TextMessages>:
	message1: 'Your loved one is in distress, and needs immediate medical attention.'
	message2: 'Your loved one is in distress, and needs immediate medical attention.'
	message3: "The user has collapsed and requires immediate medical attention"
	message4: _message4.text
	sms_message: ''
	FloatLayout:
		Label:
			id: message1
			color: 1,1,1,1
			font_size: 20
			text: "Your loved one is in distress, and needs immediate medical attention."
			size_hint: 0.8,0.2
			pos_hint: {"right":0.8, "top":1}
		Label:
			id: message2
			color: 1,1,1,1
			font_size: 20
			text: "Your loved one is in distress, and needs immediate medical attention."
			size_hint: 0.8,0.2
			pos_hint: {"right":0.8, "top":0.8}
		Label:
			id: message3
			color: 1,1,1,1
			font_size: 20
			text: "The user has collapsed and requires immediate medical attention"
			size_hint: 0.8,0.2
			pos_hint: {"right":0.8, "top":0.6}
		TextInput:
			id: _message4
			color: 1,1,1,1
			font_size: 20
			multiline: True
			text: root.message4
			size_hint: 0.8,0.2
			pos_hint: {"right":0.8, "top":0.4}
		TextInput_HomeButton:
			message_sel: message1
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.2,0.2
			text: "Select"
			on_press: root.message1_update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":1}
		TextInput_HomeButton:
			message_sel: message2
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.2,0.2
			text: "Select"
			on_press: root.message2_update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":0.8}
		TextInput_HomeButton:
			message_sel: message3
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.2,0.2
			text: "Select"
			on_press: root.message3_update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":0.6}
		TextInput_HomeButton:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.2,0.2
			text: "Select"
			on_press: root.message4_update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":0.4}

		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 1,0.2
			text: "Home"
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "bottom":1}

<ContactInput>:
	contact1: _contact1.text
	contact2: _contact2.text
	contact3: _contact3.text
	contact4: _contact4.text
	FloatLayout:
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "Contact 1"
			size_hint: 0.5,0.2
			pos_hint: {"right":0.5, "top":1}
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "Contact 2"
			size_hint: 0.5,0.2
			pos_hint: {"right":0.5, "top":0.8}
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "Contact 3"
			size_hint: 0.5,0.2
			pos_hint: {"right":0.5, "top":0.6}
		Label:
			color: 1,1,1,1
			font_size: 25
			text: "Contact 4"
			size_hint: 0.5,0.2
			pos_hint: {"right":0.5, "top":0.4}
		TextInput:
			id: _contact1
			multiline: False
			text: root.contact1
			size_hint: 0.5,0.2
			pos_hint: {"right":1, "top":1}
		TextInput:
			id: _contact2
			multiline: False
			text: root.contact2
			on_text_validate: message.focus = True
			size_hint: 0.5,0.2
			pos_hint: {"right":1, "top":0.8}
		TextInput:
			id: _contact3
			multiline: False
			text: root.contact3
			on_text_validate: message.focus = True
			size_hint: 0.5,0.2
			pos_hint: {"right":1, "top":0.6}
		TextInput:
			id: _contact4
			multiline: False
			text: root.contact4
			on_text_validate: message.focus = True
			size_hint: 0.5,0.2
			pos_hint: {"right":1, "top":0.4}
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 1,0.2
			text: "Home"
			on_press: root.update()
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":0.2}

""")
class HomePage(Screen):
	def discover_device():
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
			device.connect()# Will time out after 60 seconds, specify timeout_sec parameter
	                      # to change the timeout.
	    # Once connected do everything else in a try/finally to make sure the device
	    # is disconnected when done.
	        # Wait for service discovery to complete for the UART service.  Will
	        # time out after 60 seconds (specify timeout_sec parameter to override).
			print('Discovering services...')
			UART.discover(device)
	        # Once service discovery is complete create an instance of the service
	        # and start interacting with it.
			uart = UART(device)
			return uart

	def message_device(uart):
	    # Write a string to the TX characteristic.
	    uart.write('Hello world!\r\n')
	    print("Sent 'Hello world!' to the device.")


	        # Now wait up to one minute to receive data from the device.
	def recieve_message(uart):
		ans = False
		received = uart.read(timeout_sec=5)
		if received is not None:
			# Received data, print it out.
			print('Received: {0}'.format(received))
			ans = True
			return ans

	def run_toggle(self,*args):
		if (Main.startup):
			Main.startup = False;
		else:
			if Main.uart is None:
				Main.uart = discover_device()
			else:
				if(recieve_message(Main.uart)):
					IntentButton.send_text_message()

	run_toggle

class Contact(Screen):
	pass

class Dial(Screen):
	pass

class User(Screen):
	def update(self,*args):
		Main.user_info[0] = self.user_firstname
		Main.user_info[1] = self.user_lastname

class Text(Screen):
	pass

class ContactInput(Screen):
	def update(self,*args):
		Main.contacts[0] = self.contact1
		Main.contacts[1] = self.contact2
		Main.contacts[2] = self.contact3
		Main.contacts[3] = self.contact4


class TextMessages(Screen):
	message1 = 'Your loved one is in distress, and needs immediate medical attention.'
	message2 = 'Your loved one is in distress, and needs immediate medical attention.'
	message3 = "The user has collapsed and requires immediate medical attention"

	def message1_update(self, *args):
		Main.message = self.message1

	def message2_update(self, *args):
		Main.message = self.message2

	def message3_update(self, *args):
		Main.message = self.message3

	def message4_update(self, *args):
		Main.message = self.message4

	def update(self,*args):
		Main.message = self.message4

class ScreenManagement(ScreenManager):
	pass


class TextInput_HomeButton(Button):
	pass


class UserInput_HomeButon(Button):
	# User Info
	uinfo_first = StringProperty()
	uinfo_last = StringProperty()

class IntentButton(Button):
	def send_text_message(self, *args):
			for i in Main.contacts:
				if i:
					backend.send_sms(i,Main.message)


# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.


screen_manager = ScreenManager()
screen_manager.add_widget(HomePage(name="main"))
screen_manager.add_widget(Contact(name="other1"))
screen_manager.add_widget(Dial(name="other2"))
screen_manager.add_widget(User(name="other3"))
screen_manager.add_widget(Text(name="other4"))
screen_manager.add_widget(ContactInput(name="c_input"))
screen_manager.add_widget(TextMessages(name="t_input"))

# The class name must match the .kv file name
class Main(App):
	contacts = ['','','',''] # can select contacts by Main.contacts
	message = '' #can access messsage by using Main.message
	user_info = ['',''] #access user information by using Main.
	startup = True
	uart = None;
	def build(self):
		return screen_manager

if __name__ == '__main__':
	Main().run()