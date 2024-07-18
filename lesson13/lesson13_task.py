""" ИНФО
|-----------------------------------------------|
|   Работа с python без использования приемов   |
|   функционального программирования            |
|-----------------------------------------------|
|   Реализуйте следующие функции:               |
|   * no_func_prog_example() - полный аналог    |
|     func_prog_example() без использования ФП  |
|   * Декоратор, который выводит название       |
|     функции и добавляет отступы до и после    |
|     работы самой функции                      |
|   * Пример использования декоратора           |
|   * Напишите свой аналог                      |
|     функции zip с помощью reduce              |
|-----------------------------------------------|
"""

from functools import reduce


def highlighter(f):
    """
    Декоратор, который выводит название
    функции и добавляет отступы до и после
    работы самой функции

    :param f: оборачиваемая функция
    :return: обертка
    """
    def wrapper(*args, **kwargs):
        print('+'*90)
        print('Function:', f.__name__)
        return_value = f(*args, **kwargs)
        print('-'*90)
        return return_value
    return wrapper


@highlighter
def no_func_prog_example():
    a = list(range(10))
    b = [20 - e for e in a]
    c = [a[i]*b[i] for i in range(len(a))]
    print(' '.join([f'{e:2d}' for e in a]))
    print('x')
    print(' '.join([f'{e:2d}' for e in b]))
    print('=')
    print(' '.join([f'{e:2d}' for e in c]))

    print([(a[i], b[i]) for i in range(len(a))])
    # print([tuple([a[i], b[i]]) for i in range(len(a))])

    #    что?...откуда?..почему?
    print([e for e in a if e > 5])
    print([e for e in b if abs(e - 15) <= 2])


def analog_zip_example():
    a = list(range(5))
    b = [e + 7 for e in a]
    c = [e % 3 for e in b]
    d = zip(a, b, c)
    print(list(d))
    # reduce
    _zip = lambda *lists: reduce(lambda z, list:
                                 [(*z[i], list[i]) for i in range(len(list))],
                                 lists, [()]*len(lists[0]))
    print(_zip(a, b, c))
    aa = (1, 2, 3)
    bb = (*aa, 4)
    print(f'{aa} + 4 = {bb}')


if __name__ == '__main__':
    analog_zip_example()
    
