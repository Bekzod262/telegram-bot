import telebot
from telebot import types
import sqlite3
import random

TOKEN = "8767281487:AAFHBVwwPIk_nOed1531S0a2WM_Wlh0Yp5I"

bot = telebot.TeleBot(TOKEN)

# ===== DATABASE =====
conn = sqlite3.connect("zikr.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    count INTEGER DEFAULT 0
)
""")
conn.commit()

# ===== ZIKRLAR =====
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

# ===== USER TEKSHIRISH =====
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (user_id, count) VALUES (?, ?)", (user_id, 0))
        conn.commit()

# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("1", "2", "3")
    markup.add("4", "5", "6")
    markup.add("7", "8", "9", "10")
    markup.add("🎲 Random", "📊 Statistika", "🛑 Stop")

    bot.send_message(
        message.chat.id,
        "👋 Salom!\n\n📿 Zikr botga xush kelibsiz!\n\n👇 Tanlang:",
        reply_markup=markup
    )

# ===== HANDLER =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text or ""
    user_id = message.from_user.id

    get_user(user_id)

    # ===== ZIKR =====
    if text in zikrlar:
        cursor.execute("UPDATE users SET count = count + 1 WHERE user_id=?", (user_id,))
        conn.commit()

        cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
        count = cursor.fetchone()[0]

        bot.send_message(
            message.chat.id,
            f"📿 {zikrlar[text]}\n\n✅ Soni: {count}"
        )

    # ===== RANDOM =====
    elif text == "🎲 Random":
        zikr = random.choice(list(zikrlar.values()))
        bot.send_message(message.chat.id, f"🎲 {zikr}")

    # ===== STATISTIKA =====
    elif text == "📊 Statistika":
        cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
        count = cursor.fetchone()[0]

        bot.send_message(
            message.chat.id,
            f"📊 Siz {count} ta zikr aytdingiz\n\n😊 Siz uchun xursandman!"
        )

    # ===== STOP =====
    elif text == "🛑 Stop":
        cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
        count = cursor.fetchone()[0]

        bot.send_message(
            message.chat.id,
            f"🛑 To‘xtatildi\n\n📊 Jami: {count}\n\n😊 Siz uchun xursandman!"
        )

    else:
        bot.send_message(message.chat.id, "❗ Iltimos tugmalardan foydalaning")

# ===== RUN =====
print("Bot ishlayapti...")
bot.polling(none_stop=True)