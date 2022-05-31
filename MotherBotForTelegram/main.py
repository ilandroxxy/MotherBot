import sqlite3
import telebot
from telebot import types
from telebot import callback_data
from time import *
import random
import emoji
# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪

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



    # Кнопка для 3. Команды и функции ----------------------------------------------------------------------
    elif call.data == 'theorystart':
        markup.add(types.InlineKeyboardButton("Пример 1", callback_data='firstexamplestart'),
                   types.InlineKeyboardButton("Пример 2", callback_data='secondexamplestart'))
        theorystart_message = "Команды представляют собой более гибкий способ общения с ботом. \n" \
                              "*Рекомендуется следующий синтаксис:*\n" \
                              "_/команда [необязательный] [аргумент]_\n\n" \
                              "☝️ Команда должна начинаться с символа косой черты «/» и не может быть длиннее 32 символов. " \
                              "Команды могут состоять из букв латинского алфавита, цифр и подчёркивания. \n\n*Несколько примеров:*\n" \
                              "_get_messages_stats_\n" \
                              "_set_timer 10min Alarm!_\n" \
                              "_get_timezone London, UK_\n\n"
        msg = bot.send_message(call.message.chat.id, theorystart_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'firstexamplestart':
        firstexamplestart_message = "Например эта простейшая команда выводит на экран рандомное число:"
        msg = bot.send_message(call.message.chat.id, firstexamplestart_message, parse_mode='Markdown')
        pic_5 = open("example1.jpg", "rb")
        bot.send_photo(call.message.chat.id,pic_5)
        firstexample2start_message = "*1.* Мы задаем название команды.\n" \
                                     "*2.* Начинаем писать функцию для ее обработки.\n" \
                                     "*3.* Генерим рандомное число от 1 до 1000\n" \
                                     "*4.* Поручаем боту отправить сообщение с нашим числом (переведенным в строковый тип данных и дублируем вызов команды"
        msg = bot.send_message(call.message.chat.id, firstexample2start_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, "click me 👉 /example1", parse_mode='Markdown')

    elif call.data == 'secondexamplestart':
        secondexamplestart_message = "Эта команда посложнее, мы считываем число введенное пользователем *(именно число)*" \
                                     "и возвращаем факториал от числа"
        msg = bot.send_message(call.message.chat.id, secondexamplestart_message, parse_mode='Markdown')
        pic_6 = open("example2.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_6)
        secondexample2start_message = "*1-2.* Строчки аналогичны предыдущему примеру\n" \
                                     "*3.* Специальное обращение бота, когда он отвечает на сообщение пользователя\n" \
                                     "*6.* Мы создаем фунцию обрабатывающую текст введенный пользователем \n" \
                                     "*7.* Кладем полученное сообщение в переменную x с типом данных str\n" \
                                     "*8.* Проверяем через методы строк пришло ли на вход число\n" \
                                      "*9.* Если было введено число и оно удовлетворяет условию, то переводим его в int-вое значение\n" \
                                      "*10-13.* И вычисляем факториал числа простейшим образом\n" \
                                      "*14-15.* Иначе просим пользователя перезапустить команду"
        msg = bot.send_message(call.message.chat.id, secondexample2start_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, "touch me 👉 /example2", parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'exitexample1':
        markup.add(types.InlineKeyboardButton("Пример 2", callback_data='secondexamplestart'))
        msg = bot.send_message(call.message.chat.id, "Отлично, двигаемся дальше 👇",reply_markup=markup)

    elif call.data == 'exitexample2':
        msg = bot.send_message(call.message.chat.id, "✅ Пора двигаться дальше 😉",reply_markup=markup)
    # Кнопка для 3. Команды и функции ----------------------------------------------------------------------

    # Кнопки 4. Бот отправляет ----------------------------------------------------------------------
    elif call.data == 'theorybotsend':
        markup.add(types.InlineKeyboardButton("Пример", callback_data='firstexamplebotsend'))
        theorybotsend_message = "Для взаимодействия бота с пользовательским чатом, а бот реагирует именно на *chat.id* - нам понадобится функция\n\n" \
                                "*bot.send_действие()*\n\n" \
                                "С помощью этой функции мы можем отправлять от лица бота разные файлы, картинки, стикеры, контакты и т.д."
        msg = bot.send_message(call.message.chat.id, theorybotsend_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'firstexamplebotsend':
        examplebotsend_message = "Вот примеры простейших объектов которые бот может отправлять пользователю:"
        msg = bot.send_message(call.message.chat.id,  examplebotsend_message, parse_mode='Markdown')
        pic_5 = open("example3.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_5)
        example2botsend_message = "*3.* Отправляем текст пользователю \n" \
                                     "*5-6.* Открываем картинку из проекта и отправляем ее пользователю\n" \
                                     "*8.* Бот отправляет заготовленный заранее контакт\n" \
                                     "*10-11.* Аналогично картинке скачиваем в проект стикер и отправлем его"
        msg = bot.send_message(call.message.chat.id, example2botsend_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, " 👉 /example3", parse_mode='Markdown')
    # Кнопки 4. Бот отправляет ----------------------------------------------------------------------


    # Кнопки 5. KeyboardButton ----------------------------------------------------------------------
    elif call.data == 'theoryKeyboardButton':
        markup.add(types.InlineKeyboardButton("Пример 1", callback_data='firstexampleKeyboardButton'), types.InlineKeyboardButton("Пример 2", callback_data='secondexampleKeyboardButton'))
        theoryKeyboardButton_message = "При передаче сервером ответа есть возможность передать команду на отображение специальной клавиатуры с предустановленными вариантами " \
                                       "ответа используя:\n\n*ReplyKeyboardMarkup()*\n\nКлиент Telegram, получив сообщение, отобразит пользователю вашу клавиатуру. " \
                                       "Нажатие на клавишу сразу же отправит на сервер соответствующую команду. " \
                                       "\n\nТаким образом можно значительно упростить взаимодействие робота с пользователем. " \
                                       "На данный момент для отображения на клавише могут использоваться эмодзи и текст. \n\nВот несколько примеров таких клавиатур:"
        msg = bot.send_message(call.message.chat.id, theoryKeyboardButton_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'firstexampleKeyboardButton':
        exampleKetboardButton_message = "В этом примере мы просто создаем две клавиши и возвращаем те или иные сообщения в зависимости от нажатия."
        msg = bot.send_message(call.message.chat.id, exampleKetboardButton_message, parse_mode='Markdown')
        pic_5 = open("example4.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_5)
        example2KetboardButton_message = "*3.* Мы объявляем форму для клавиатуры и задаем размер (кол-во клавишь) на экране\n" \
                                  "*4-5.* Создаем сами клавиши через переменные\n" \
                                  "*7-8.* Добавляем в единую форму и просим бота отобразить их через *replay_markup=имя формы*, " \
                                        "для этого действия обязательно использовать какой-то из *bot.send_действие*\n" \
                                  "*10-11.* Создаем функцию обрабатывающую введенные клавиши с типом text\n" \
                                         "12. Используем метод *строка.strip() для удаления всех пробелов (проверка на дурака)*\n" \
                                         "14-18. В зависимости от нажатой клавиши возвращаем пользователею какое-то выбранное действие"

        msg = bot.send_message(call.message.chat.id, example2KetboardButton_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, " 👉 /example4", parse_mode='Markdown')

    elif call.data == 'exitfirstexampleKeyboardButton':
        markup.add(types.InlineKeyboardButton("Пример 1", callback_data='firstexampleKeyboardButton'),
                   types.InlineKeyboardButton("Пример 2", callback_data='secondexampleKeyboardButton'))
        msg = bot.send_message(call.message.chat.id, "Магия свершилась 🪄", parse_mode='Markdown',
                               reply_markup=markup)

    elif call.data == 'secondexampleKeyboardButton':
        exampleKetboardButton_message = "А это пример создания мини викторины."
        msg = bot.send_message(call.message.chat.id, exampleKetboardButton_message, parse_mode='Markdown')
        pic_5 = open("example5.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_5)
        example2KetboardButton_message = "В целом эта часть кода не требует пояснений кроме совей последней строчки, " \
                                         'в 10 строке есть параметр *parse_mode=* он позволяет выбрать форматирование' \
                                         'текста, поддерживаются два варианта:\n1. *"Markdown"*\n2. *"HTML"*\n'


        msg = bot.send_message(call.message.chat.id, example2KetboardButton_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, " 👉 /example5", parse_mode='Markdown')

    elif call.data == 'exitsecondexampleKeyboardButton':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup.add(btn1, btn2)
        msg = bot.send_message(call.message.chat.id, "✅ Движение жизнь, идем дальше 👇",reply_markup=markup)
    # Кнопки 5. KeyboardButton ----------------------------------------------------------------------

    # Кнопки 6. InlineButton ----------------------------------------------------------------------
    elif call.data == 'theoryInlineButton':
        markup.add(types.InlineKeyboardButton("Пример", callback_data='firstexampleInlineButton'))
        theoryInlineButton_message = "Мы также имеем возможность передать команду на отображение специальных кнопок с предустановленными " \
                                     "вариантами ответа:\n\n*InlineKeyboardMarkup()*\n\nКлиент Telegram, получив сообщение, отобразит пользователю нашу клавишу" \
                                     "нажатие на которую сразу же отправит на сервер соответствующую команду с предустановленными " \
                                     "вариантами ответа - очень похоже на ReplayKeyboardMarkup(), но более гибкие варианты использования. "
        msg = bot.send_message(call.message.chat.id, theoryInlineButton_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'firstexampleInlineButton':
        exampleInlineButton_message = "Тут я написал простейший скрип играющий с пользователем в камень ножница бумага, именно такие игры встречаем в умных чайниках и термокружках 😅"
        msg = bot.send_message(call.message.chat.id, exampleInlineButton_message, parse_mode='Markdown')
        pic_5 = open("example6.jpg", "rb")
        bot.send_photo(call.message.chat.id, pic_5)
        example2InlineButton_message = "*3.* В функции мы подключаем форму и для кнопок - их может быть несколько по аналогии с прошлым объектом изучения\n" \
                                       "*4.* Обратите внимание, что тут используется *callback_data=' '* - эта штука помогает нас связать со второй " \
                                       "частью программы исполняющей наш запрос на игру\n" \
                                       "*5.* Мы так же как и с *KeyboardButton()* должны обновлять запросы для отображения клавиш используя *replay_markup=*\n" \
                                       "*9:* Остальная часть реализует саму игру и с минимальным знанием Python должна быть понятная всем читающим "

        msg = bot.send_message(call.message.chat.id, example2InlineButton_message, parse_mode='Markdown')
        msg = bot.send_message(call.message.chat.id, " 👉 /example6", parse_mode='Markdown')

    elif call.data == 'exampleGameInlineButton':
        Step = ['Камень', 'Ножницы', 'Бумага', '1️⃣ Раз!', '2️⃣ Два!', '3️⃣ Три!']
        Massive = ['КАМЕНЬ', 'НОЖНИЦЫ', 'БУМАГА!']
        for i in range(0, len(Step)):
            msg = bot.send_message(call.message.chat.id, Step[i])
            sleep(0.6)

        x = random.randint(0, 2)
        msg = bot.send_message(call.message.chat.id, '▶️' + Massive[x])
        sleep(2)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🎮 Play", callback_data='exampleGameInlineButton'))
        msg = bot.send_message(call.message.chat.id, 'Давай сыграем снова!', parse_mode="Markdown", reply_markup=markup)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Back", callback_data='exitexampleInlineButton'))
        msg = bot.send_message(call.message.chat.id, 'Или продолжим учиться', parse_mode="Markdown", reply_markup=markup2)

    elif call.data == 'exitexampleInlineButton':
        msg = bot.send_message(call.message.chat.id, "✅ Конец близок, не сдавайся👇", reply_markup=markup)
    # Кнопки 6. InlineButton ----------------------------------------------------------------------

    # 7. Кнопки Подключаем к CRM ----------------------------------------------------------------------
    # AMO CRM
    elif call.data == 'amo_crm':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='amostep1'))
        send_message = "ТЕКСТ 1"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'amostep1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='amostep2'))
        send_message = "ТЕКСТ 2"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'amostep2':
        markup = types.InlineKeyboardMarkup(row_width=3)
        click1 = types.InlineKeyboardButton("amoCRM", callback_data='amo_crm')
        click2 = types.InlineKeyboardButton("Jivo", callback_data='jivo_crm')
        click3 = types.InlineKeyboardButton("Битрик24", callback_data='bitrix_crm')
        click4 = types.InlineKeyboardButton("Закончим на CRM системах", callback_data='endcrm')
        markup.add(click1, click2, click3, click4)
        send_message = "ТЕКСТ 3\n" \
                       "👋 Рад видеть, предприниматель!"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)
    # AMO CRM

    # JIVO
    elif call.data == 'jivo_crm':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='jivostep1'))
        send_message = "ТЕКСТ 1"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'jivostep1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='jivostep2'))
        send_message = "ТЕКСТ 2"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'jivostep2':
        markup = types.InlineKeyboardMarkup(row_width=3)
        click1 = types.InlineKeyboardButton("amoCRM", callback_data='amo_crm')
        click2 = types.InlineKeyboardButton("Jivo", callback_data='jivo_crm')
        click3 = types.InlineKeyboardButton("Битрик24", callback_data='bitrix_crm')
        click4 = types.InlineKeyboardButton("Закончим на CRM системах", callback_data='endcrm')
        markup.add(click1, click2, click3, click4)
        send_message = "ТЕКСТ 3\n" \
                       "👋 Рад видеть, предприниматель!"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)
    # JIVO

    # БИТРИКС
    elif call.data == 'bitrix_crm':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='bitrixstep1'))
        send_message = "ТЕКСТ 1"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'bitrixstep1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Далее", callback_data='bitrixstep2'))
        send_message = "ТЕКСТ 2"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'bitrixstep2':
        markup = types.InlineKeyboardMarkup(row_width=3)
        click1 = types.InlineKeyboardButton("amoCRM", callback_data='amo_crm')
        click2 = types.InlineKeyboardButton("Jivo", callback_data='jivo_crm')
        click3 = types.InlineKeyboardButton("Битрик24", callback_data='bitrix_crm')
        click4 = types.InlineKeyboardButton("Закончим на CRM системах", callback_data='endcrm')
        markup.add(click1, click2, click3, click4)
        send_message = "ТЕКСТ 3\n" \
                       "👋 Рад видеть, предприниматель!"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)
    # БИТРИКС

    elif call.data == 'endcrm':
        msg = bot.send_message(call.message.chat.id, "✅ Остался последний урок и скоро этот кошмар кончится 😅", reply_markup=markup)
    # 7. Кнопки Подключаем к CRM ----------------------------------------------------------------------







    # Кнопки для получения Донатов ----------------------------------------------------------------------
    elif call.data == "finishtoken":
        markup.add(types.InlineKeyboardButton("💸 Tinkoff", url='https://www.tinkoff.ru/cf/9f3vcMecD9w'))
        pic_4 = open("donate.jpg", 'rb')
        bot.send_photo(call.message.chat.id, pic_4, reply_markup=markup)
        msg = bot.send_message(call.message.chat.id, " Спасибо за оценку моей работы ❤️ ")

        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS donaters(
                        id INTEGER,
                        data TEXT,
                        donate BOOLEAN
                    )""")
        sql.commit()

        people_id = call.message.chat.id
        cursor.execute(f"SELECT id FROM donaters WHERE id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = call.message.chat.id
            today = ctime()
            cursor.execute(f"INSERT INTO donaters VALUES(?, ?, ?);", (user_id, today, True))
            sql.commit()
    # Кнопки для получения Донатов ----------------------------------------------------------------------

@bot.message_handler(commands=['example6'])
def example6(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎮 Play", callback_data='exampleGameInlineButton'))
    bot.send_message(message.chat.id, 'Сыграй с компьютером в игру:\n"Камень, ножницы, бумага"' , parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(commands=['example5'])
def example5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("A")
    btn2 = types.KeyboardButton("B")
    btn3 = types.KeyboardButton("C")
    btn4 = types.KeyboardButton("D")
    markup.add(btn1, btn2, btn3, btn4)
    question_messsage = 'В каком году было крещение Руси?\nA)  998\nB)  992\nC)  988\nD)  990'
    bot.send_message(message.chat.id, question_messsage , parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(commands=['example4'])
def example4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Круто")
    btn2 = types.KeyboardButton("Не очень, я устал")
    btn3 = types.KeyboardButton("Как вернуться назад?")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Скажи мне, как у тебя дела?', parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(commands=['example3'])
def example3(message):
    bot.send_message(message.chat.id, 'Вот тут мы отправляем текст')

    pic = open("privetexample.jpg", "rb")
    bot.send_photo(message.chat.id, pic)

    bot.send_contact(message.chat.id, phone_number=79998887766, first_name="Бот Анатолий", last_name="Прокат NFT великов за биткоин")

    sti = open("AnimatedStickerFrog.tgs", "rb")
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "✅ Двигаемся вперед 💪")

@bot.message_handler(commands=['example1'])
def example1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("🙏 Вернуться назад", callback_data='exitexample1'))
    x = str(random.randint(1, 1000))
    bot.send_message(message.chat.id, x + "  try again /example1", reply_markup=markup)

@bot.message_handler(commands=['example2'])
def example2(message):
    markup = types.InlineKeyboardMarkup()
    bot.reply_to(message, 'Посчитаем факториал числа:\n(Не превышающего 1000) ')

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        x = message.text
        if x.isdigit() == True and 0 < int(x) <= 1000:
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
    sql = sqlite3.connect('analytics.db')
    cursor = sql.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS visitors(
        id INTEGER,
        data TEXT,
        donate BOOLEAN
    )""")
    sql.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM visitors WHERE id = {people_id}")
    data = cursor.fetchone()

    if data is None:
        user_id = message.chat.id
        today = ctime()
        cursor.execute(f"INSERT INTO visitors VALUES(?, ?, ?);", (user_id, today, False))
        sql.commit()



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

    # 3. Команды и функции ----------------------------------------------------------------------
    if get_message_bot == "Команды и функции":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Бот отправляет")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Token получен, библиотеки установлены - пора запускать бота!\n\n" \
                        "Любой бот запускается с первой команды, которую нам и необходимо реализовать в этом разделе. " \
                        "\n\nДумаю, вы уже замечали, что большинство ботов начинаются с команды /start , " \
                        "но это просто название, мы можем написать команду с любым функционалом."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theorystart'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)
    # 3. Команды и функции ----------------------------------------------------------------------

    # 4. Бот отправляет ----------------------------------------------------------------------
    if get_message_bot == "Бот отправляет":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("KeyboardButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Пришло время научить бота отправлять данные в ответ"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theorybotsend'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)
    # 4. Бот отправляет ----------------------------------------------------------------------

    # 5. KeyboardButton ----------------------------------------------------------------------
    if get_message_bot == "KeyboardButton":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Одна из самых необычных возможностей Bot API — кастомизированные клавиатуры."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theoryKeyboardButton'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    # for example 1
    if get_message_bot == "Круто":
        bot.send_message(message.chat.id, "Молодец, так держать 💪")

    elif get_message_bot == "Не очень, я устал":
        bot.send_message(message.chat.id, "Сделай паузу, продолжишь завтра!")

    elif get_message_bot == "Как вернуться назад?":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup2.add(btn1, btn2)
        first_message = "Телепорт к примерам"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup2)

        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton("Телепорт 🔮", callback_data='exitfirstexampleKeyboardButton'))
        bot.send_message(message.chat.id, "✨", reply_markup=markup3)
    # for example 1

    # for example 2
    elif get_message_bot == "A":
        bot.send_message(message.chat.id, "Ответ неверный")
    elif get_message_bot == "B":
        bot.send_message(message.chat.id, "Ты был близок")
    elif get_message_bot == "D":
        bot.send_message(message.chat.id, "Попытка не пытка...")
    elif get_message_bot == "C":
        bot.send_message(message.chat.id, "Верно, молодец!")
        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton("Телепорт 🔮", callback_data='exitsecondexampleKeyboardButton'))
        bot.send_message(message.chat.id, "✨", reply_markup=markup3)
    # for example 2
    # 5. KeyboardButton ----------------------------------------------------------------------


    # 6. InlineButton ----------------------------------------------------------------------
    if get_message_bot == "InlineButton":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Подключаем к CRM")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Помимо клавиатуры мы можем подключать и активно использовать inline кнопки"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theoryInlineButton'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)


    # 6. InlineButton ----------------------------------------------------------------------

    # 7. Подключаем к CRM ----------------------------------------------------------------------
    if get_message_bot == "Подключаем к CRM":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Работа с СБД")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "CRM - это система управления взаимоотношениями с клиентами предназначенное для автоматизации стратегий взаимодействия с клиентами, в частности " \
                        "для повышения уровня продаж, оптимизации маркетинга и улучшения обслуживания клиентов путём сохранения информации о клиентах и истории взаимоотношений с ними, установления" \
                        " и улучшения бизнес-процессов и последующего анализа результатов."

        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=3)
        click1 = types.InlineKeyboardButton("amoCRM", callback_data='amo_crm')
        click2 = types.InlineKeyboardButton("Jivo", callback_data='jivo_crm')
        click3 = types.InlineKeyboardButton("Битрик24", callback_data='bitrix_crm')
        markup2.add(click1, click2, click3)
        CrmTheory_sendmessage = "В основном CRM систему используют для работы колл- центров, так вот представим ситуацию, " \
                                "что вам нужен единый канал связи через телегарм на колл-центр в 30 человек. Обычный акаунт физического " \
                                "лица вам не подойдет - подключаютя через ботов. Чащей всего подключение очень простое и не поддерживает всех " \
                                "наших модных кнопочек - такие компании делают API, чтобы зарабатывать деньги на Ботах интегрированных в свою систему." \
                                "Но не будем унывать и таки попробуем подключить некоторые (а их бесчисленное множество) сервисы к нашему боту ✌️"
        bot.send_message(message.chat.id, CrmTheory_sendmessage, parse_mode='Markdown', reply_markup=markup2)
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
        first_message = "Token получен, библиотеки установлены - пора запускать бота!\n\n" \
                        "Любой бот запускается с первой команды, которую нам и необходимо реализовать в этом разделе. " \
                        "\n\nДумаю, вы уже замечали, что большинство ботов начинаются с команды /start , " \
                        "но это просто название, мы можем написать команду с любым функционалом."
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
        first_message = "Пришло время научить бота отправлять данные в ответ"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theorybotsend'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot =='5. KeyboardButton':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("InlineButton")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Одна из самых необычных возможностей Bot API — кастомизированные клавиатуры."
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theoryKeyboardButton'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot == "6. InlineButton":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Подключаем к CRM")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "Помимо клавиатуры мы можем подключать и активно использовать inline кнопки"
        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("Теория", callback_data='theoryInlineButton'))
        bot.send_message(message.chat.id, "👇", parse_mode='Markdown', reply_markup=markup2)
        sleep(0.5)

    if get_message_bot =='7. Подключаем к CRM':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Работа с СБД")
        btn2 = types.KeyboardButton("Содержание")
        markup1.add(btn1, btn2)
        first_message = "CRM - это система управления взаимоотношениями с клиентами предназначенное для автоматизации стратегий взаимодействия с клиентами, в частности " \
                        "для повышения уровня продаж, оптимизации маркетинга и улучшения обслуживания клиентов путём сохранения информации о клиентах и истории взаимоотношений с ними, установления" \
                        " и улучшения бизнес-процессов и последующего анализа результатов."


        bot.send_message(message.chat.id, first_message, parse_mode='Markdown', reply_markup=markup1)
        sleep(0.5)

        markup2 = types.InlineKeyboardMarkup(row_width=3)
        click1 = types.InlineKeyboardButton("amoCRM", callback_data='amo_crm')
        click2 = types.InlineKeyboardButton("Jivo", callback_data='jivo_crm')
        click3 = types.InlineKeyboardButton("Битрик24", callback_data='bitrix_crm')
        markup2.add(click1, click2, click3)
        CrmTheory_sendmessage = "В основном CRM систему используют для работы колл- центров, так вот представим ситуацию, " \
                                "что вам нужен единый канал связи через телегарм на колл-центр в 30 человек. Обычный акаунт физического " \
                                "лица вам не подойдет - подключаютя через ботов. Чащей всего подключение очень простое и не поддерживает всех " \
                                "наших модных кнопочек - такие компании делают API, чтобы зарабатывать деньги на Ботах интегрированных в свою систему." \
                                "Но не будем унывать и таки попробуем подключить некоторые (а их бесчисленное множество) сервисы к нашему боту ✌️"
        bot.send_message(message.chat.id, CrmTheory_sendmessage, parse_mode='Markdown', reply_markup=markup2)
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