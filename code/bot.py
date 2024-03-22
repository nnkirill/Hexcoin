import telebot
import time
import func
import mining
bot=telebot.TeleBot('7014815470:AAFme-eowMQBXobd_zw6-zdY0qOSHHX3HSc')
user = func.User(0, 1)
print(user.stonks)
mining.t1.start()



@bot.message_handler(commands=['start'])
def start_message(message):

    global user
    user = func.User(message.chat.id, 1)
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('id')
    item2 = telebot.types.KeyboardButton('баланс')
    item3 = telebot.types.KeyboardButton('создать новые ключи')

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,"вы всегда можете прочитать инструкцию, нужно просто написать \i", reply_markup=markup)
    bot.send_message(message.chat.id,"аккаунт успешно создан")
    bot.send_message(message.chat.id,f"ваш пароль: {func.find_self_chat(message.chat.id).password}", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
    global user

    def keys(message):
        if message.text == func.find_self_chat(message.chat.id).password:
            func.find_self_chat(message.chat.id).create_keys()    

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('id')
            item2 = telebot.types.KeyboardButton('баланс')
            item3 = telebot.types.KeyboardButton('отправить денег')
            item4 = telebot.types.KeyboardButton('ферма')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id,"успешно", reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'неверный пароль')


    def send(message):
        ammount = ''
        for i in message.text:
            if i == ' ':
                break
            ammount += i
        if int(ammount) <= func.find_self_chat(message.chat.id).balance:
            bot.send_message(message.chat.id, 'отправленно')
            func.User.send_money(self=func.find_self_chat(message.chat.id), message=float(ammount), recipient_id=message.text[len(str(ammount))+1::])
            func.find_self_chat(message.chat.id).balance -= ammount
        else:
            bot.send_message(message.chat.id, 'недостаточно средств')

    if message.text == 'id':
        bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).id)

    if message.text == 'баланс':
        bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).balance)

    if message.text == 'создать новые ключи':
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'ваш пароль'),keys)

    if message.text == 'отправить денег':
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'сколько, id получателя:'),send)

    if message.text  == 'ферма':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('макс. мощность')
        item2 = telebot.types.KeyboardButton('мощность')
        item3 = telebot.types.KeyboardButton('охлаждение')
        item4 = telebot.types.KeyboardButton('улучшить ферму')
        item5 = telebot.types.KeyboardButton('цены')
        item6 = telebot.types.KeyboardButton('назад')
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(message.chat.id, '--------------------', reply_markup=markup)
        
        
    if message.text  == 'макс. мощность':
        bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).count_max_stonks())

    if message.text  == 'мощность':
        bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).stonks)

    if message.text  == 'охлаждение':
        bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).cooling)

    if message.text  == 'улучшить ферму':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('мощность + 1')
        item2 = telebot.types.KeyboardButton('охлаждение + 1')
        item3 = telebot.types.KeyboardButton('хватит')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '--------------------', reply_markup=markup)

    if message.text  == 'цены':
        bot.send_message(message.chat.id, '1 единица мощьностьи = 100h, 2 А/мин \n 1 единица охлаждения = 70h, 1 A/мин \n 1 А/мин = 1h')

    if message.text  == 'назад':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('id')
        item2 = telebot.types.KeyboardButton('баланс')
        item3 = telebot.types.KeyboardButton('отправить денег')
        item4 = telebot.types.KeyboardButton('ферма')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '--------------------', reply_markup=markup)

    if message.text  == 'мощность + 1':
        if func.find_self_chat(message.chat.id).count_max_stonks() >= 1:
            if func.find_self_chat(message.chat.id).balance > 70:
                func.find_self_chat(message.chat.id).buy_stonks()
                bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).stonks)
            else:
                bot.send_message(message.chat.id, 'недостаточно средств')
        else:
            bot.send_message(message.chat.id, 'мало охлаждения')

    if message.text  == 'охлаждение + 1':
        if func.find_self_chat(message.chat.id).balance > 100:
            func.find_self_chat(message.chat.id).buy_cooling()
            bot.send_message(message.chat.id, func.find_self_chat(message.chat.id).cooling)
        else:
            bot.send_message(message.chat.id, 'недостаточно средств')

    if message.text  == 'хватит':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('id')
        item2 = telebot.types.KeyboardButton('баланс')
        item3 = telebot.types.KeyboardButton('отправить денег')
        item4 = telebot.types.KeyboardButton('ферма')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '--------------------', reply_markup=markup)


    if message.text == '\i':
        bot.send_message(message.chat.id, 'в разработке.....')
bot.infinity_polling()
func.close_data()