#pylint:disable=W0612
#pylint:disable=W0613
#pylint:disable=W0611
import sys, os
try:
	 import telebot
except ImportError as e:
	print(f"error : {e}")
	os.system("pip3 install pyTelegramBotAPI")
	import telebot

TOKEN = '1758541311:AAGakFlxSKMjewDdWA-jlwNpe1FrgR4HFX4' # token api

mybot = telebot.TeleBot(TOKEN)
os.system('clear')
print('Telegram Bot Start\n')
def auto_reply(pesan, jawab):
	@mybot.message_handler(commands=[pesan])
	def reply(pesan):
		mybot.send_message(pesan.chat.id, jawab)
		print(f"id : {pesan.chat.id}\npesan : {pesan.text}\njawaban : {jawab}\n")
		
#----------#
def main():
	auto_reply('start', 'BOT AKTIF')
	auto_reply('hallo', 'hai!...')
	auto_reply('odading', 'mang oleh!')
	mybot.polling()
	while True:
		pass

"""
perintah dengan argument
def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['yourCommand'])
def yourCommand(message):
    status = extract_arg(message.text)

"""

if __name__ == '__main__':
	main()