from telegram.ext import * # kod boshlanishi ekan demak bekzod >>>>>>>>>>>>lets start bekzod 
 #kichik kichik kichik mufaqatla katda galabalaga ollib keladi demak dustlarim
async def start(update, context):
# async def start(update, context): funksiya and enternet kutadi va qilla olladi demak bekzod lets start bekzod
    await update.message.reply_text("Salom 🙂")
    await update.message.reply_text("Ismingizni kiriting:")

async def chat(update, context):

    ism = update.message.text # input urnini bosadi demak bekzod 
# ism kirit deyabmiz demak  bekzod lets start bekzod (///////////>>>>>>><<<<<<<//////////)
    await update.message.reply_text(
         f"Salom {ism} aka 😎 Qalaysiz?")

async def chat(update, context):

    age = update.message.text 

    await update.message.reply_text(
        f"Sizning yoshingiz{age} aka 
    siz zurisiz okam ")

app = ApplicationBuilder().token("8767281487:AAG6T40XHhfpmvf4g4tpyIU6BPMUphx0kmc").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()
    