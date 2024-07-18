""" ИНФО
|-------------------------------------------------------|
|   Примеры создания и использования функций в python   |
|-------------------------------------------------------|
|   Будут разобраны:                                    |
|   * Модуль functools                                  |
|   * Декораторы                                        |
|   * zip, map, filter, reduce                          |
|-------------------------------------------------------|
"""
from functools import partial, update_wrapper, reduce, wraps


def functools_example():
    """ Пример работы с partial и update_wrapper """
    
    def poly_p2(x, a, b, c):
        """ Полином второй степени в общем виде """
        return a*x**2 + b*x + c
    
    print('\nПримеры работы partial')
    parabolic = partial(poly_p2, a=1, b=-2, c=1)
    squared = partial(poly_p2, a=1, b=0, c=0)
 
    print('(x - 1)^2, x = 0:', parabolic(0))
    print('x^2, x = 3:', squared(3))

    print('\nМетаданные при простом присваивании')
    p = poly_p2
    print('Name:', p.__name__)
    print('Doc:', p.__doc__)

    print('\nМетаданные при использовании partial, до update_wrapper')
    try:
        print('Name:', parabolic.__name__)
    except AttributeError: 
        print('Name: __no name__')
    
    print('Doc:', parabolic.__doc__)
    print('После update_wrapper')
    update_wrapper(parabolic, poly_p2)
    print('Name:', parabolic.__name__)
    print('Doc:', parabolic.__doc__)
    print('Keywords:', parabolic.keywords)


def decorator_function(func):
    """ Пример декоратора общего вида """
    def wrapper(*args, **kwargs):
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func(*args, **kwargs)
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def add(x, y):
    print(f'{x} + {y} = {x+y}')


def benchmark(func):
    """ Пример декоратора, засекающего время работы функции """
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


@benchmark
def fetch_webpage(url='https://google.com'):
    import requests
    webpage = requests.get(url)
    return webpage.text


@benchmark
def func_prog_example():
    print('\nmap:')
    a = list(range(10))
    b = list(map(lambda x: 20 - x, a))
    c = list(map(lambda x, y: x*y, a, b))
    print(' '.join(map(lambda x: f'{x:2d}', a)))
    print('x')
    print(' '.join(map(lambda x: f'{x:2d}', b)))
    print('=')
    print(' '.join(map(lambda x: f'{x:2d}', c)))

    print('\nzip:')
    print(list(zip(a,b)))
    print(*zip(*zip(a,b)))
    print(*zip(*zip(*zip(a,b))))

    print('\nfilter')
    print(list(filter(lambda x: x > 5, a)))
    print(list(filter(lambda x: abs(x - 15) <= 2, b)))


def reduce_example():
    _map = lambda f: lambda d: reduce(lambda x, y: x + [f(y)], d, [])
    a = list(range(10))
    b = list(_map(lambda x: 20 - x)(a))
    print(' '.join(_map(lambda x: f'{x:2d}')(a)))
    print(' '.join(_map(lambda x: f'{x:2d}')(b)))

    _sum = lambda d: reduce(lambda a, b: a+b, d, 0)
    print(_sum(a), reduce(lambda a, b: a+b[0], zip(a,b), 0))
    print(_sum(b), reduce(lambda a, b: a+b[1], zip(a,b), 0))
    
    _filter = lambda fl: lambda d: reduce(lambda x, y: x + [y] if fl(y) else x, d, [])
    print(_filter(lambda x: x > 5)(a))


if __name__ == '__main__':
    # func_prog_example()
    reduce_example()

