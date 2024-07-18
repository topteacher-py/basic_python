""" ИНФО
|-------------------------------------------------------|
|   Примеры создания и использования функций в python   |
|-------------------------------------------------------|
|   Будут разобраны:                                    |
|   * Функции как аргументы функций                     |
|   * Рекурсия                                          |
|   * lambda-функции                                    |
|   * Замыкания                                         |
|-------------------------------------------------------|
"""


def lambda_examples():
    """
        Примеры работы с lambda-функциями
        
        Формат:
        lambda список_аргументов: выражение
    """
    print('\nlambda-функция как альтернатива def-функции')

    def sm(x, y):
        return x + y

    a = sm(5, 7)
    print('5 + 7 =', a)
    a = (lambda x, y: x+y)(5, 7)
    print('5 + 7 =', a)

    print('\nв некоторых случаях можно обойтись без lambda-функции')
    a = list(range(10))
    print(list(filter(lambda b: b%2 == 0, a)))
    print([b for b in a if b%2 == 0])


def fp_examples():
    """ Примеры функционального программирования в python """
    print('\nфункция как входной аргумент')

    def repeat(func, n):
        for i in range(n):
            func()
    
    def hello():
        print("Hello, world!")
    
    repeat(hello, 3)


    print('\nфункция как входной и выходной аргумент')

    def composite(function1, function2):
        def inner(argument):
            return function1(function2(argument))
        return inner
    
    def x3(a):
        return a*3

    def x5(a):
        return a*5
    
    x15 = composite(x3, x5)
    print(x15(3))


def fibonacci(n):
    """
    Рекурсивный подсчет n-го числа Фибоначчи
    Args:
        n (int): номер числа

    Returns:
        int: Число Фибоначчи
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_gen():
    """ Реализация подсчета чисел Фибоначчи через генератор с замыканием"""
    x1 = 0
    x2 = 1

    def get_next_number():
        nonlocal x1, x2
        x1, x2 = x2, x1 + x2
        return x2

    return get_next_number


def fibonacci_closure(n):
    """
    Подсчет n-го числа Фибоначчи через замыкание
    Args:
        n (int): номер числа

    Returns:
        int: Число Фибоначчи
    """
    f = fib_gen()
    num = 1
    for _ in range(2, n+1):
        num = f()
    return num


def golden_ratio():
    """ Золотое сечение """
    phi = (1 + 5**0.5) / 2
    print(phi)
    print(1 + 1 / phi)
    print(phi * phi - 1)
    print(fibonacci(30) / fibonacci(29))


def print_fib(n):
    for i in range(1, n+1):
        print(f'{i:3d}', fibonacci_closure(i))


if __name__ == '__main__':
    print_fib(6)
    
