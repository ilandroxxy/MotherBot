
import telebot
from telebot import types
from telebot import callback_data
from time import sleep
import emoji
# 👉 🙏 👆 👇 😅 👋 🙌 ✅ ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉

bot = telebot.TeleBot('5430380851:AAFEEwSPbUmpm5-FKBzkEUz4eCQ9BWiF_gM')


# ссылка для "Как Python связан с Telegram?"
@bot.message_handler(commands=['documentation'])
def open_documentation(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Документация Telegram API", url = "https://tlgrm.ru/docs#boty"))
    bot.send_message(message.chat.id, "✅ Это не призыв к действию, читать документацию сложно, но можно. \n"
                                      "Пробуй и подучи английский, так очевидные вещи станут еще очевиднее 😉", parse_mode='html', reply_markup=markup)

# кнопки для модуля "Что такое token?"
@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    markup = telebot.types.InlineKeyboardMarkup()

    if call.data == 'firsttoken':
        firsttoken_message = " Первая клавиша"
        msg = bot.send_message(call.message.chat.id, firsttoken_message, reply_markup = markup)
    elif call.data == 'secondtoken':
        secondtoken_message = "Вторая"
        msg = bot.send_message(call.message.chat.id, secondtoken_message, reply_markup = markup)
    elif call.data == 'thirdtoken':
        thirdtoken_message = "Третья"
        msg = bot.send_message(call.message.chat.id, thirdtoken_message, reply_markup = markup)


#START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('👨‍💻Начнем')
    btn2 = types.KeyboardButton('О авторе курса')
    btn3 = types.KeyboardButton('Содержание')
    markup.add(btn1, btn2, btn3)
    send_mess = f"👋 Доброго времени, *{message.from_user.first_name}*!\n\nРад Вас приветствовать на моем авторском курсе *'NameTesting'*.\n\n" \
                f"Надеюсь курс получился информативным и полезным для вас, буду рад, если в конце Вы заполните Google форму с обратной связью.\n" \
                f" 🥳 *Hello, World - Давайте начинать!*"
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()



    # 1. Вступление ----------------------------------------------------------------------
    if get_message_bot == "👨‍💻Начнем":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Как Python связан с Telegram?")
        btn2 = types.KeyboardButton("Если я ничего не знаю о Python?")
        btn3 = types.KeyboardButton("Содержание")
        markup.add(btn1, btn2, btn3)
        send_mess = "Рaсскажу чуть подробнее о курсе..Будем вести разработку на Языке Python"
        bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

    if get_message_bot == "О авторе курса":
        pic_1 = open('MyFace.JPG', 'rb')
        bot.send_photo(message.chat.id, pic_1)

        first_message = "👋 *Привет, меня зовут Андрианов Илья* и я программист, точнее мог бы им стать," \
                        "но мне захотелось стать преподавателем и делится с людьми знаниями.\n\n" \
                        "Этот курс подразумевается как ознакомительный и вообще получился благодаря моей Выпускной работе..😅"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown')
        sleep(0.5)
        bot.send_message(message.chat.id, "Мои контактные данные:")
        bot.send_message(message.chat.id, "Написать на почтовый ящик: *ilandroxxy@gmail.com*", parse_mode='Markdown')
        sleep(0.5)
        bot.send_message(message.chat.id, "Позвонить по номеру телефона: *+79954375259*", parse_mode='Markdown')
        sleep(0.5)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("VK", url="https://vk.com/ilandroxxy"), types.InlineKeyboardButton("WhatsApp", url="https://clck.ru/eBVga"))
        markup.add(types.InlineKeyboardButton("Telegram", url="https://t.me/ilandroxy"))
        bot.send_message(message.chat.id, "Или написать в социальных сетях: ", parse_mode='Markdown', reply_markup=markup)
        sleep(0.5)

    if get_message_bot == "Если я ничего не знаю о Python?":
        sti_1 = open('bimo.webp', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
        markup1 = types.InlineKeyboardMarkup()
        first_message = "В рамках, этого курса мы не планируем изучать базу языка Python, поэтому я собрал для вас ссылки на хорошие бексплатные материалы доступные в интернете:"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

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

    if get_message_bot == "Как Python связан с Telegram?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Что такое token?")
        btn2 = types.KeyboardButton("Хочу получить ссылку")
        btn3 = types.KeyboardButton("Содержание")
        markup.add(btn1, btn2, btn3)

        first_message = "*Telegram* это не просто популярный мессенджер, но и огромная рабочая платформа делящаяся своими " \
                    "ресурсами с другими разработчиками. Такие решения называются API и нужны они в первую очередь для интеграции" \
                    "сторонних сервисов в экосистему нашей платформы (Для тех кто уже запутался - в нашем случае это Telegram)." \
                    "Telegram имеет свое API для языка Python и позволяет нам как сторонним разработчикам делать разные действия на площадке, в том числе и ботов 🤖\n\n"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup)
        sleep(0.5)
        second_message = "Надеюсь вы уже скачали Python и Pycharm (IDE для разработки программ, не обязательное, но желательное - вам так будет удобнее) потому что мы начинаем " \
                    "подключать Telegram API к нашему пустому проекту, для этого нам нужно его скачать! Воспользуемся pip установщиком библиотек и в Terminal проекта " \
                    "введем команду: \n\n*pip install PyTelegramBotAPI* \n\nЖдем несколько секунд и вуаля, наше API уже есть в проекте, осталось только его подключить.." \
                    "Но это уже стандартная практика, через import подключаем библиотеку telebot:\n\n*import telebot*\n*from telebot import types*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown')

    if message.text == "Хочу получить ссылку":
        open_documentation(message)

    # 1. Вступление ----------------------------------------------------------------------

    # 2. Получение token ----------------------------------------------------------------------
    if get_message_bot == "Что такое token?":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Модуль Start")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Чтобы связать нашу программу и бота по сети, нужен token бота.\n" \
                        "Это специальный ключ, с помощью которого его можно подключать к сторонним сервисам. " \
                        "Token нужно сохранить и никому не показывать — он так же важен, как и пароль от почты."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Создание", callback_data ='firsttoken'),
                    types.InlineKeyboardButton("Редактирование", callback_data ='secondtoken'),
                    types.InlineKeyboardButton("Подключение", callback_data ='thirdtoken'))
        second_message = "Для получения нашего ключа, необходимо написать *@BotFather*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)







    # 2. Получение token ----------------------------------------------------------------------

    # 3. Функция "start" ----------------------------------------------------------------------
    # 3. Функция "start" ----------------------------------------------------------------------

    # 4. Про buttons ----------------------------------------------------------------------
    # 4. Про buttons ----------------------------------------------------------------------

    # 5. Добавление ссылок ----------------------------------------------------------------------
    # 5. Добавление ссылок ----------------------------------------------------------------------

    # 6. Отправляем файлы ----------------------------------------------------------------------
    # 6. Отправляем файлы ----------------------------------------------------------------------

    # 7. Подключаем к CRM ----------------------------------------------------------------------
    # 7. Подключаем к CRM ----------------------------------------------------------------------

    # 8. Работа с СБД ----------------------------------------------------------------------
    # 8. Работа с СБД ----------------------------------------------------------------------

    # Содержание ----------------------------------------------------------------------
    if get_message_bot == "Содержание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1. Вступление')
        btn2 = types.KeyboardButton('2. Получение token')
        btn3 = types.KeyboardButton('3. Функция "start"')
        btn4 = types.KeyboardButton('4. Про buttons')
        btn5 = types.KeyboardButton('5. Добавление ссылок')
        btn6 = types.KeyboardButton('6. Отправляем файлы')
        btn7 = types.KeyboardButton('7. Подключаем к CRM')
        btn8 = types.KeyboardButton('8. Работа с СБД')
        btn9 = types.KeyboardButton('Содержание')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_dice(message.chat.id, reply_markup=markup)

    if get_message_bot == "1. Вступление":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('👨‍💻Начнем')
        btn2 = types.KeyboardButton('О авторе курса')
        btn3 = types.KeyboardButton('Содержание')
        markup.add(btn1, btn2, btn3)
        send_mess = "*"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    if get_message_bot == '2. Получение token':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Модуль Start")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Чтобы связать нашу программу и бота по сети, нужен token бота.\n" \
                        "Это специальный ключ, с помощью которого его можно подключать к сторонним сервисам. " \
                        "Token нужно сохранить и никому не показывать — он так же важен, как и пароль от почты."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Создание", callback_data='firsttoken'),
                    types.InlineKeyboardButton("Редактирование", callback_data='secondtoken'),
                    types.InlineKeyboardButton("Подключение", callback_data='thirdtoken'))
        second_message = "Для получения нашего ключа, необходимо написать *@BotFather*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot =='3. Функция "start"':
        pass

    if get_message_bot =='4. Про buttons':
        pass

    if get_message_bot =='5. Добавление ссылок':
        pass

    if get_message_bot =='6. Отправляем файлы':
        pass

    if get_message_bot =='7. Подключаем к CRM':
        pass

    if get_message_bot =='8. Работа с СБД':
        pass
    # Содержание ----------------------------------------------------------------------




bot.polling(none_stop=True)