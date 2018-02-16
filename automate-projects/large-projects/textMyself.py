#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

accountSID = 'AC9128e86a633ccb097cd4ef6f42034b34' 
authToken = '74f61dd527b2b5f2412a61d5d3fcab75'
twilioNumber = '+14056731517'
myNumber = '+14058330559'

from twilio.rest import Client

def textmyself(message):
	twilioCli = Client(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)