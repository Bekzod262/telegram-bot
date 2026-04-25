from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN =  "8675377217:AAFp7taRDjRwg5OvV3ha9vv98RjFfcK20_k"

# user data (temporary database)
user_data = {}

# keyboard
keyboard = [
    ["➕ Zikr (+1)", "🔄 Reset"],
    ["📊 Statistika"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_data[user_id] = 0
    await update.message.reply_text(
        "🤲 Assalomu alaykum!\nZikr botga xush kelibsiz!",
        reply_markup=markup
    )

# main handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id not in user_data:
        user_data[user_id] = 0

    if text == "➕ Zikr (+1)":
        user_data[user_id] += 1
        await update.message.reply_text(f"📿 Zikr soni: {user_data[user_id]}")

    elif text == "🔄 Reset":
        user_data[user_id] = 0
        await update.message.reply_text("🔄 Zikr reset qilindi")

    elif text == "📊 Statistika":
        await update.message.reply_text(f"📊 Sizning zikrlaringiz: {user_data[user_id]}")

    else:
        await update.message.reply_text("❗ Tugmalardan foydalaning")

# run bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("✅ Bot ishlayapti...")
app.run_polling()