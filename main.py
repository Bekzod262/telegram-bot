from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

balanslar = {}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    balanslar[user_id] = 1000

    await update.message.reply_text(
        f"Assalomu alleykum {update.message.from_user.first_name}\n"
        f"Mini Market botga xush kelibsiz 😎\n\n"
        f"1 - Tovarlar\n"
        f"2 - Balans\n"
        f"3 - Balans qo‘shish\n"
        f"4 - Balans ayirish\n"
        f"5 - Market haqida"
    )

# MESSAGE
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    text = update.message.text

    if user_id not in balanslar:
        balanslar[user_id] = 500

    # 1
    if text == "1":
        await update.message.reply_text(
            "Tovarlar:\n"
            "Kepka\n"
            "Futbolka\n"
            "Marojni\n"
            "Komputer\n"
            "Telfone\n"
            "Ruchka"
        )

    # 2
    elif text == "2":
        await update.message.reply_text(
            f"Sizning balansingiz: {balanslar[user_id]}"
        )

    # 3
    elif text.startswith("3 "):
        summa = int(text.split()[3])
        balanslar[user_id] += summa

        await update.message.reply_text(
            f"{summa} qo‘shildi ✅\n"
            f"Yangi balans: {balanslar[user_id]}"
        )

    # 4
    elif text.startswith("4 "):
        summa = int(text.split()[1])
        balanslar[user_id] -= summa

        await update.message.reply_text(
            f"{summa} ayirildi ❌\n"
            f"Yangi balans: {balanslar[user_id]}"
        )

    # 5
    elif text == "5":
        await update.message.reply_text(
            "Bizning market eng zo‘r market jigar 😎🔥"
        )

    else:
        await update.message.reply_text(
            "Noto‘g‘ri buyruq 😅"
        )

# MAIN
app = Application.builder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_handler))

print("Bot ishga tushdi 😎")

app.run_polling()