import telebot
import google.generativeai as genai
import os

# ከ Variables የምናገኛቸው መረጃዎች
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! እኔ የአንተ የ AI ረዳት ነኝ። የምትፈልገውን ነገር መጠየቅ ትችላለህ።")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ይቅርታ፣ አሁን ትንሽ ችግር አጋጥሞኛል።")

bot.infinity_polling()
