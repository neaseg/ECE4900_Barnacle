import kivy

from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

#Classes per Page
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 4

	self.add_widget(Label(text="Your loved one is in distress, and needs immediate medical attention", size_hint_x=None, width = 500))
	self.add_widget(Button(text="Select"))

	self.add_widget(Label(text="An individual is in distress and seeks immediate medical attention", size_hint_x=None, width = 500))
	self.add_widget(Button(text="Select"))

	self.add_widget(Label(text="The user has collapsed and requires immediate medical attention",size_hint_x=None, width = 500))
	self.add_widget(Button(text="Select"))

	self.add_widget(TextInput(multiline=False, size_hint_x=None, width=500))
	self.add_widget(Button(text="Select"))

class SimpleKivy(App):
    def build(self):
        return LoginScreen()
class Widgets(Widget):
    pass
	

#final line
if __name__ == "__main__":
    SimpleKivy().run()
