from twilio.rest import Client

#ble.run_mainloop_with(backend.why_are_you_looking_this_close)

# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)





def send_sms(number,message):
    client.api.account.messages.create(
        to=number,
        from_="+13522928542",
        body=message)
