import telebot
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
        "reminder_msg": "🔔 Don't forget zikr 📿"
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
    cursor.execute(
        "SELECT user_id FROM users WHERE user_id=?",
        (user_id,)
    )

    if cursor.fetchone() is None:
        cursor.execute("""
        INSERT INTO users (user_id, count, reminder, lang)
        VALUES (?, 0, 0, 'uz')
        """, (user_id,))

        conn.commit()


def get_lang(user_id):
    cursor.execute(
        "SELECT lang FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "uz"


def set_lang(user_id, lang):
    cursor.execute(
        "UPDATE users SET lang=? WHERE user_id=?",
        (lang, user_id)
    )

    conn.commit()


def t(user_id, key, **kwargs):
    lang = get_lang(user_id)
    return TEXTS[lang][key].format(**kwargs)


def keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("1", "2", "3")
    kb.row("4", "5", "6")
    kb.row("7", "8", "9", "10")

    kb.row("🎲 Random", "📊 Statistika")
    kb.row("🏆 Top")
    kb.row("🔔 Reminder ON", "🔕 Reminder OFF")
    kb.row("🌐 Language")

    return kb


def lang_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("🇺🇿 Uzbek", "🇬🇧 English")

    return kb


# ===== REMINDER =====
def reminder_loop():
    while True:
        time.sleep(REMINDER_INTERVAL)

        cursor.execute(
            "SELECT user_id, lang FROM users WHERE reminder=1"
        )

        users = cursor.fetchall()

        for user_id, lang in users:
            try:
                bot.send_message(
                    user_id,
                    TEXTS[lang]["reminder_msg"]
                )

            except:
                pass


threading.Thread(
    target=reminder_loop,
    daemon=True
).start()


# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    get_user(user_id)

    bot.send_message(
        message.chat.id,
        TEXTS["uz"]["choose_lang"],
        reply_markup=lang_keyboard()
    )


# ===== MAIN HANDLER =====
@bot.message_handler(func=lambda message: True)
def handler(message):

    user_id = message.from_user.id
    text = message.text

    get_user(user_id)

    # ===== LANGUAGE =====
    if text == "🇺🇿 Uzbek":

        set_lang(user_id, "uz")

        bot.send_message(
            message.chat.id,
            t(user_id, "welcome"),
            reply_markup=keyboard()
        )

    elif text == "🇬🇧 English":

        set_lang(user_id, "en")

        bot.send_message(
            message.chat.id,
            t(user_id, "welcome"),
            reply_markup=keyboard()
        )

    elif text == "🌐 Language":

        bot.send_message(
            message.chat.id,
            t(user_id, "choose_lang"),
            reply_markup=lang_keyboard()
        )

    # ===== RANDOM =====
    elif text == "🎲 Random":

        random_zikr = random.choice(
            list(zikrlar.values())
        )

        bot.send_message(
            message.chat.id,
            f"🎲 {random_zikr}"
        )

    # ===== ZIKR =====
    elif text in zikrlar:

        cursor.execute(
            "UPDATE users SET count=count+1 WHERE user_id=?",
            (user_id,)
        )

        conn.commit()

        count = cursor.execute(
            "SELECT count FROM users WHERE user_id=?",
            (user_id,)
        ).fetchone()[0]

        bot.send_message(
            message.chat.id,
            f"📿 {zikrlar[text]}\n\n✅ {count}"
        )

    # ===== STATISTIKA =====
    elif text == "📊 Statistika":

        count = cursor.execute(
            "SELECT count FROM users WHERE user_id=?",
            (user_id,)
        ).fetchone()[0]

        bot.send_message(
            message.chat.id,
            t(user_id, "count", count=count)
        )

    # ===== TOP =====
    elif text == "🏆 Top":

        top_users = cursor.execute("""
        SELECT user_id, count
        FROM users
        ORDER BY count DESC
        LIMIT 5
        """).fetchall()

        msg = t(user_id, "top")

        for i, user in enumerate(top_users, start=1):
            msg += f"\n{i}. ID: {user[0]} — {user[1]}"

        bot.send_message(
            message.chat.id,
            msg
        )

    # ===== REMINDER ON =====
    elif text == "🔔 Reminder ON":

        cursor.execute(
            "UPDATE users SET reminder=1 WHERE user_id=?",
            (user_id,)
        )

        conn.commit()

        bot.send_message(
            message.chat.id,
            t(user_id, "reminder_on")
        )

    # ===== REMINDER OFF =====
    elif text == "🔕 Reminder OFF":

        cursor.execute(
            "UPDATE users SET reminder=0 WHERE user_id=?",
            (user_id,)
        )

        conn.commit()

        bot.send_message(
            message.chat.id,
            t(user_id, "reminder_off")
        )

    # ===== UNKNOWN =====
    else:

        bot.send_message(
            message.chat.id,
            t(user_id, "use_buttons")
        )


# ===== RUN =====
print("Bot ishga tushdi...")

bot.infinity_polling()