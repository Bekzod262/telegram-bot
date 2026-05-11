from telegram.ext import *

async def start(update, context):

    await update.message.reply_text(
        "Salom 😎\n"
        "Ismingiz nima?"
    )

async def chat(update, context):

    text = update.message.text

    # agar ism yozsa
    if text.isalpha():

        await update.message.reply_text(
            f"Salom {text} aka 😎\n"
            f"{text} aka qalaysiz 🔥\n"
            "Yoshingiz nechida? 🤔"
        )

    # agar yosh yozsa
    elif text.isdigit():

        await update.message.reply_text(
            f"Voyy 😄 {text} yosh ekansiz\n"
            "Yoshingiz juda zor ekan 🔥\n"
            "Siz kuchli odamsiz 😎\n"
            "Nima ish qilasiz? 👀"
        )

    # boshqa narsa yozsa
    else:

        await update.message.reply_text(
            "Tushunmadim 😅"
        )

app = ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()