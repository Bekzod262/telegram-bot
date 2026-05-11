from telegram.ext import *

async def start(update, context):

    await update.message.reply_text(
        "Salom \n"
        "Ismingiz nima"

    )
async def chat(update, context):

    text = update.message.text

    if text.isalpha():

        await update.message.reply_text(
            f"Salom {text} aka \n"
            f"{text} aka qalaysiz"
            "Yoshingiz nechida"
        )
    elif text.isdigit():

        await update.message.reply_text(
            f"voy {text} yosh"

            "Yoshingiz juda zor ekan"

            "siz kuchli odamsiz \n"
            "Nima ish qilasiz?"
            
        )
    
    else:
        await update.message.reply_text("Tushunmadim")

app= 
ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build(s

app.add_handler(CommandHandler("start",start))

app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()