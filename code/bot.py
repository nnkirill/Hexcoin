import telebot
bot=telebot.TeleBot('7014815470:AAFme-eowMQBXobd_zw6-zdY0qOSHHX3HSc')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Иди в пенёчек, пожалуйста😘')






bot.infinity_polling()