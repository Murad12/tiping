import telebot

bot = telebot.TeleBot("1097106929:AAHHULbtWtNkPVeqfzSHsl0ieGDSA6gSo2g")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
