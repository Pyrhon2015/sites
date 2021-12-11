import telebot

bot = telebot.TeleBot("2141562532:AAGhz6zBwsfCqT3fDHiWW_trisRCXqfE2p4")
@bot.message_handler(content_types=['text'])
def send_echo(message):
	if message.text == "Привет":
		bot.send_message(message.chat.id, "Привет пользовотель")
bot.polling( none_stop = True )