""" ЗАДАНИЕ
|-------------------------------------------------------------------------------|
|   Реализуйте интерфейс работы с импровизированной базой данных                |
|-------------------------------------------------------------------------------|
|   В качестве примера в базу уже добавлены записи одного студента              |
|-------------------------------------------------------------------------------|
|   Весь пользовательский интерфейс предлагается реализовать внутри функции     |
|   data_base_interface()                                                       |
|   Так же необходимо реализовать функции распечатывания БД, добавления и       |
|   удаления студентов из БД, которые будут вызваться из интерфейса             |
|-------------------------------------------------------------------------------|
|   Доп. задание 1.                                                             |
|   Добавьте возможность изменения имени и предметов студента по его id         |
|-------------------------------------------------------------------------------|
|   Доп. задание 2*.                                                            |
|   Добавьте возможность сохранения и выгрузки БД из файла                      |
|-------------------------------------------------------------------------------|
"""

import random

# Глобальные переменные для хранения базы данных
global g_id_list, g_name_list, g_subjects_list

g_id_list = [123456]
g_name_list = ['Игорь Горшков']
g_subjects_list = [['ОБЖ', 'Геометрия', 'Химия']]


def get_new_id():
    """ Генерирует случайный шестизначный идентификатор студента

    Returns:
        Идентификатор (int): число в интервале от 100000 до 999999
    """
    return random.randint(100000, 999999)


def add_student(name, subjects):
    """ Добавляет в базу данных информацию о студенте

    Args:
        name (str): Имя Фамилия студента
        subjects (list[str]): Список предметов
    """
    sid = get_new_id()
    while sid in g_id_list:
        sid = get_new_id()
    g_id_list.append(sid)
    g_name_list.append(name)
    g_subjects_list.append(subjects)


def del_student(sid):
    """ Удаляет студента из БД по идентификатору

    Args:
        sid (int): Идентификатор
    """
    if sid not in g_id_list:
        print('Неверный номер студента.')
        return
    # порядковый номер студента в БД
    ind = g_id_list.index(sid)
    # имя студента для вывода информации
    name = g_name_list[ind]
    # удаляем студента из БД
    del g_id_list[ind]
    del g_name_list[ind]
    del g_subjects_list[ind]
    # выводим информационное сообщение
    print(f'Студент {name} удален из БД.')


def print_data_base():
    """ Распечатывает в консоль базу данных """
    L = len(g_id_list)
    print(f'БД содержит {L} записей:')
    for i in range(L):
        subjects = ', '.join(g_subjects_list[i])
        print(g_id_list[i], g_name_list[i],
              'Предметы:', subjects, sep='\t')


def change_student_info(sid, name=None, subjects=None):
    """
    Меняет информацию о студенте
    :param sid:          идентификатор студента
    :param name:        новое имя студента
    :param subjects:    новые предметы студента
    """
    if sid not in g_id_list:
        print('Неверный номер студента.')
        return
    # порядковый номер студента в БД
    ind = g_id_list.index(sid)
    if name is not None:
        g_name_list[ind] = name
    if subjects is not None:
        g_subjects_list[ind] = subjects
    print(f'Запись под номером {sid} успешно обновлена.')


def save_to_file():
    path = 'students_db.txt'
    with open(path, 'w') as f:
        # создаем список id, хранящихся в виде строк
        str_id_list = [f'{sid}' for sid in g_id_list]
        f.write('&'.join(str_id_list) + '\n')
        f.write('&'.join(g_name_list) + '\n')
        str_subjects_list = '&'.join(['@'.join(s) for s in g_subjects_list])
        f.write(str_subjects_list + '\n')


def read_from_file():
    path = 'students_db.txt'
    with open(path, 'r') as f:
        global g_id_list, g_name_list, g_subjects_list
        id_line = f.readline()[:-1]
        id_list = id_line.split('&')
        g_id_list = [int(sid) for sid in id_list]
        g_name_list = f.readline()[:-1].split('&')
        subjects_list = f.readline()[:-1].split('&')
        g_subjects_list = [s.split('@') for s in subjects_list]


def data_base_interface():
    """ Интерфейс для работы с БД """
    spr = '-'*42
    print(spr, '   Вас приветствует служба работы с БД!', spr, sep='\n')
    while True:
        print(spr)
        print('Выберите действие:\n\t'
              '1 - Вывести БД\n\t'
              '2 - Добавить студента в БД\n\t'
              '3 - Удалить студента из БД\n\t'
              '4 - Изменить информацию о студенте\n\t'
              '5 - Выйти из программы')
        action = input()
        print(spr)
        if action == '1':
            print_data_base()
        elif action == '2':
            name = input('Введите ИФ студента: ')
            print('Введите изучаемые предметы (через ,):')
            subjects = input().split(',')
            add_student(name, subjects)
        elif action == '3':
            try:
                sid = int(input('Введите номер студента: '))
            except ValueError:
                continue
            del_student(sid)
        elif action == '4':
            try:
                sid = int(input('Введите номер студента: '))
            except ValueError:
                continue
            choice = input('Поменяем ИФ(n) или предметы?: ')
            if choice.lower() == 'n':
                name_and_surname = input('Введите ИФ студента: ')
                # указываем только ИФ, предметы не меняются
                change_student_info(sid, name=name_and_surname)
            else:
                print('Введите изучаемые предметы (через ,):')
                subjects_list = input().split(',')
                # указываем только предметы, ИФ не меняются
                change_student_info(sid, subjects=subjects_list)
        elif action == '5':
            break


if __name__ == '__main__':
    # data_base_interface()
    read_from_file()
    print_data_base()
