#pylint:disable=W0612
#pylint:disable=W0611
from telebot import TeleBot
import  os, sys

TOKEN = '1758541311:AAGakFlxSKMjewDdWA-jlwNpe1FrgR4HFX4' # token api

class TelBot:
	debug = False
	def __init__(self, __token):
		self.__Token = __token
		self.__bot = TeleBot(self.__Token)
#--------#
	def auto_reply(self, message, answer):
		@self.__bot.message_handler(commands=[message])
		def handle_message(message):
			self.__bot.send_message(message.chat.id, answer)
			if self.debug == True:
				print(f"\nid : {message.chat.id}\nmessage : {message.text}\nanswer : {answer}")
#--------#
	def start_polling(self, timeout=0):
		self.__bot.polling(self, timeout)
		while True:
			pass
#--------#
def main():
	bot1 = TelBot(TOKEN)
	os.system('clear')
	bot1.debug = True
	bot1.auto_reply('start', 'BOT AKTIF')
	bot1.start_polling(timeout=5)
	
if __name__ == '__main__':
	main()