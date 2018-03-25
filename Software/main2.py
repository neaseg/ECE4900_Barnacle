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
#from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


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
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.7,1
			text: "Welcome to TIMBER!"
			on_release: app.root.current = 'main' 
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
			on_release: app.root.current = 'other3' 
			pos_hint: {"right":1, "top":0.50}

        FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.25
			text: "User Info"
			on_release: app.root.current = 'other4' 
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
		Button:
			color: 1,1,1,1
			font_size: 20
			size_hint: 1,0.8
			text: "Press 'Next' to enter up to four emergency contacts or press 'Home' to go back."
			on_release: app.root.current = "other1" 
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
		Button:
			color: 1,1,1,1
			font_size: 75
			size_hint: 1,0.8
			text: "DIAL 911"
			on_release: app.root.current = "main" 
			pos_hint: {"right":1, "top":1}


<User>:
	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.2
			text: "Back Home"
			on_release: app.root.current = "main" 
			pos_hint: {"right":1, "bottom":1}

<Text>:
	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.2
			text: "Back Home"
			on_release: app.root.current = "main" 
			pos_hint: {"right":1, "bottom":1}

<ContactInput>:
        
	FloatLayout:
		Button:
			color: 1,1,1,1
			font_size: 25
			size_hint: 0.3,0.2
			text: "Back Home"
			on_release: app.root.current = "main" 
			pos_hint: {"right":1, "bottom":1}

""")


# Create the class for each page
class HomePage(Screen):
    pass

class Contact(Screen):
    pass

class Dial(Screen):
    pass

class User(Screen):
    pass

class Text(Screen):
    pass

class ContactInput(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(HomePage(name="main"))
screen_manager.add_widget(Contact(name="other1"))
screen_manager.add_widget(Dial(name="other2"))
screen_manager.add_widget(User(name="other3"))
screen_manager.add_widget(Text(name="other4"))
screen_manager.add_widget(ContactInput(name="c_input"))

# The class name must match the .kv file name
# 
class Main(App):
    def build(self):
      return screen_manager


# This line kept as the last line

if __name__ == '__main__':
     Main().run()




