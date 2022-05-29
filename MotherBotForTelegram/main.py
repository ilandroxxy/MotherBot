
import telebot
from telebot import types
from telebot import callback_data
from time import sleep
import random
import emoji
# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️

bot = telebot.TeleBot('5430380851:AAE70eeR3jFdxuM_BlWjWLNgsDEGhWRqC7o')


# ссылка для "Как Python связан с Telegram?"
@bot.message_handler(commands=['documentation'])
def open_documentation(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Документация Telegram API", url = "https://tlgrm.ru/docs#boty"))
    bot.send_message(message.chat.id, "✅ Это не призыв к действию, читать документацию сложно, но можно. \n"
                                      "Пробуй и подучи английский, так очевидные вещи станут еще очевиднее 😉", parse_mode='html', reply_markup=markup)

# Функция для обработки последовательных inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # Кнопки для 2. Получение token ----------------------------------------------------------------------
    if call.data == 'createtoken':
        pic_2 = open("BotFather.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_2)
        createtoken_message = "Бот приветствует нас вот таким сообщением, как не сложно догадаться - нам необходима команда /newbot\n" \
                             "В этом же боте происходит редактирование всех наших ботов.\n\n" \
                             "В ответ на команду бот пишет:\n" \
                             "_Alright, a new bot. How are we going to call it? Please choose a name for your bot_.\n\n" \
                             "Выбираем имя, оно будет основным, но не будет являться id! Потому что следующим сообщением @BotFather попросит:\n" \
                             "_Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot_.\n\n" \
                             "Если на этом этапе у вас все получится, то вам прийдет готовый token (к слову, его тоже можно будет сменить через @BotFather):\n" \
                             "_*Use this token to access the HTTP API:*_ 5543492408:AAFKGXowK8CV5Q4IFOGzDTCTR4O_AaLtU2I"

        msg = bot.send_message(call.message.chat.id, createtoken_message, parse_mode="Markdown", reply_markup=markup)
        pic_3 = open("CreateBot.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_3)

        markup.add(types.InlineKeyboardButton("Создание", callback_data='addtoken'),
                   types.InlineKeyboardButton("Подключение", callback_data='addtoken'),
                    types.InlineKeyboardButton("Редактирование", callback_data='fixtoken'))
        bot.send_message(call.message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'addtoken':
        addtoken_message = "Далее в нашем Python проекте необходимо написать две строчки:\n" \
                              "*bot = telebot.TeleBot('наш token')* - подключение бота к проекту.\n" \
                              "И строку: \n*bot.polling(none_stop=True)*\n\n" \
                              "Чат-боты должны получать уведомления от соцсети моментально. " \
                              "Они не могут проверять обновления каждую секунду, это неэффективно.\n\n" \
                              "Такой подход, когда раз в n секунд опрашивается сторонний сервис, называется polling.\n\n" \
                              "Все, что будет находиться между этими двумя строчками и станет нашим ботом ✊"

        msg = bot.send_message(call.message.chat.id, addtoken_message, parse_mode="Markdown", reply_markup = markup)

        markup.add(types.InlineKeyboardButton("Создание", callback_data='addtoken'),
                   types.InlineKeyboardButton("Подключение", callback_data='addtoken'),
                   types.InlineKeyboardButton("Редактирование", callback_data='fixtoken'))
        bot.send_message(call.message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'fixtoken':
        fixtoken_message = "Как я уже говорил - все настройки и изменения происходят благодаря @BotFather\n" \
                             "прописываем команду /mybots, выбираем нашего бота по id\n" \
                             "и переходим во вкладку Edit Bot, тут мы можем менять имя, описание, приветственное сообщение, picture и редактировать команды" \
                             "(Опять же для самых внимательных - у нас уже есть команда 'start', тут мы можем сделать отдельное меню для отображения таких команд."
        msg = bot.send_message(call.message.chat.id, fixtoken_message, reply_markup = markup)
        msg = bot.send_message(call.message.chat.id, "✅ Уверен, что теперь мы готовы идти дальше 😉", reply_markup=markup)
    # Кнопки для 2. Получение token ----------------------------------------------------------------------



    # Кнопка для 3. Команда start ----------------------------------------------------------------------
    elif call.data == 'theorystart':
        markup.add(types.InlineKeyboardButton("Пример 1", callback_data='firstexamplestart'),
                   types.InlineKeyboardButton("Пример 2", callback_data='secondexamplestart'))
        theorystart_message = "Функции могут исполнять какие-то действия и возвращать нам результат."
        msg = bot.send_message(call.message.chat.id, theorystart_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'firstexamplestart':
        firstexamplestart_message = "Например эта простейшая функция выводит на экран рандомное число:"
        msg = bot.send_message(call.message.chat.id, firstexamplestart_message, parse_mode='Markdown')
        pic_5 = open("example1.jpg", "rb")
        bot.send_photo(call.message.chat.id,pic_5)
        msg = bot.send_message(call.message.chat.id, "click me 👉 /example1", parse_mode='Markdown')

    elif call.data == 'secondexamplestart':
        secondexamplestart_message = "Эта функция посложнее, мы считываем число введенное пользователем *(именно число)*" \
                                     "и возвращаем факториал от числа"
        msg = bot.send_message(call.message.chat.id, secondexamplestart_message, parse_mode='Markdown')
        pic_6 = open("example2.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_6)
        msg = bot.send_message(call.message.chat.id, "touch me 👉 /example2", parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'exitexample1':
        markup.add(types.InlineKeyboardButton("Пример 2", callback_data='secondexamplestart'))
        msg = bot.send_message(call.message.chat.id, "Отлично, двигаемся дальше 👇",reply_markup=markup)


    elif call.data == 'exitexample2':
        msg = bot.send_message(call.message.chat.id, "✅ Пора двигаться дальше 😉",reply_markup=markup)
    # Кнопка для 3. Команда start ----------------------------------------------------------------------




    # Кнопки для получения Донатов ----------------------------------------------------------------------
    elif call.data == "finishtoken":
        markup.add(types.InlineKeyboardButton("💸 Tinkoff", url='https://www.tinkoff.ru/cf/9f3vcMecD9w'))
        pic_4 = open("donate.jpg", 'rb')
        bot.send_photo(call.message.chat.id, pic_4, reply_markup=markup)
        msg = bot.send_message(call.message.chat.id, " Спасибо за оценку моей работы ❤️ ")
    # Кнопки для получения Донатов ----------------------------------------------------------------------


# Command for example1, in chapter 'Команда start'
@bot.message_handler(commands=['example1'])
def example1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("🙏 Вернуться назад", callback_data='exitexample1'))
    x = str(random.randint(1, 1000))
    bot.send_message(message.chat.id, x + "  try again /example1", reply_markup=markup)

# Command for example2, in chapter 'Команда start'
@bot.message_handler(commands=['example2'])
def example2(message):
    markup = types.InlineKeyboardMarkup()
    bot.reply_to(message, 'Посчитаем факториал числа: ')

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        x = message.text
        if x.isdigit() == True:
            temp = int(x)
            res = 1
            while temp > 0:
                res *= temp
                temp = temp - 1
            markup.add(types.InlineKeyboardButton("Закончить", callback_data='exitexample2'))
            bot.send_message(message.chat.id, f'Факториал числа: {x} = {res}', reply_markup=markup)
        else:
            bot.reply_to(message, 'Я в такие игры не играю.. 👉 /example2 ')



    bot.register_next_step_handler(message, message_input)




#MENU
@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('1. Вступление')
    btn2 = types.KeyboardButton('2. Получение token')
    btn3 = types.KeyboardButton('3. Команда start')
    btn4 = types.KeyboardButton('4. Бот отправляет')
    btn5 = types.KeyboardButton('5. KeyboardButton')
    btn6 = types.KeyboardButton('6. InlineButton')
    btn7 = types.KeyboardButton('7. Подключаем к CRM')
    btn8 = types.KeyboardButton('8. Работа с СБД')
    btn9 = types.KeyboardButton('Содержание')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_dice(message.chat.id, reply_markup=markup)

#START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('👨‍💻Начнем')
    btn2 = types.KeyboardButton('О авторе курса')
    btn3 = types.KeyboardButton('Содержание')
    markup.add(btn1, btn2, btn3)
    send_mess = f"👋 Доброго времени суток, *{message.from_user.first_name}*!\n\nРад Вас приветствовать на моем авторском курсе *'PyTelegramBotAPI'*.\n\n" \
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
        send_mess = 'Рaсскажу чуть подробнее о курсе:\nИдея была в том, чтобы создать интересный курс на удобной для "употребления" контента плоащадке.\n'\
                    "Cогласитесь забавно выходит, учимся делать ботов в боте 🌚\n\n" \
                    "В курсе нам понадобятся базовые знания Python, среда разработки Pycharm, немного терпения и щепотка удачи ✨\n\n" \
                    "В конце курса я прикреплю ссылки на шаблоны готовых решений - балванки для ваших будущих 🤖"
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
                    "ресурсами с другими разработчиками. \n\n👉 Такие решения называются *API* и нужны они в первую очередь для интеграции" \
                    "сторонних сервисов в экосистему нашей платформы (Для тех кто уже запутался - в нашем случае это Telegram)." \
                    "\n\n*Telegram* имеет свое *API* для языка *Python* и позволяет нам как сторонним разработчикам делать разные действия на площадке, в том числе и ботов 🤖\n\n"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup)
        sleep(0.5)
        second_message = "❗Надеюсь вы уже скачали *Python и Pycharm* (IDE для разработки программ, не обязательное, но желательное - вам так будет удобнее) потому что мы начинаем " \
                    "*подключать Telegram API* к нашему пустому проекту, для этого нам нужно его скачать! Воспользуемся pip установщиком библиотек и в Terminal проекта " \
                    "введем команду: \n\n*pip install PyTelegramBotAPI* \n\nЖдем несколько секунд и вуаля, наше *API* уже есть в проекте, осталось только его подключить.." \
                    "Но это уже стандартная практика, через import подключаем библиотеку telebot:\n\n*import telebot*\n*from telebot import types*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown')
        sti_2 = open("AnimatedSticker.tgs", "rb")
        bot.send_sticker(message.chat.id, sti_2)
        bot.send_message(message.chat.id, "✅ Надеюсь вы все еще с нами 😅")

    # Получение ссылки на TelegramAPI документакцию
    if message.text == "Хочу получить ссылку":
        open_documentation(message)
    # 1. Вступление ----------------------------------------------------------------------


    # 2. Получение token ----------------------------------------------------------------------
    if get_message_bot == "Что такое token?":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Команды и функции")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Чтобы связать нашу программу и бота по сети, нужен token бота.\n" \
                        "Это специальный ключ, с помощью которого его можно подключать к сторонним сервисам. " \
                        "Token нужно сохранить и никому не показывать — он так же важен, как и пароль от почты."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Создание", callback_data ='createtoken'),
                    types.InlineKeyboardButton("Подключение", callback_data ='addtoken'),
                    types.InlineKeyboardButton("Редактирование", callback_data ='fixtoken'))
        second_message = "Для получения нашего ключа, необходимо написать *@BotFather*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)
    # 2. Получение token ----------------------------------------------------------------------

    # 3. Команда "start" ----------------------------------------------------------------------
    if get_message_bot == "Команды и функции":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Бот отправляет")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Token получен, библиотеки установлены, энтузиазмом заряжены - пора запускать бота!\n" \
                        "Любой бот запускается с первой команды, которую нам и необходимо реализовать в этом разделе."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theorystart'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)
    # 3. Команда "start" ----------------------------------------------------------------------

    # 4. Про buttons ----------------------------------------------------------------------
    if get_message_bot == "Бот отправляет":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("KeyboardButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # 4. Про buttons ----------------------------------------------------------------------

    # 5. Добавление ссылок ----------------------------------------------------------------------
    if get_message_bot == "KeyboardButton":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # 5. Добавление ссылок ----------------------------------------------------------------------

    # 6. Отправляем файлы ----------------------------------------------------------------------
    if get_message_bot == "InlineButton":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Подключаем к CRM")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # 6. Отправляем файлы ----------------------------------------------------------------------

    # 7. Подключаем к CRM ----------------------------------------------------------------------
    if get_message_bot == "Подключаем к CRM":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Работа с СБД")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # 7. Подключаем к CRM ----------------------------------------------------------------------

    # 8. Работа с СБД ----------------------------------------------------------------------
    if get_message_bot == "Работа с СБД":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Оставить отзыв")
        btn2 = types.KeyboardButton("Поблагодарить")
        btn3 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2, btn3)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # 8. Работа с СБД ----------------------------------------------------------------------

    # Содержание ----------------------------------------------------------------------
    if get_message_bot == "Содержание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('1. Вступление')
        btn2 = types.KeyboardButton('2. Получение token')
        btn3 = types.KeyboardButton('3. Команды и функции')
        btn4 = types.KeyboardButton('4. Бот отправляет')
        btn5 = types.KeyboardButton('5. KeyboardButton')
        btn6 = types.KeyboardButton('6. InlineButton')
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
        send_mess = "Рад снова тебя видеть здесь 😅😉"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    if get_message_bot == '2. Получение token':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Команда start")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Чтобы связать нашу программу и бота по сети, нужен token бота.\n" \
                        "Это специальный ключ, с помощью которого его можно подключать к сторонним сервисам. " \
                        "Token нужно сохранить и никому не показывать — он так же важен, как и пароль от почты."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Создание", callback_data='createtoken'),
                    types.InlineKeyboardButton("Подключение", callback_data='addtoken'),
                    types.InlineKeyboardButton("Редактирование", callback_data='fixtoken'))
        second_message = "Для получения нашего ключа, необходимо написать *@BotFather*"
        bot.send_message(message.chat.id, second_message, parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot =='3. Команды и функции':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Бот отправляет")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Token получен, библиотеки установлены, энтузиазмом заряжены - пора запускать бота!\n" \
                        "Любой бот запускается с первой команды, которую нам и необходимо реализовать в этом разделе."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theorystart'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot =='4. Бот отправляет':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("KeyboardButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

    if get_message_bot =='5. KeyboardButton':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

    if get_message_bot =='6. InlineButton':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Подключаем к CRM")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

    if get_message_bot =='7. Подключаем к CRM':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Работа с СБД")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

    if get_message_bot =='8. Работа с СБД':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Оставить отзыв")
        btn2 = types.KeyboardButton("Поблагодарить")
        btn3 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2, btn3)
        first_message = "туть нужен текст"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)
    # Содержание ----------------------------------------------------------------------

    # The end ----------------------------------------------------------------------
    if get_message_bot == "Оставить отзыв":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🗳 Ссылка на форму", url="https://forms.gle/139k1Z3S3WBGPpNXA"))
        bot.send_message(message.chat.id, "*Спасибо, за участие в жизни проекта, я это очень ценю* ☺️✌️️", parse_mode="Markdown", reply_markup=markup)

    if get_message_bot == "Поблагодарить":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ donate",  callback_data="finishtoken"))
        bot.send_message(message.chat.id, "Я с радостью приму любую помощь 🙏", parse_mode="Markdown", reply_markup=markup)
    # The end ----------------------------------------------------------------------

bot.polling(none_stop=True)