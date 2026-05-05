import telebot
from telebot import types
import sqlite3
import random
import threading
import time

# ===== TOKEN =====
TOKEN = "8767281487:AAGk2D65jnvJYFZoyc_V1haLB2zNj5wsYlY"
bot = telebot.TeleBot(TOKEN)

# ===== DATABASE =====
conn = sqlite3.connect("zikr.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    count INTEGER DEFAULT 0,
    reminder INTEGER DEFAULT 0
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

# ===== USER =====
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute(
            "INSERT INTO users (user_id, count, reminder) VALUES (?, ?, ?)",
            (user_id, 0, 0)
        )
        conn.commit()

# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1","2","3")
    markup.add("4","5","6")
    markup.add("7","8","9","10")
    markup.add("🎲 Random","📊 Statistika")
    markup.add("🏆 Top","🔔 Reminder ON","🔕 Reminder OFF")

    bot.send_message(
        message.chat.id,
        "👋 Salom!\n📿 Zikr botga xush kelibsiz!",
        reply_markup=markup
    )

# ===== HANDLER =====
@bot.message_handler(func=lambda message: True)
def handler(message):
    text = message.text or ""
    user_id = message.from_user.id
    get_user(user_id)

    if text in zikrlar:
        cursor.execute("UPDATE users SET count=count+1 WHERE user_id=?", (user_id,))
        conn.commit()

        cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
        count = cursor.fetchone()[0]

        bot.send_message(message.chat.id, f"📿 {zikrlar[text]}\n✅ {count}")

    elif text == "🎲 Random":
        zikr = random.choice(list(zikrlar.values()))
        bot.send_message(message.chat.id, f"🎲 {zikr}")

    elif text == "📊 Statistika":
        cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
        count = cursor.fetchone()[0]
        bot.send_message(message.chat.id, f"📊 Siz {count} ta zikr aytdingiz")

    elif text == "🏆 Top":
        cursor.execute("SELECT user_id, count FROM users ORDER BY count DESC LIMIT 5")
        top = cursor.fetchall()

        msg = "🏆 TOP 5:\n"
        for i, user in enumerate(top, start=1):
            msg += f"{i}. ID:{user[0]} — {user[1]} ta\n"

        bot.send_message(message.chat.id, msg)

    elif text == "🔔 Reminder ON":
        cursor.execute("UPDATE users SET reminder=1 WHERE user_id=?", (user_id,))
        conn.commit()
        bot.send_message(message.chat.id, "🔔 Reminder yoqildi")

    elif text == "🔕 Reminder OFF":
        cursor.execute("UPDATE users SET reminder=0 WHERE user_id=?", (user_id,))
        conn.commit()
        bot.send_message(message.chat.id, "🔕 Reminder o‘chirildi")

    else:
        bot.send_message(message.chat.id, "❗ Tugmalardan foydalan")

# ===== REMINDER THREAD =====
def reminder_loop():
    while True:
        cursor.execute("SELECT user_id FROM users WHERE reminder=1")
        users = cursor.fetchall()

        for user in users:
            try:
                bot.send_message(user[0], "🔔 Zikr aytishni unutmang 📿")
            except:
                pass

        time.sleep(3600)  # 1 soat

threading.Thread(target=reminder_loop).start()

# ===== RUN =====
print("Bot ishlayapti...")
bot.polling(none_stop=True)