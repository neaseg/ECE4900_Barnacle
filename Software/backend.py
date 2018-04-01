from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)

def send_sms(number,message):
    try:
        client.api.account.messages.create(
            to=number,
            from_="+13522928542",
            body=message)
    except Exception as e:
        raise
    else:
        client.api.account.messages.create(
            to="+16148057073",
            from_="+13522928542",
            body="Message did not send")
