[06.05.2026 2:41] ..: import telebot
from telebot import types
import sqlite3
import random
import threading
import time
import logging

# ===== CONFIG =====
TOKEN = "8767281487:AAFY_jdwXxANzda3eU2xPGd1WWP1hqZpZ-E"
DB_NAME = "zikr.db"
REMINDER_INTERVAL = 3600

logging.basicConfig(level=logging.INFO)

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

# ===== BOT CLASS =====
class ZikrBot:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

        self.zikrlar = {
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

        self._create_table()
        self._register_handlers()

    # ===== DATABASE =====
    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            count INTEGER DEFAULT 0,
            reminder INTEGER DEFAULT 0,
            lang TEXT DEFAULT 'uz'
        )
        """)
        self.conn.commit()

    def get_user(self, user_id):
        with self.lock:
            self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
            user = self.cursor.fetchone()

            if not user:
                self.cursor.execute(
                    "INSERT INTO users (user_id, count, reminder, lang) VALUES (?, 0, 0, 'uz')",
                    (user_id,)
                )
                self.conn.commit()

    def get_lang(self, user_id):
        self.cursor.execute("SELECT lang FROM users WHERE user_id=?", (user_id,))
        return self.cursor.fetchone()[0]

    def set_lang(self, user_id, lang):
        with self.lock:
            self.cursor.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, user_id))
            self.conn.commit()

    def t(self, user_id, key, **kwargs):
        lang = self.get_lang(user_id)
        return TEXTS[lang][key].format(**kwargs)

    # ===== UI =====
    def get_keyboard(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("1","2","3")
        markup.add("4","5","6")
        markup.add("7","8","9","10")
        markup.add("🎲 Random","📊 Statistika")
        markup.add("🏆 Top","🔔 Reminder ON","🔕 Reminder OFF")
        markup.add("🌐 Language")
        return markup

    def lang_keyboard(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("🇺🇿 Uzbek", "🇬🇧 English")
        return markup

    # ===== HANDLERS =====
    def _register_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start(message):
            user_id = message.from_user.id
            self.get_user(user_id)

            self.bot.send_message(
                message.chat.id,
                TEXTS["uz"]["choose_lang"],
                reply_markup=self.lang_keyboard()
            )

        @self.bot.message_handler(func=lambda m: True)
        def handler(message)
[06.05.2026 2:41] ..: :
            user_id = message.from_user.id
            text = message.text or ""

            self.get_user(user_id)

            if text == "🇺🇿 Uzbek":
                self.set_lang(user_id, "uz")
                self.bot.send_message(message.chat.id, self.t(user_id, "welcome"), reply_markup=self.get_keyboard())

            elif text == "🇬🇧 English":
                self.set_lang(user_id, "en")
                self.bot.send_message(message.chat.id, self.t(user_id, "welcome"), reply_markup=self.get_keyboard())

            elif text == "🌐 Language":
                self.bot.send_message(message.chat.id, self.t(user_id, "choose_lang"), reply_markup=self.lang_keyboard())

            elif text in self.zikrlar:
                self.cursor.execute("UPDATE users SET count=count+1 WHERE user_id=?", (user_id,))
                self.conn.commit()
                count = self.cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,)).fetchone()[0]

                self.bot.send_message(message.chat.id, f"📿 {self.zikrlar[text]}\n✅ {count}")

            elif text == "📊 Statistika":
                count = self.cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
                self.bot.send_message(message.chat.id, self.t(user_id, "count", count=count))

            elif text == "🏆 Top":
                top = self.cursor.execute("SELECT user_id, count FROM users ORDER BY count DESC LIMIT 5").fetchall()
                msg = self.t(user_id, "top")

                for i, u in enumerate(top, 1):
                    msg += f"{i}. ID:{u[0]} — {u[1]}\n"

                self.bot.send_message(message.chat.id, msg)

            elif text == "🔔 Reminder ON":
                self.cursor.execute("UPDATE users SET reminder=1 WHERE user_id=?", (user_id,))
                self.conn.commit()
                self.bot.send_message(message.chat.id, self.t(user_id, "reminder_on"))

            elif text == "🔕 Reminder OFF":
                self.cursor.execute("UPDATE users SET reminder=0 WHERE user_id=?", (user_id,))
                self.conn.commit()
                self.bot.send_message(message.chat.id, self.t(user_id, "reminder_off"))

            elif text == "🎲 Random":
                zikr = random.choice(list(self.zikrlar.values()))
                self.bot.send_message(message.chat.id, f"🎲 {zikr}")

            else:
                self.bot.send_message(message.chat.id, self.t(user_id, "use_buttons"))

    # ===== REMINDER =====
    def reminder_loop(self):
        while True:
            users = self.cursor.execute("SELECT user_id FROM users WHERE reminder=1").fetchall()
            for u in users:
                try:
                    self.bot.send_message(u[0], self.t(u[0], "reminder_msg"))
                except:
                    pass
            time.sleep(REMINDER_INTERVAL)

    def run(self):
        threading.Thread(target=self.reminder_loop, daemon=True).start()
        self.bot.infinity_polling()

# ===== START =====
if __name__ == "__main__":
    ZikrBot(TOKEN).run()