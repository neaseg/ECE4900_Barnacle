#!/usr/bin/python
# import sys
# import os.path


import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create the class for each page
class HomePage(Screen):
    pass

class Contact(Screen):
    pass

class Dial(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("MainKivy.kv")


# The class name must match the .kv file name
class MainKivy(App):
    def build(self):
      return presentation


# This line kept as the last line
if __name__ == '__main__':
     MainKivy().run()
