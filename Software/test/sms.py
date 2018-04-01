# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty

# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)


Builder.load_string('''
<SmsInterface>:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: sp(30)
        Label:
            text: 'Recipient:'
        TextInput:
            id: recipient
            multiline: False
            on_text_validate: message.focus = True
            input_filter: 'int'
    BoxLayout:
        Label:
            text: 'Message:'
        TextInput:
            id: message
    IntentButton:
        sms_recipient: recipient.text
        sms_message: message.text
        text: 'Send SMS'
        size_hint_y: None
        height: sp(40)
        on_release: self.send_sms()
''')


class SmsInterface(BoxLayout):
    pass


class IntentButton(Button):
    sms_recipient = StringProperty()
    sms_message = StringProperty()

    def send_sms(self, *args):
	client.api.account.messages.create(
    	to=self.sms_recipient,
    	from_=self.sms_message,
    	body="Does this work? (This was sent from Ben's Computer)")

class SmsApp(App):
    def build(self):
        return SmsInterface()

if __name__ == "__main__":
    SmsApp().run()