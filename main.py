from telegram.ext import *
# from deb atallarkan demak bekzod it is right bekzod


async def start(update, context):
#async def start(update, context deb yozib olldik demak bekzod)

    await update.message.reply_text( 
        "Salom 😎\nIsmingiz nima?"
    )

async def chat(update, context):

    text = update.message.text # ismingiz nimma deb olldik demak bekzod lets start bekzod

    await update.message.reply_text(
        f"Voyy {text} 😄 juda zor ism ekan!"
    )

    await update.message.reply_text(
        f"{text} aka yoshingiz nechida? 🔥"

    work = update.message.reply_text(
        f"{work} siz zur ekansiz demak bekzod"
    )
    )

    await update.message.reply_text(
        "Qanday ish qilasiz? 😎"
    )

    await update.message.reply_text(
        "Siz juda zor odamsiz okam 🤣🔥"
    )

app = ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()