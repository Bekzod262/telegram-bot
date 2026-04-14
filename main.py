import telebot

TOKEN ="8576549325:AAEVJQcsY8Zuhpvzjb9gU2zWOq6zZIRglZU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom jigar ")

@bot.message_handler(func=lambda message: True)
def  echo(message):
    if message.text == "salom":
        bot.reply_to(message, "Salom jigar ")
    else:
        bot.reply_to(message, "Tushunmadim")
print("Bot ishlayapti....")  

bot.polling()


