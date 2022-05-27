
import telebot
from telebot import types
from time import sleep
import emoji
# 👉 🙏 👆 👇 😅 👋 🙌 ✅ ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻

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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('👨‍💻Начнем')
    btn2 = types.KeyboardButton('Об авторе курса')
    btn3 = types.KeyboardButton('Содержание')
    markup.add(btn1, btn2, btn3)
    #sti_0 = open('logo.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti_0)
    send_mess = f"👋 Доброго времени, *{message.from_user.first_name}*!\n\nРад Вас приветствовать на моем авторском курсе *'NameTesting'*.\n\n" \
                f"Надеюсь курс получился информативным и полезным для вас, буду рад, если в конце Вы заполните Google форму с обратной связью.\n" \
                f" 🥳 *Hello, World - Давайте начинать!*"
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Об авторе курса":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ссылка teletype", url="https://kitelab.pro/ru"))
        final_message = "Я решил, что так будет проще."

    if get_message_bot == "👨‍💻Начнем":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

        btn1 = types.KeyboardButton("Как Python связан с телеграм?")
        btn2 = types.KeyboardButton("Если я ничего не знаю о Python?")
        btn3 = types.KeyboardButton("Содержание")
        markup.add(btn1, btn2, btn3)

        send_mess = "Рaсскажу чуть подробнее о курсе..Будем вести разработку на Языке Python"
        bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

    # Штука позволяющая дать пользователю ссылки на курс языка Pyhton
    if get_message_bot == "Я ничего не знаю о Python!":
        sti = open('bimo.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        markup1 = types.InlineKeyboardMarkup()
        first_message = "В рамках, этого курса мы не планируем изучать базу языка Python, поэтому я собрал для вас ссылки на хорошие бексплатные материалы доступные в интернете:"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("1. Школа BEEGEEK: 'Поколение Python' ", url="https://stepik.org/course/58852/info"))
        second_message = "Курс – победитель конкурса Stepik Awards 2020 в номинации\n" \
                        "*'Лучший бесплатный онлайн-курс размещенный на платформе Stepik'*.\n" \
                        "Время прохождения курса: *38 часов*\n" \
                        "Язык: *Русский*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton("2. Университет ИТМО: 'Программирование на Python' ", url="https://stepik.org/course/67/syllabus"))
        third_message = "Институт биоинформатики, Университет ИТМО\n" \
                        "Нагрузка: *3-6 часов в неделю*\n" \
                        "Время прохождения курса: *19 часов*\n" \
                        "Язык: *Русский*"
        bot.send_message(message.chat.id, third_message, parse_mode='Markdown', reply_markup=markup3)
        sleep(0.5)


        markup4 = types.InlineKeyboardMarkup()
        markup4.add(types.InlineKeyboardButton("3. Учим Python за 1 час!", url="https://www.youtube.com/watch?v=fp5-XQFr_nk&t=964s"))
        fourth_message = "Часовая YouTube лекция самых \n" \
                        "основных функций языка Python.\n" \
                        "Aвторский канал:\n" \
                        "'Хауди Хо™ - Просто о мире IT!' "
        bot.send_message(message.chat.id, fourth_message, parse_mode='html', reply_markup=markup4)
        sleep(0.5)

        markup5 = types.InlineKeyboardMarkup()
        markup5.add(types.InlineKeyboardButton("4. Курс лекций Профессора МФТИ", url="https://www.youtube.com/watch?v=KdZ4HF1SrFs"))
        fifth_message = "Прекраснейшие видео лекции с очень чательным разбором всех мелочей, от великолепного:\n" \
                        " *Тимофея Хирьянова*\n" \
                        "*преподаватель кафедры информатики МФТИ* "
        bot.send_message(message.chat.id, fifth_message, parse_mode='Markdown', reply_markup=markup5)
        sleep(0.5)



    if get_message_bot == "Начнем!":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Как Python связан с телеграм?")
        btn2 = types.KeyboardButton("Если я ничего не знаю о Python?")
        btn3 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2, btn3)
        send_mess = "Рaсскажу чуть подробнее о курсе..Будем вести разработку на Языке Python"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup1)

    # end main

    # Содержание
    if get_message_bot == "Содержание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1. Вступление')
        btn2 = types.KeyboardButton('2. Получение token')
        btn3 = types.KeyboardButton('3. Функция "star"')
        btn4 = types.KeyboardButton('4. Про buttons')
        btn5 = types.KeyboardButton('5. Добавление ссылок')
        btn6 = types.KeyboardButton('6. Отправляем файлы')
        btn7 = types.KeyboardButton('7. Подключаем к CRM')
        btn8 = types.KeyboardButton('8. Работа с СБД')
        btn9 = types.KeyboardButton('0. Содержание')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_dice(message.chat.id, reply_markup=markup)


    if get_message_bot == "1. Вступление":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('👨‍💻Начнем')
        btn2 = types.KeyboardButton('Об авторе курса')
        btn3 = types.KeyboardButton('Содержание')
        markup.add(btn1, btn2, btn3)
        send_mess = "*"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    # END Содержание




bot.polling(none_stop=True)

# message.reply("text") - ответить на сообщение
