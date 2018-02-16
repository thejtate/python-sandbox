from twilio.rest import Client

#15808190672 - Lance

accountSID = 'xxxxxxxxxxxx' 
authToken = 'xxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken) 
myTwilioNumber = '+xxxxxxxxxxxx'
myCellPhone = '+xxxxxxxxxxxx'
message = twilioCli.messages.create(body='PING PING PING', from_=myTwilioNumber, to=myCellPhone)