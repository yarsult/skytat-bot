import telebot

from telebot import types
token='2083248479:AAFLRg2g4WAw9m9otsi72edjN7NsLSvjjYE'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Выберите группу")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите, что вам надо', reply_markup=markup)

@bot.message_handler(commands=['button'])
def button_message1(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Оплата")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите, что вам надо', reply_markup=markup)

@bot.message_handler(commands=['button'])
def button_message1(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Оповещение")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите, что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Оповещение":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")

# def checkuserCommand(bot, update):
    # if update.message.from_user.id == "449977621":
      #  if update.message.text == "/start":
       #     startCommand(bot, update)

bot.infinity_polling()


