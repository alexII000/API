import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.authToken)

TwilioNumber='+15074163593'

MyNumber = '+15713443960'

textmessage = client.messages.create(to=MyNumber, from_=TwilioNumber,body="Fuck You")

print(textmessage.status) 