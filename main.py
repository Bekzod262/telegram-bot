from telegram.ext import *

async def start(update, context):

    await update.message.reply_text(
        "Salom \nIsmingiz nima? "
    )

async def chat(update, context):

    text = update.message.text

    await update.message.reply_text(
        f"Voyy {text} juda zor ism ekan!"
    )

    await update.message.reply_text(
        f"{text} aka yoshingiz nechida ?"
    )

    await update.message.reply_text(
        "qanday ish qilasiz? "
    )

    await update.message.reply_text(
        "siz juda zor odamsiz okam
        "
    )
app = 
ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build()

app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()