import os

from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16692924191", 
    from_="+16692000743",
    body="ALERT!!! Potential emergency situation in the ride detected by SafeRide.AI")

print(message)