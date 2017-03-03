import sys


def action_show_menu():
    print('''
Ежедневник. Выберите действие

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход''')

def action_exit():
    sys.exit(0)

actions = {
    'm': action_show_menu,
    'q': action_exit
}


if __name__ == '__main__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Не известная команда')
