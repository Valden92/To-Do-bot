import telebot

token = ''

bot = telebot.TeleBot(token)

HELP = """
Что может To-Do бот:

/help - Напечатать справку о программе.

/add - Добавить новую задачу в список. Все параметры ввода обязательны и вводятся через пробел.
       (Пример: /add 10.07.2021 Текст задачи)

/show - Напечатать добавленные задачи по дате или все имеющиеся (ввести all)
       (Пример: /show 10.07.2021)
       (Пример: /show 10.07.2021 09.07.2021)
       (Пример: /show all)

/clear - Удалить все данные введенные ранее. Восстановление невозможно! С основной командой ввести последовательно тест:\nЯ согласен на удаление всех моих данных
"""

tasks = {}


def input_validation(message, command, date):
    """Проверяет правильность ввода даты."""
    import datetime, time

    if command.strip().lower() == '/add':
        date_now = datetime.datetime.today().strftime('%d.%m.%Y')
        try:
            valid_date = time.strptime(date, '%d.%m.%Y')
            date_now = time.strptime(date_now, '%d.%m.%Y')
            if valid_date >= date_now:
                return True
            else:
                bot.send_message(message.chat.id, "Этот день затерялся где-то в прошлом.")
                return False
        except ValueError:
            return False
    elif command.strip().lower() == '/show':
        try:
            time.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False


def show_tasks(message, command, date):
    """Кусок кода для вывода информации в зависимости от даты."""
    if input_validation(message, command, date):
        if date in tasks.keys():
            bot.send_message(message.chat.id, "Дата: {}".format(date))
            for i in tasks[date]:
                bot.send_message(message.chat.id, "- {}".format(i))
        else:
            bot.send_message(message.chat.id, "На {} ничего не запланировано.".format(date))
    else:
        bot.send_message(message.chat.id, "Неверный формат ввода даты.\nВзгляните на пример тут /help")



@bot.message_handler(commands=["help", "start"])
def help(message):
    """Выводит меню помощи."""
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
    """Добавляет новые задачи в список задач на определенную дату."""
    try:
        command = message.text.split(maxsplit=2)
        date = command[1]
        task = command[2]

        if input_validation(message, command[0], date):
            if len(task) > 2:
                if date in tasks.keys():
                    tasks[date].append(task)
                    bot.send_message(message.chat.id, "Задача успешно добавлена на {}".format(date))
                else:
                    tasks[date] = []
                    tasks[date].append(task)
                    bot.send_message(message.chat.id, "Задача успешно добавлена на {}".format(date))
            else:
                bot.send_message(message.chat.id, "Слишком короткая задача.")
        else:
            bot.send_message(message.chat.id, "Неверный формат ввода даты.\nВзгляните на пример тут /help")
    except IndexError:
        bot.send_message(message.chat.id, "Неверный формат ввода задачи.\nВзгляните на пример тут /help")


@bot.message_handler(commands=["show"])
def show(message):
    """Выводит список уже сформированных задач."""
    try:
        command = message.text.split(maxsplit=1)
        date = command[1]
        if date.strip().lower() == 'all':
            if len(tasks) == 0:
                bot.send_message(message.chat.id, "В списке задач пока пусто.\nДавай что-нибудь добавим.")
            else:
                for k, v in sorted(tasks.items()):
                    bot.send_message(message.chat.id, "Дата: {}".format(k))
                    for i in v:
                        bot.send_message(message.chat.id, "- {}".format(i))
        elif len(date.split(' ')) > 1:
            date = date.split()
            for d in date:
                show_tasks(message, command[0], d)
        elif len(date.split(' ')) == 1:
            show_tasks(message, command[0], date)
    except IndexError:
        bot.send_message(message.chat.id, "Неверный формат ввода задачи.\nВзгляните на пример тут /help")


@bot.message_handler(commands=["clear"])
def clear(message):
    """Польностью очищает словарь."""
    try:
        command = message.text.split(maxsplit=1)
        text = command[1]
        if text == "Я согласен на удаление всех моих данных":
            tasks.clear()
            bot.send_message(message.chat.id, "Все данные удалены безвозвратно.")
        else:
            bot.send_message(message.chat.id,
                             "Проверочная фраза введена неверно. Попробуйте обратиться к команде /help \n"
                             "Вводите проверочную фразу без лишних пробелов и с большой буквы.")
    except IndexError:
        bot.send_message(message.chat.id, "Неверный формат ввода задачи или отсутствует валидация.\nВзгляните на пример тут /help")


bot.polling(none_stop=True)
