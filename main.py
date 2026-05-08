from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

balans = 1100
savat = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Xush kelibsiz 🛒\n"
        "1 - Mahsulot\n"
        "2 - Balans\n"
        "3 - Qo‘shish\n"
        "4 - Ayirish\n"
        "5 - Chek\n"
        "6 - Chiqish"
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global balans, savat
    text = update.message.text.lower()

    if text == "1":
        await update.message.reply_text(
            "kepka-200\nfutbolka-300\nmuzqaymoq-100\ntelefon-800\nTanlang:"
        )

    elif text in ["kepka", "futbolka", "muzqaymoq", "telefon"]:
        narxlar = {
            "kepka": 200,
            "futbolka": 300,
            "muzqaymoq": 100,
            "telefon": 800
        }

        narx = narxlar[text]

        if balans >= narx:
            balans -= narx
            savat.append((text, narx))
            await update.message.reply_text(f"✅ Olindi. Balans: {balans}")
        else:
            await update.message.reply_text("❌ Pul yetarli emas")

    elif text == "2":
        await update.message.reply_text(f"💰 Balans: {balans}")

    elif text == "3":
        context.user_data["state"] = "add_money"
        await update.message.reply_text("Qancha qo‘shasiz?")

    elif context.user_data.get("state") == "add_money":
        try:
            summa = int(text)
            balans += summa
            context.user_data["state"] = None
            await update.message.reply_text(f"✅ Balans: {balans}")
        except:
            await update.message.reply_text("❌ Son yoz")

    elif text == "4":
        context.user_data["state"] = "minus_money"
        await update.message.reply_text("Qancha ayirasiz?")

    elif context.user_data.get("state") == "minus_money":
        try:
            summa = int(text)
            if balans >= summa:
                balans -= summa
                await update.message.reply_text(f"✅ Balans: {balans}")
            else:
                await update.message.reply_text("❌ Yetarli emas")
            context.user_data["state"] = None
        except:
            await update.message.reply_text("❌ Son yoz")

    elif text == "5":
        if not savat:
            await update.message.reply_text("🧾 Savat bo‘sh")
        else:
            msg = "🧾 Chek:\n"
            jami = 0
            for item in savat:
                msg += f"{item[0]} - {item[1]}\n"
                jami += item[1]
            msg += f"JAMI: {jami}"
            await update.message.reply_text(msg)

    elif text == "6":
        await update.message.reply_text("👋 Xayr")

    else:
        await update.message.reply_text("❌ Noto‘g‘ri buyruq")

app = ApplicationBuilder().token("8767281487:AAFdeqYyGOqmJJzZVL7HuKMfjUGBlrGvQp0").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_handler))

app.run_polling()