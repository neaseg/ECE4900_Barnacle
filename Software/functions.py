#This is the Backend of the TIMBER code


# Order of Operations
1. The press of a button on the bluetooth feater sends a signal via bluetooth to the android phone
2. The signal is receieved and accepeted by the android phone App
3. The App then sends out a prerecorded text message to a list of Contacts

4. The phone recieves a text message then sends a signal back to the bluetooth device
5. The device then plays a noise to notify the client that the message has been sent and receieved


from kivy.app import App
from kivy.uix.label import Label
from kivy uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Create a list of contacts (from the phone)

class Contact(object):
    name = "";
    number = "";
    message = "";

    def __init__(self, name, number, message):
        self.name = name
        self.number = number
        self.message = message


class EnterContact(GridLayout):
        def __init__(self, **kwargs):
            super(EnterContact,self).__init__(**kwargs)
            self.cols =2

            self.add_widget(Label(text="Contact Name:"))
            self.contact_name = TextInput(multiline=False)
            self.add_widget(self.contact_name)

            self.add_widget(Label(text="Contact Number:"))
            self.contact_number = TextInput(multiline=False)
            self.add_widget(self.contact_number)

            self.add_widget(Label(text="Message for Contact:"))
            self.message = TextInput(multiline=True)
            self.add_widget(self.message)


def make_Contact(name,number,message):
    contact = Contact(name,number,message)
    return contact

def send_sms(contact_list):
    for x in contact_list:
        plyver.sms(x.number,x.message)



new object Contact
        contact's name
        contact's number
        message to be sent to contact


send sms
        function should take in the list of objects and send out texts to all of them
        #for loop using plyver send sms
