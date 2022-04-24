from random import choice
from sec import sec
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from sel import sel
from weather import code_location, weather

state = 0
reply_keyboard = [['Инфо', 'Выбрать группу'], ['Погода в Казани', 'Случайное слово'], ['Закрыть клавиатуру']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text('Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())


def main():
    updater = Updater('5331419578:AAGQUFsR7poil4NHuE34xAvQH9RQCoXIbU0', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, text))
    updater.start_polling()
    updater.idle()


def start(update, context):
    send_photo(update, context)
    update.message.reply_text('''Сәлам! Это бот разговорного клуба SkyTat. Чтобы узнать больше о нас, \
напиши "Инфо"''', reply_markup=markup)


def kazweather(update, context):
    cod_loc = code_location('55.797444', '49.104329', 'wbRhTtLzL4Mt6mZtmqFikOuUbjvCx3tK')
    w = weather(cod_loc, 'wbRhTtLzL4Mt6mZtmqFikOuUbjvCx3tK')['сейчас']
    update.message.reply_text(f"Температура: {w['temp']}. {w['sky']}")


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Занятие начнётся через 5 мин!')


def task1(context):
    job = context.job
    context.bot.send_message(job.context, text='Не забудьте, сегодня вечером у вас занятие.')


def days(update, context, sec):
    sec += 300
    a = [0, 0, 0]
    day = sec
    while day > 0:
        day //= 86400
        a[0] += 1
    sec = sec % 86400
    a[1] = sec // 3600
    sec %= 3600
    a[2] = sec // 60
    sec %= 60
    update.message.reply_text(f"Занятие начнётся через {a[0]} дн {a[1]} ч {a[2]} мин {sec} сек")


def set_timer(update, context, day, time):
    time = f'{time.split(":")[0]}:{int(time.split(":")[1]) - 5}'
    d = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    chat_id = update.message.chat_id
    due = sec(str(d.index(day)), time)
    days(update, context, due)
    due2 = sec(str(d.index(day)), '10:00')
    context.job_queue.run_once(task, due, context=chat_id, name=str(chat_id))
    context.job_queue.run_once(task1, due2, context=chat_id, name=str(chat_id))


def send_photo(update, context):
    context.bot.send_photo(chat_id=update.message.chat.id, photo=open('tat.png', 'rb'))


def text(update, context):
    global state, markup
    if update.message.text == 'Погода в Казани':
        kazweather(update, context)
    elif update.message.text == 'Инфо':
        info(update, context)
    elif update.message.text == 'Выбрать группу':
        choose_group(update, context)
    elif update.message.text == 'Случайное слово':
        word_of_the_day(update, context)
    elif update.message.text == 'Закрыть клавиатуру':
        close_keyboard(update, context)
    if state == 1 and update.message.text in ('Замира', 'Расима', 'Ильмир', 'Римма'):
        return choose_teacher(update, context)
    elif state == 2 and [update.message.text] in time_keyboard:
        day, time = update.message.text.split()
        set_timer(update, context, day, time)
        update.message.reply_text('''Напоминание установлено''', reply_markup=markup)


def info(update, context):
    update.message.reply_text(
        'Наши контакты',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Сайт', url='https://skytat.ru')],
            [InlineKeyboardButton(text='Telegram', url='https://t.me/skytat')],
            [InlineKeyboardButton(text='Вконтакте', url='https://vk.com/skytat')],
            ])
        )


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
