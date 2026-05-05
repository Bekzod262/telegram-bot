import telebot
from telebot import types
import random

TOKEN = "8767281487:AAEld5ZnA8OTPtJSDkiZJZ2tjrk5Vk0piH8"
bot = telebot.TeleBot(TOKEN)

# userlar uchun counter
user_count = {}

zikrlar = {
    "1": "Subhanalloh",
    "2": "Alhamdulillah",
    "3": "Allohu Akbar",
    "4": "La ilaha illalloh",
    "5": "Astag‘firulloh",
    "6": "Subhanallohi va bihamdihi",
    "7": "Subhanallohil azim",
    "8": "La hawla wa la quwwata illa billah",
    "9": "Salovat",
    "10": "Hasbiyallohu la ilaha illa hu"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1","2","3")
    markup.add("4","5","6")
    markup.add("7","8","9","10")
    markup.add("Random","Statistika")

    bot.send_message(message.chat.id, "👇 Zikr tanla:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def handler(message):
    text = message.text
    user_id = message.from_user.id

    # user uchun counter ochamiz
    if user_id not in user_count:
        user_count[user_id] = 0

    # oddiy tanlov
    if text in zikrlar:
        user_count[user_id] += 1
        bot.send_message(
            message.chat.id,
            f"{zikrlar[text]} ✅\nSana: {user_count[user_id]}"
        )

    # random
    elif text == "Random":
        zikr = random.choice(list(zikrlar.values()))
        bot.send_message(message.chat.id, f"🎲 {zikr}")

    # statistika
    elif text == "Statistika":
        bot.send_message(
            message.chat.id,
            f"📊 Siz {user_count[user_id]} ta zikr aytdingiz"
        )

    else:
        bot.send_message(message.chat.id, "❗ Iltimos tugmadan tanla")

bot.polling()