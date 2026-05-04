msg = bot.send_message(chat_id, "Savol 1")
bot.register_next_step_handler(msg,func1)

def func1(message):
    javob1 = message.text


    msg = 
bot.send_message(message.chat.id,"Savol 2")

bot.register_next_step_handler(msg,func2, javob1)

def func2(message, javob1):
    javob2 = message.text

    bot.send_message(message.chat.id, f"1 - javob: {javob1}\n2-javob:{javob2}")