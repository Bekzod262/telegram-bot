from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8675377217:AAFp7taRDjRwg5OvV3ha9vv98RjFfcK20_k"

user_step = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_step[user_id] = 1

    await update.message.reply_text("Assalomu alaykum 🤝")
    await update.message.reply_text("Allohni birinchi o‘ringa qo‘ysang, oxirgi bo‘lmaysan 🙏")
    await update.message.reply_text("Boshlaymiz 🔥")
    await update.message.reply_text("1️⃣ 30 marta Allohu Akbar ayting va 'yes' yozing")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()

    # 🔁 restart
    if text == "/start" or text == "restart":
        user_step[user_id] = 1
        await start(update, context)
        return

    if user_id not in user_step:
        await update.message.reply_text("Avval /start bosing ❗")
        return

    step = user_step[user_id]

    # 1-step
    if step == 1:
        if text == "yes":
            user_step[user_id] = 2
            await update.message.reply_text("Zo‘r 👍")
            await update.message.reply_text("2️⃣ 30 marta Astag‘firulloh ayting va 'yes' yozing")
        else:
            await update.message.reply_text("Iltimos 'yes' yozing ❗")

    # 2-step
    elif step == 2:
        if text == "yes":
            user_step[user_id] = 3
            await update.message.reply_text("Ajoyib 🔥")
            await update.message.reply_text("3️⃣ 30 marta Alhamdulillah ayting va 'yes' yozing")
        else:
            await update.message.reply_text("Faqat 'yes' yozing ❗")

    # 3-step
    elif step == 3:
        if text == "yes":
            user_step[user_id] = 4
            await update.message.reply_text("Barakalla 👏")
            await update.message.reply_text("4️⃣ 30 marta La ilaha illallah ayting va 'ok' yozing")
        else:
            await update.message.reply_text("'yes' yozing ❗")

    # 4-step
    elif step == 4:
        if text == "ok":
            user_step[user_id] = 5
            await update.message.reply_text("Rahmat 🙏")
            await update.message.reply_text("Hayot qiyinmi? (ha/yo‘q)")
        else:
            await update.message.reply_text("'ok' yozing ❗")

    # 5-step
    elif step == 5:
        if text in ["ha", "yoq", "yo‘q"]:
            user_step[user_id] = 6
            await update.message.reply_text("Tabriklayman 🎉")
            await update.message.reply_text("Alloh yaxshi ko‘rgan bandasini sinaydi 🤲")
            await update.message.reply_text("Allohga ishonasizmi? (ha/yo‘q)")
        else:
            await update.message.reply_text("'ha' yoki 'yo‘q' yozing ❗")

    # 6-step (yakun + restart)
    elif step == 6:
        if text in ["ha", "yoq", "yo‘q"]:
            user_step[user_id] = 1  # 🔥 qayta boshlanadi

            await update.message.reply_text("To‘g‘ri yo‘ldasiz 🙏")
            await update.message.reply_text("Bu dunyo Allohniki 🤍")
            await update.message.reply_text("Yana kelishingizga ishonaman 🌟")
            await update.message.reply_text("Yana boshlaymiz 🔁")
            await update.message.reply_text("1️⃣ 30 marta Allohu Akbar ayting va 'yes' yozing")
        else:
            await update.message.reply_text("'ha' yoki 'yo‘q' yozing ❗")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()