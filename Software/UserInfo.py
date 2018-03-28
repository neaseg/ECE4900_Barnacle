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
        self.cols = 2

	self.add_widget(Label(text="First Name:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
		
        self.add_widget(Label(text="Last Name:"))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

	self.add_widget(Button(text="Home"))
	

class SimpleKivy(App):
    def build(self):
        return LoginScreen()
class Widgets(Widget):
    pass
	

#final line
if __name__ == "__main__":
    SimpleKivy().run()
