""" ИНФО
|---------------------------------------------------|
|   Примеры создания и обработки списков в python   |
|---------------------------------------------------|
|   Будут разобраны:                                |
|   * Инициализация списков                         |
|   * Индексация списков и функция slice()          |
|   * Методы append(), insert(), extend()           |
|   * Генераторы                                    |
|---------------------------------------------------|
"""


def lists_example():
    """ Примеры различных списков """
    print('список чисел:')
    a = list(range(5))
    print(f'{a = }')
    print('список строк:')
    b = ['apples', 'bananas', 'oranges']
    print(f'{b = }')
    print('список с заданной длинной:')
    c = [0] * 7
    print(f'{c = }')
    print('список списков:')
    d = [a, b, ['+', '*', '=']]
    print(f'{d = }')


def indexing_example():
    """ Примеры работы с индексами в строках и списках """    
    a = list(range(10))
    print(f'{a = }')
    print(f'{a[0] = }')
    print(f'{a[3] = }')
    print(f'{a[len(a)-1] = }')
    # -ind - означает номер индекса (ind) с конца
    print(f'{a[-1] = }')
    print(f'{a[-3] = }')
    b = ['яблоки', 'бананы', 'апельсины']
    print(f'\n{b = }')
    print(f'{b[2] = }')
    print(f'{b[2][3] = }')
    i = b.index('бананы')
    print(f"индекс слова 'бананы' {i}")
    c = [a, b, ['+', '*', '=']]
    print('\nвывод в цикле:')
    for i in range(len(c)):
        print(f'c[{i}] = {c[i]}')


def slice_example_1():
    """ Примеры работы с функцией slice() """    
    a = list(range(10))
    print(f'{a = }')
    s = slice(1, 9, 1)
    """ slice(start, stop, step)
        start - индекс начала
        stop  - индекс конца
        step  - размер шага по индексам
    """
    b = a[s]
    print(f'{b = }')    
    s = slice(9, 0, -2)
    c = a[s]
    print(f'{c = }')


def slice_example_2():
    """ Примеры работы с индексами без функции slice """    
    a = list(range(10))
    print(f'{a = }')
    b = a[1:9:1]
    print(f'{b = }')  
    c = a[-1:0:-2]
    print(f'{c = }')


def methods_example():
    """ Примеры добавления элементов в списки """
    a = list(range(5))
    print(f'{a = }')
    a.append(10)
    print(f'После append(10):\n{a = }')
    a.insert(3, 33)
    print(f'После insert(3, 33):\n{a = }')
    b = [1] * 3
    print(f'\n{b = }')
    a.extend(b)
    print(f'После a.extend(b):\n{a = }')
    c = ['a'] * 3
    print(f'\n{c = }')
    c += b
    print(f'После c += b:\n{c = }')
    

def increment_generator(listed):
    """ Пример генератора, который прибавляет ко всем элементам списка 1

    Args:
        listed : список чисел
    """
    for l in listed:
        # аналог return для генераторов
        yield l+1


def generator_example():
    """ Пример работы с генератором """
    a = list(range(10))
    print(f'{a = }')
    # *list - превращает список в перечисление его элементов
    print(f'*a =', *a)
    print(f'{type(a) = }\n')

    b = increment_generator(a)
    print(f'{b = }')
    print(f'{type(b) = }\n')

    print('работаем с b как с iterable:')
    for _b in b:
        print(_b, end = ' ')
    
    print('\n\nРаботаем с b как с subscriptable:')
    try:
        print(b[0])
    except Exception as err:
        print('Ошибка:', err)


def mini_task():
    a = list(range(20))
    print(f'{a = }')
    print(f'Первый элемент: {a[0]}')
    print(f'Первый элемент: {a[-20]}')
    print(f'Последний элемент: {a[-1]}')
    print(f'Четные числа: {a[::2]}')
    print(f'Нечетные числа: {a[1::2]}')
    print(f'Первые 5 чисел: {a[:5]}')
    print(f'Последние 5 чисел: {a[-5:]}')
    print(f'И они же по убыванию: {a[-1:-6:-1]}')
    b = 'hello'
    print(f'Реверс: {b[::-1]}')


def copying_example():
    a = [1, 2, 3]
    b = a[:]
    print(f'{id(a) = }')
    print(f'{id(b) = }')
    # print(f'{a = }')
    # print(f'{b = }')
    # b[2] = 'банан'
    # print(f'{a = }')
    # print(f'{b = }')


def draw_circle():
    r = 10
    s = '$$'
    # x^2 + y^2 = r^2
    # r = 5
    for y in range(-r, r+1):
        for x in range(-r, r+1):
            r_curr_2 = abs(x**2) + abs(y**2)
            if 0 < r*r - r_curr_2 < 50:
                print(s, end='')
            else:
                print('  ', end='')
        print('')


if __name__ == '__main__':
    draw_circle()
