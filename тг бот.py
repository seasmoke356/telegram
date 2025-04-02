import telebot
from telebot import types
bot = telebot.TeleBot('7656215409:AAGS95NO_EhoexecI9n1APCd5FKLKDFLYOA')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("привет!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я бот-помощник для школьников", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'привет!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('помоги с дз')
        btn2 = types.KeyboardButton('помоги подготовиться к ВПР')
        btn3 = types.KeyboardButton('помоги с ОГЭ\ЕГЭ')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'помоги с дз':
        bot.send_message(message.from_user.id, 'сайт гдз можно найти по ' + '[ссылке](https://gdz.ru/)', parse_mode='Markdown')

    elif message.text == 'помоги подготовиться к ВПР':
        bot.send_message(message.from_user.id, 'пробники ВПР ты сможешь найти по ' + '[ссылке](https://vpr.sdamgia.ru/prob_catalog)', parse_mode='Markdown')

    elif message.text == 'помоги с ОГЭ\ЕГЭ':
        bot.send_message(message.from_user.id, 'пробники ОГЭ\ЕГЭ ты сможешь найти по ' + '[ссылке](https://sdamgia.ru/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть