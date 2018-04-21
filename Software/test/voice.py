# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token can be found at https://www.twilio.com/console
# Find these values at https://twilio.com/user/account
account_sid = "AC63957f26fab90921c4d410f722425ab7"
auth_token = "89191cd5fa173f9a4e4539adf33ec27c"

client = Client(account_sid, auth_token)

# Start a phone call
call = client.calls.create(
    to="+16148057073",
    from_="+13522928542",
    url="http://raw.githubusercontent.com/ulnneverknow/temp/master/danger.xml"
)

print(call.sid)
