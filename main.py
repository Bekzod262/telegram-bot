[06.05.2026 2:47] ..: import telebot
from telebot import types
import sqlite3
import random
import threading
import time

# ===== CONFIG =====
TOKEN =  "8767281487:AAFY_jdwXxANzda3eU2xPGd1WWP1hqZpZ-E"
DB_NAME = "zikr.db"
REMINDER_INTERVAL = 3600

bot = telebot.TeleBot(TOKEN)

# ===== DATABASE =====
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    count INTEGER DEFAULT 0,
    reminder INTEGER DEFAULT 0,
    lang TEXT DEFAULT 'uz'
)
""")
conn.commit()

# ===== TEXTS =====
TEXTS = {
    "uz": {
        "welcome": "👋 Salom!\n📿 Zikr botga xush kelibsiz!",
        "choose_lang": "🌐 Tilni tanlang:",
        "count": "📊 Siz {count} ta zikr aytdingiz",
        "top": "🏆 TOP 5:\n",
        "reminder_on": "🔔 Reminder yoqildi",
        "reminder_off": "🔕 Reminder o‘chirildi",
        "use_buttons": "❗ Tugmalardan foydalan",
        "reminder_msg": "🔔 Zikr aytishni unutmang 📿"
    },
    "en": {
        "welcome": "👋 Hello!\n📿 Welcome to Zikr Bot!",
        "choose_lang": "🌐 Choose language:",
        "count": "📊 You said {count} zikr",
        "top": "🏆 TOP 5:\n",
        "reminder_on": "🔔 Reminder enabled",
        "reminder_off": "🔕 Reminder disabled",
        "use_buttons": "❗ Use buttons",
        "reminder_msg": "🔔 Don't forget to do zikr 📿"
    }
}

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

# ===== FUNCTIONS =====
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (user_id, count, reminder, lang) VALUES (?, 0, 0, 'uz')",
            (user_id,)
        )
        conn.commit()

def get_lang(user_id):
    cursor.execute("SELECT lang FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()[0]

def set_lang(user_id, lang):
    cursor.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, user_id))
    conn.commit()

def t(user_id, key, **kwargs):
    lang = get_lang(user_id)
    return TEXTS[lang][key].format(**kwargs)

def keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("1","2","3")
    kb.add("4","5","6")
    kb.add("7","8","9","10")
    kb.add("🎲 Random","📊 Statistika")
    kb.add("🏆 Top","🔔 Reminder ON","🔕 Reminder OFF")
    kb.add("🌐 Language")
    return kb

def lang_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🇺🇿 Uzbek","🇬🇧 English")
    return kb

# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    get_user(message.from_user.id)
    bot.send_message(message.chat.id, TEXTS["uz"]["choose_lang"], reply_markup=lang_kb())

# ===== HANDLER =====
@bot.message_handler(func=lambda m: True)
def handler(message):
    user_id = message.from_user.id
    text = message.text or ""

    get_user(user_id)

    if text == "🇺🇿 Uzbek":
        set_lang(user_id, "uz")
        bot.send_message(message.chat.id, t(user_id,"welcome"), reply_markup=keyboard())

    elif text == "🇬🇧 English":
        set_lang(user_id, "en")
        bot.send_message(message.chat.id, t(user_id,"welcome"), reply_markup=keyboard())

    elif text == "🌐 Language":
        bot.send_message(message.chat.id, t(user_id,"choose_lang"), reply_markup=lang_kb())

    elif text in zikrlar:
        cursor.execute("UPDATE users SET count=count+1 WHERE user_id=?", (user_id,))
        conn.commit()

        count = cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
        bot.send_message(message.chat.id, f"📿 {zikrlar[text]}\n✅ {count}")

    elif text == "📊 Statistika":
        count = cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
        bot.send_message(message.chat.id, t(user
[06.05.2026 2:47] ..: _id,"count", count=count))

    elif text == "🏆 Top":
        top = cursor.execute("SELECT user_id, count FROM users ORDER BY count DESC LIMIT 5").fetchall()
        msg = t(user_id,"top")
        for i, u in enumerate(top, 1):
            msg += f"{i}. ID:{u[0]} — {u[1]}\n"
        bot.send_message(message.chat.id, msg)

    elif text == "🔔 Reminder ON":
        cursor.execute("UPDATE users SET reminder=1 WHERE user_id=?", (user_id,))
        conn.commit()
        bot.send_message(message.chat.id, t(user_id,"reminder_on"))

    elif text == "🔕 Reminder OFF":
        cursor.execute("UPDATE users SET reminder=0 WHERE user_id=?", (user_id,))
        conn.commit()
        bot.send_message(message.chat.id, t(user_id,"reminder_off"))

    elif text == "🎲 Random":
        bot.send_message(message.chat.id, "🎲 " + random.choice(list(zikrlar.values())))

    else:
        bot.send_message(message.chat.id, t(user_id,"use_buttons"))

# ===== REMINDER =====
def reminder():
    while True:
        users = cursor.execute("SELECT user_id FROM users WHERE reminder=1").fetchall()
        for u in users:
            try:
                bot.send_message(u[0], t(u[0], "reminder_msg"))
            except:
                pass
        time.sleep(REMINDER_INTERVAL)

threading.Thread(target=reminder, daemon=True).start()

# ===== RUN =====
print("Bot ishlayapti...")
bot.infinity_polling()