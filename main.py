from random import choice
from sec import sec
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from sel import sel

state = 0
reply_keyboard = [['/info', '/choose_group'], ['/info', '/random_word'], ['/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text('Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())


def main():
    updater = Updater('5103166103:AAGynbQFRHdzd1VXrM6DRErTTAPkjl6uojk', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(CommandHandler('random_word', word_of_the_day))
    dp.add_handler(CommandHandler('choose_group', choose_group))
    dp.add_handler(CommandHandler('close', close_keyboard))
    dp.add_handler(MessageHandler(Filters.text, text))
    updater.start_polling()
    updater.idle()


def start(update, context):
    send_photo(update, context)
    update.message.reply_text('''Привет! Это бот школы татарского языка SkyTat. Чтобы узнать больще о нас, \
напиши /help''', reply_markup=markup)


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Занятие начнётся через 5 мин!')


def set_timer(update, context, day, time):
    time = f'{time.split(":")[0]}:{int(time.split(":")[1]) - 5}'
    d = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    chat_id = update.message.chat_id
    due = sec(str(d.index(day)), time)
    print((d.index(day), time))
    context.job_queue.run_once(task, due, context=chat_id, name=str(chat_id))
    text = f'Вернусь через {due} секунд!'
    update.message.reply_text(text)


def send_photo(update, context):
    context.bot.send_photo(chat_id=update.message.chat.id, photo=open('tat.jpeg', 'rb'))


def text(update, context):
    global state, markup
    if state == 1 and update.message.text in ('Замира', 'Расима', 'Ильмир', 'Римма'):
        return choose_teacher(update, context)
    elif state == 2 and [update.message.text] in time_keyboard:
        day, time = update.message.text.split()
        set_timer(update, context, day, '21:39')
        update.message.reply_text('''Напоминание установлено''', reply_markup=markup)


def help(update, context):
    update.message.reply_text('''Разбирайся сам''')


def info(update, context):
    update.message.reply_text('''Наш сайт: https://skytat.ru/\n
Telegram-канал https://t.me/skytat\n
Вконтакте https://vk.com/skytat''')


def word_of_the_day(update, context):
    with open('dict1.txt', 'r') as f:
        text = f.readlines()
    update.message.reply_text(choice(text))


def choose_group(update, context):
    global state
    group_keyboard = [['Замира', 'Расима'], ['Римма', 'Ильмир']]
    markup = ReplyKeyboardMarkup(group_keyboard, one_time_keyboard=True)
    update.message.reply_text('''Как зовут вашего преподавателя?''', reply_markup=markup)
    state = 1


def choose_teacher(update, context):
    global state, time_keyboard
    teacher = update.message.text
    res = sel(teacher)
    time_keyboard = [[i[0] + ' ' + i[1]] for i in res]
    markup = ReplyKeyboardMarkup(time_keyboard, one_time_keyboard=True)
    update.message.reply_text('''Когда у вас проходят занятия?''', reply_markup=markup)
    state = 2


if __name__ == '__main__':
    main()

