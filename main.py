import telebot 

bot = 
telebot.TeleBot("8767281487:AAFKfLIpn9hZ2RtD_wbrs-F2dhGbEfHZKRI")


@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id,
    "Salom!\n\n"
    "1- Subhanalloh\n"
    "2- Alhamdulillah\n"
    "3- Allohu Akbar\n"
    "4- La ilaha illalloh\n"
    "5- Astaghfirulloh\n"
    "6- SubhanaLLohi va bihamdihi\n"
    "7- Subhanallohil azim\n"
    "8- La hawla wa la quwwata"
    "9- Salovat\n"
    "10- Hasbiyallohu la ilaha illa hu")

    # har qanday xabarni ushlaydi

@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text

    if text ==  "1":
        bot.send_message(message.chat.id,"Subhanalloh")
    elif text == "2":
        bot.send_message(message.chat.id,"Alhamdulilla")
    elif text ==  "3":
        bot.send_message(message.chat.id,"Allohu Akbar")
    elif text == "4":
        bot.send_message(message.chat.id,"La ilaha illalloh")
    elif  text == "5":
        bot.send_message(message.chat.id, "Astaghfirulloh")
    elif text == "6":
        bot.send_message(message.chat.id, "Subhanallohi va bihamdihi")
    elif text == "7":
        bot.send_message(message.chat.id, "Subhanallohil azim")
    elif text == "8":
        bot.send_message(message.chat.id, "La hawla wa la quwwata illa billah")
    elif text == "9":
        bot.send_message(message.chat.id, "Allohumma salli ala Muhamamd")
    elif text == "10":
        bot.send_message(message.chat.id, "Hasbiyallohu la ilaha illa hu")
    else:
        bot.send_message(message.chat.id,"Iltimos 1 dan 10 gacha son yoz")
    
    bot.polling()
                   


    
    
    
    
    
    
    
    
    
    
    
    
    
    )








































