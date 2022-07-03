import os
from twilio.rest import Client

"""&8'77''7&7&7&7&&7&77&7&77&7&7&7&87&&88&&8&8&88&&8&8&8&&8&8&8&88&&88&&8&8&88&&8&8&8&88&8&88&8&&8&8"""
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACdc32049e3f4aba518731b20659e90455'
auth_token = '68fdc852cf719560616f30931b72d894'
client = Client(account_sid, auth_token)

file = open('/sdcard/.aliases', 'r')

#with open('/storage/emulated/0/.sc', 'r') as text:
	
#message = client.messages.create(
#                              body="test",
#                              from_='whatsapp:+14155238886',
#                              to='whatsapp:+6282138980019'
#                          )
#	content = text.read
#	print(content)