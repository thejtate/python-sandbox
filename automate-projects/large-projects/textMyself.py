#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

accountSID = 'xxxxxxxxxxxx' 
authToken = 'xxxxxxxxxxx'
twilioNumber = '+xxxxxxxxxxxx'
myNumber = '+xxxxxxxxxxxx'

from twilio.rest import Client

def textmyself(message):
	twilioCli = Client(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)