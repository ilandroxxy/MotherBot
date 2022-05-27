import telebot
from telebot import types
bot = telebot.TeleBot('5133235684:AAH05QIrfqh3Ph_Bj541Lha4zN4siWO2ALA')

# пример добавления ссылки
@bot.message_handler(commands=['site'])
def open_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("www.kitelab.pro", url = "https://kitelab.pro/ru"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажми на кнопку", parse_mode='html', reply_markup=markup)


#START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Содержание')
    btn2 = types.KeyboardButton('Начнем!')
    btn3 = types.KeyboardButton('Об авторе курса')
    markup.add(btn1, btn2, btn3)
    #sti_0 = open('logo.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti_0)
    send_mess = f"<b>Доброго времени, {message.from_user.first_name}</b>!\nРады видеть вас и хотим представить Telegram-бота производства KiteLab.\nПриступим к общению!\n\nСейчас нажмите."
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)




@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()


    #  main
    if get_message_bot == "Об авторе курса":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ссылка teletype", url="https://kitelab.pro/ru"))
        final_message = "Я решил, что так будет проще."

    if get_message_bot == "Начнем!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Как Python связан с телеграм?")
        btn2 = types.KeyboardButton("Я ничего не знаю о Python!")
        btn3 = types.KeyboardButton("Содержание")
        markup.add(btn1, btn2, btn3)
        send_mess = "Рaсскажу чуть подробнее о курсе..Будем вести разработку на Языке Python"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    # end main

    # contents
    if get_message_bot == "Содержание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1. Вступление')
        btn2 = types.KeyboardButton('2. Получение token')
        btn3 = types.KeyboardButton('3. Функция \n/start')
        btn4 = types.KeyboardButton('4. Вступление')
        btn5 = types.KeyboardButton('5. Вступление')
        btn6 = types.KeyboardButton('6. Вступление')
        btn7 = types.KeyboardButton('7. Вступление')
        btn8 = types.KeyboardButton('8. Вступление')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        send_mess = "*"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    if get_message_bot == "1. Вступление":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Содержание')
        btn2 = types.KeyboardButton('Начнем!')
        btn3 = types.KeyboardButton('Об авторе курса')
        markup.add(btn1, btn2, btn3)
        send_mess = "*"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


    # end contents



bot.polling(none_stop=True)

# message.reply("text") - ответить на сообщение
