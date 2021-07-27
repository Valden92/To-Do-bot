HELP = """
Что может To-Do бот:
* help - напечатать справку о программе.
* add - добавить новую задачу в список.
* show - напечатать все добавленные задачи.
* exit - завершение работы с приложением (работает в любой момент).
"""

tasks = {}
flag = True

def input_validation(command, date):
    """Проверяет правильность ввода даты."""
    import datetime, time

    if command.strip().lower() == 'add':
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
    elif command.strip().lower() == 'show':
        try:
            valid_date = time.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False


while flag:
    command = input('Введите команду из меню: ')
    if command.strip().lower() == 'help':
        # Выводит меню помощи
        print(HELP)
    elif command.strip().lower() == 'show':
        # Показывает задачи в хранилище задач
        date = input('Введите дату в формате (ДД.ММ.ГГГГ) '
                     'или "all" для вывода полного списка задач: ')
        if date.strip().lower() == 'all':
            for k, v in sorted(tasks.items()):
                print('Дата: {}'.format(k))
                for i in v:
                    print('- {}'.format(i.lower().capitalize()), end='\n')
        elif date.strip().lower() == 'exit':
            # Завершает работу приложения
            print('\nСпасибо за использование приложения!\n'
                  'До встречи!')
            break
        elif input_validation(command, date):
            if date in tasks.keys():
                print('Дата: {}'.format(date))
                for i in tasks[date]:
                    print('- {}'.format(i.lower().capitalize()), end='\n')
            else:
                print('На эту дату ничего не запланировано.')
                continue
        else:
            print('\nНеверный формат ввода!\n'
                  'Попробуйте еще раз.')
            continue
    elif command.strip().lower() == 'add':
        # Позволяет сохранять новые задачи
        date = input('Введите дату в формате (ДД.ММ.ГГГГ): ').strip()
        if input_validation(command, date):
            task = input('Введите название задачи: ')
            if date in tasks.keys():
                tasks[date].append(task)
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
