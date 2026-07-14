import os
import google.generativeai as genai
from telegram.ext import Application, MessageHandler, filters

# "AQ" bilan boshlanadigan json faylingizni main.py bilan bir papkaga qo'ying
# va nomini "key.json" deb o'zgartiring!
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# Bu kod to'g'ridan-to'g'ri fayl orqali ulanadi
model = genai.GenerativeModel("gemini-1.5-flash")

async def handle_message(update, context):
    try:
        response = model.generate_content(update.message.text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Bobojon, uzr, kod xatolik berdi.")

app = Application.builder().token("8960719550:AAEb6GMcGpLIK4-FthfgEdn6dH5SdR6D0lE").build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()