import telebot
from telebot import types
import random
import sqlite3

TOKEN = '8767281487:AAHEBRJwawCgP9dmsuCd61yQHMWhL0pIzjE"
bot = telebot.TeleBot(TOKEN)

# DATABASE
conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    count INTEGER
)
""")
conn.commit()

# ZIKRLAR
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

# USERNI OLISH/YARATISH
def get_user(user_id):
    cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, 0))
        conn.commit()
        return 0
    return user[0]

# COUNT UPDATE
def update_count(user_id):
    cursor.execute("UPDATE users SET count = count + 1 WHERE user_id=?", (user_id,))
    conn.commit()

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1", "2", "3")
    markup.add("4", "5", "6")
    markup.add("7", "8", "9", "10")
    markup.add("🎲 Random", "📊 Statistika")
    markup.add("🛑 Stop")

    bot.send_message(
        message.chat.id,
        "👋 Assalomu alaykum!\n\n"
        "📿 Bu Zikr Bot.\n\n"
        "👇 Quyidagilardan birini tanlang:\n"
        "• Raqam bosib zikr ayting\n"
        "• 🎲 Random — tasodifiy zikr\n"
        "• 📊 Statistika — hisobingiz\n"
        "• 🛑 Stop — yakunlash",
        reply_markup=markup
    )

# HANDLER
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text
    user_id = message.from_user.id

    count = get_user(user_id)

    # ZIKR
    if text in zikrlar:
        update_count(user_id)
        count += 1

        bot.send_message(
            message.chat.id,
            f"✅ {zikrlar[text]}\n\n📿 Soni: {count}"
        )

    # RANDOM
    elif text == "🎲 Random":
        zikr = random.choice(list(zikrlar.values()))
        bot.send_message(message.chat.id, f"🎯 {zikr}")

    # STATISTIKA
    elif text == "📊 Statistika":
        bot.send_message(
            message.chat.id,
            f"📊 Siz {count} ta zikr aytdingiz"
        )

    # STOP
    elif text == "🛑 Stop":
        bot.send_message(
            message.chat.id,
            f"🤝 Siz {count} ta zikr aytdingiz.\n\n😊 Siz uchun xursandman!"
        )

    else:
        bot.send_message(
            message.chat.id,
            "❗ Iltimos tugmalardan foydalaning"
        )

bot.polling()