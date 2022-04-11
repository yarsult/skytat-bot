from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from random import choice


reply_keyboard = [['xxxxxxxx', 'xxxxxxxx'], ['/info', '/word_of_the_day'], ['/close']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text('Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater('5103166103:AAGynbQFRHdzd1VXrM6DRErTTAPkjl6uojk', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(CommandHandler('word_of_the_day', word_of_the_day))
    dp.add_handler(CommandHandler('close', close_keyboard))

    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text('''Привет! Я бот-справочник''', reply_markup=markup)


def help(update, context):
    update.message.reply_text('''Разбирайся сам''')


def info(update, context):
    update.message.reply_text('''Наш сайт: https://skytat.ru/\n
Telegram-канал https://t.me/skytat\n
Вконтакте https://vk.com/skytat''')


def word_of_the_day(update, context):
    with open('dict1.txt', 'r') as f:
        text = f.readlines()
    # word = choice(text).split()
    # parts = ['сущ', "гл", "пр", "нар", "посл", "мест", "числ", "вводн сл"]
    # for i in parts:
    #     if i in word:
    #         m = word.index(i)
    #         break
    # tat = word[:m]
    # noun = word[m]
    # word = ''.join(word)
    # rest = word[len(tat) + len(noun) + 6:]
    update.message.reply_text(choice(text))


if __name__ == '__main__':
    main()
