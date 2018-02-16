from twilio.rest import Client

#15808190672 - Lance

accountSID = 'AC9128e86a633ccb097cd4ef6f42034b34' 
authToken = '74f61dd527b2b5f2412a61d5d3fcab75'
twilioCli = Client(accountSID, authToken) 
myTwilioNumber = '+14056731517'
myCellPhone = '+14058330559'
message = twilioCli.messages.create(body='PING PING PING', from_=myTwilioNumber, to=myCellPhone)