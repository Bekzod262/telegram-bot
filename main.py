import telebot
from telebot import types
import random

TOKEN = "8767281487:AAHOR6OcqP1OP4-bx3sZa7KArbtsy5OXCP4"
bot = telebot.TeleBot(TOKEN)

# user counter
user_count = {}

# zikrlar
zikrlar = {
    "1": "Subhanalloh",
    "2": "Alhamdulillah",
    "3": "Allohu Akbar",
    "4": "La ilaha illalloh",
    "5": "Astaghfirulloh",
    "6": "Subhanallohi va bihamdihi",
    "7": "Subhanallohil azim",
    "8": "La hawla wa la quwwata illa billah",
    "9": "Salovat",
    "10": "Hasbiyallohu la ilaha illa hu"
}

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1", "2", "3")
    markup.add("4", "5", "6")
    markup.add("7", "8", "9", "10")
    markup.add("🎲 Random", "📊 Statistika")

    bot.send_message(
        message.chat.id,
        "👇 Zikr tanla:",
        reply_markup=markup
    )

# HANDLER
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text
    user_id = message.from_user.id

    # userni yaratamiz
    if user_id not in user_count:
        user_count[user_id] = 0

    # zikr bosilsa
    if text in zikrlar:
        user_count[user_id] += 1

        bot.send_message(
            message.chat.id,
            f"✅ {zikrlar[text]}\n\n📿 Soni: {user_count[user_id]}"
        )

    # random
    elif text == "🎲 Random":
        zikr = random.choice(list(zikrlar.values()))
        bot.send_message(message.chat.id, f"🎯 {zikr}")

    # statistika
    elif text == "📊 Statistika":
        bot.send_message(
            message.chat.id,
            f"📊 Siz {user_count[user_id]} ta zikr aytdingiz"
        )

    else:
        bot.send_message(message.chat.id, "❗ Tugmalardan foydalaning")

bot.polling()