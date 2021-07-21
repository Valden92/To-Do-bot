help = """
Что может To-Do бот:
* help - напечатать справку о программе.
* add - добавить новую задачу в список.
* show - напечатать все добавленные задачи.
* exit - завершение работы с приложением.
"""

today = []
tomorrow = []
others = []

def tasks_append(tasks):
    task = input('Введите название задачи: ')
    tasks.append(task)
    print('Ваша задача добавлена.')

def tasks_show(tasks):
    print(*tasks, sep='\n')


while True:
    command = input('Веедите команду: ')
    if command == 'help':
        print(help)
    elif command == 'show':
        qw = input('Из какого списка показать заздачи?\n'
                   '(Сегодня, Завтра, Когда-нибудь, Все списки): ')
        print('\n')
        if qw.strip().lower() == 'сегодня':
            if len(today) > 0:
                print('Задачи на сегодня:')
                tasks_show(today)
            else:
                print('Задач пока нет.')
        elif qw.strip().lower() == 'завтра':
            if len(tomorrow) > 0:
                print('Задачи на завтра:')
                tasks_show(tomorrow)
            else:
                print('Задач пока нет.')
        elif qw.strip().lower() == 'когда-нибудь':
            if len(others) > 0:
                print('Задачи на когда-нибудь:')
                tasks_show(others)
            else:
                print('Задач пока нет.')
        elif qw.strip().lower() == 'все списки':
            if len(today) > 0:
                print('Задачи на сегодня:')
                tasks_show(today)
            else:
                print('Задач на сегодня пока нет.')
            if len(tomorrow) > 0:
                print('Задачи на завтра:')
                tasks_show(tomorrow)
            else:
                print('Задач на завтра пока нет.')
            if len(others) > 0:
                print('Задачи на когда-нибудь:')
                tasks_show(others)
            else:
                print('Задач на когда-нибудь пока нет.')
        else:
            print('Неизвестная задача!'
                  'Попробуйте еще раз.')
            continue
    elif command == 'add':
        day = input('Выберите время для выполенения задачи\n'
                    '(Сегодня, Завтра, Когда-нибудь): ')
        print('\n')
        if day.strip().lower() == 'сегодня':
            tasks_append(today)
        elif day.strip().lower() == 'завтра':
            tasks_append(tomorrow)
        elif day.strip().lower() == 'когда-нибудь':
            tasks_append(others)
        else:
            print('Неизвестная задача!'
                  'Попробуйте еще раз.')
            continue
    elif command == 'exit':
        print('\n')
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная задача!'
              'Попробуйте еще раз.')
        continue
