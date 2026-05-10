from  telegram.ext import *

async def start(update, context):

    await
update.message.reply_text("Salom")
    await
update.message.reply_text("Ismingizni kiriting: ")
    await

async def chat(update, context):

    ism = update.message.text


    await update.message.reply_text(f"salom {ism} aka qalaysiz")

    await update.message.reply_text("Yoshingiz nechida?")

app = 
ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").bu ild()

app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling
    