""" ИНФО
|-------------------------------------------------------|
|   Примеры создания и использования функций в python   |
|-------------------------------------------------------|
|   Будут разобраны:                                    |
|   * Синтаксис объявления функций                      |
|   * Аргументы и возвращаемые значения                 |
|   * Распаковка и упаковка аргументов                  |
|   * Аргументы по-умолчанию, аргументы-ключи           |
|   * Области видимости, правило LEGB                   |
|   * Локальные и глобальные переменные                 |
|-------------------------------------------------------|
"""

# Built-in Scope
from math import pi

# Global Scope
e = 2.718281828


def outer():
    # Enclosed Scope
    pi = 3.14
    e = 2.72
    def inner():
        print('inner:')
        # Local Scope
        global pi
        nonlocal e
        # pi = 3.1
        e = 2.7
        print(f'{pi = }')
        print(f'{e  = }')
    inner()
    print('outer:')
    print(f'{pi = }')
    print(f'{e  = }')


def scope_example():
    print('До всех присваиваний:')    
    print(f'{pi = }')
    print(f'{e  = }')
    outer()
    print('global:')
    print(f'{pi = }')
    print(f'{e  = }')


# |-------------------------------------------------------|


def some_function(aa, bb):
    """
    Некоторая функция

    Args:
        aa (int): первый аргумент
        bb (int): второй аргумент

    Returns:
        tuple: измененные аргументы
    """
    print('Внутри some_function():')
    print(f'{aa = }')
    print(f'{bb = }')
    print('Увеличим входные значения:')
    aa += 1
    bb += 1
    print(f'теперь {aa = }')
    print(f'теперь {bb = }')
    cc = aa + bb
    print(f'Сумма: {cc = }')
    return aa, bb


def run_some_function():
    """ Пример работы с some_function() """
    a, b = 3, 5
    _, b = some_function(a, b)
    print(f'{a = }')
    print(f'{b = }')
    try:
        print(f'{cc = }')
    except NameError as err:
        print(f'Error: {err}')


def process_five_numbers(num1, num2, num3, num4, num5):
    """ Пример обработки 5 входных аргументов """
    s = num1 + num2 + num3 + num4 + num5
    m = num1 * num2 * num3 * num4 * num5
    return s, m


def process_array(*arr):
    """ Пример обработки любого количества входных аргументов """
    for a in arr:
        print(a, end=' ')
    print('\n')


def packing_example():
    """ Примеры упаковки и распаковки аргументов """
    arr = list(range(1, 6))
    s, m = process_five_numbers(*arr)
    print(f'{s = }, {m = }')
    process_array(1, 2, 3, 'top', 5, 6, 7, 'банан', 77, [1, 2, 3])


def many_keys_function(arg1, arg2, opr='+', arg3=None, arg4=None, output=False):
    """
    Пример функции с аргументами-ключами и аргументами по-умолчанию

    Args:
        arg1 (float): Первое число в выражении
        arg2 (float): Второе число в выражении
        opr (str, optional): Оператор. Defaults to '+'.
        arg3 (float, optional): Третье число в выражении. Defaults to None.
        arg4 (float, optional): Четвертое число в выражении. Defaults to None.
        output (bool, optional): Флаг вывода на экран. Defaults to False.

    Returns:
        (float): результат вычислений
    """
    args = [arg1, arg2]
    if arg3 is not None:
        args.append(arg3)
    if arg4 is not None:
        args.append(arg4)
    
    ans = arg1
    for a in args[1:]:
        if opr == '+':
            ans += a
        elif opr == '-':
            ans -= a
        elif opr == '*':
            ans *= a
        elif opr == '/':
            ans /= a
    
    if output:
        str_args = [f'{a}' for a in args]
        eq = f' {opr} '.join(str_args)
        print(f'{eq} = {ans}')
    
    return ans


def func_keys_example():
    a, b = 3, 5
    c = many_keys_function(a, b)
    print(f'{a} + {b} = {c}')
    c = many_keys_function(a, b, '-')
    print(f'{a} - {b} = {c}')
    c = many_keys_function(a, b, arg3=3, opr='*')
    print(f'{a} * {b} * 3 = {c}')
    many_keys_function(a, b, arg3=2, arg4=7, output=True)
    many_keys_function(a, b, '*', 2, 1, True)


def print_figure(w, h, sym='#', fig_type='square', filled=True):
    if fig_type == 'square':
        for i in range(h):
            for j in range(w):
                if filled:
                    print(sym, end='')
                elif i == 0 or i == h-1:
                    print(sym, end='')
                elif j == 0 or j == w-1:
                    print(sym, end='')
                else:
                    print(' ', end='')
            print('')


if __name__ == '__main__':
    scope_example()
