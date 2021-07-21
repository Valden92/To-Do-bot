HELP = """
Что может To-Do бот:
* help - напечатать справку о программе.
* add - добавить новую задачу в список.
* show - напечатать все добавленные задачи.
* exit - завершение работы с приложением (работает в любой момент).
"""

tasks = {}
flag = True

def add_input_validation(date):
    """Проверяет правильность ввода даты."""
    import datetime, time
    date_now = datetime.datetime.today().strftime('%d.%m.%Y')
    try:
        valid_date = time.strptime(date, '%d.%m.%Y')
        date_now = time.strptime(date_now, '%d.%m.%Y')
        if valid_date >= date_now:
            return True
        else:
            print('Невозможно сделать запись в прошлое.')
            return False
    except ValueError:
        return False

while flag:
    command = input('Введите команду из меню: ')
    if command.strip().lower() == 'help':
        # Выводит меню помощи
        print(HELP)
    elif command.strip().lower() == 'show':
        # Показывает задачи в хранилище задач
        date = input()
    elif command.strip().lower() == 'add':
        # Позволяет сохранять новые задачи
        date = input('Введите дату в формате (ДД.ММ.ГГГГ): ').strip()
        if add_input_validation(date):
            task = input('Введите название задачи: ')
            if date in tasks.keys():
                tasks[date].append(date)
            elif task.strip().lower() == 'exit':
                # Завершает работу приложения
                print('\nСпасибо за использование приложения!\n'
                      'До встречи!')
                break
            else:
                tasks[date] = []
                tasks[date].append(task)
        elif date.strip().lower() == 'exit':
            # Завершает работу приложения
            print('\nСпасибо за использование приложения!\n'
                  'До встречи!')
            break
        else:
            print('\nНеверный формат ввода даты!\n'
                  'Попробуйте еще раз.')
            continue
    elif command.strip().lower() == 'exit':
        # Завершает работу приложения
        print('\nСпасибо за использование приложения!\n'
              'До встречи!')
        break
    else:
        print('\nТакой команды нет в приложении.\n'
              'Ошибка ввода!\n'
              'Попробуйте еще раз.')
        continue
