import os
import sqlite3
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8675377217:AAFp7taRDjRwg5OvV3ha9vv98RjFfcK20_k"

# DATABASE
conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    count INTEGER DEFAULT 0
)
""")
conn.commit()

# FUNKSIYALAR
def get_count(user_id):
    cursor.execute("SELECT count FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("INSERT INTO users (user_id, count) VALUES (?, ?)", (user_id, 0))
        conn.commit()
        return 0

def update_count(user_id, value):
    cursor.execute("UPDATE users SET count=? WHERE user_id=?", (value, user_id))
    conn.commit()

# TUGMALAR
keyboard = [
    ["📿 Zikr (+1)"],
    ["📊 Statistika", "🔄 Reset"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    get_count(user_id)

    await update.message.reply_text(
        "🤲 Assalomu alaykum!\nZikr botga xush kelibsiz",
        reply_markup=markup
    )

# MESSAGE
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    count = get_count(user_id)

    if text == "📿 Zikr (+1)":
        count += 1
        update_count(user_id, count)
        await update.message.reply_text(f"📿 Zikr qabul bo‘lsin!\n📊 Sanoq: {count}")

    elif text == "📊 Statistika":
        await update.message.reply_text(f"📊 Siz {count} marta zikr qildingiz")

    elif text == "🔄 Reset":
        update_count(user_id, 0)
        await update.message.reply_text("🔄 Sanoq 0 ga tushirildi")

    else:
        await update.message.reply_text("❗ Tugmalardan foydalaning")

# RUN
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("✅ Bot ishlayapti...")
app.run_polling()