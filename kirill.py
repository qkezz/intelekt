import telebot

token = "6813041632:AAFDdSD7f5-Rv_vjFrHFPHsxJKcgqYge0Lk"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling()