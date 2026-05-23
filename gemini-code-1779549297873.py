import telebot
import google.generativeai as genai
import os

bot = telebot.TeleBot('8708361571:AAEZlQD8WWj--90lWrgNsINTKKe8lP4Juag')
genai.configure(api_key='AIzaSyADhqQoYce0k-chheSm_ZALZ1GDdu4q2ck')
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(func=lambda message: True)
def handle_chat(message):
    try:
        response = model.generate_content(f"አንተ የቤተሰብ ረዳት ነህ። ጥያቄ: {message.text}")
        bot.reply_to(message, response.text)
    except Exception:
        bot.reply_to(message, "ይቅርታ፣ አሁን ትንሽ ችግር አጋጥሞኛል።")

bot.infinity_polling()