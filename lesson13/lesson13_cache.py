""" ИНФО
|---------------------------------------|
|   Примеры использования декораторов   |
|   cache и lru_cache в python          |
|---------------------------------------|
"""

from functools import cache, lru_cache
from random import randint
from timeit import default_timer as timer
import matplotlib.pyplot as plt


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


@cache
def fibonacci_cached(n):
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
        return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


@lru_cache(maxsize=10)
def fibonacci_lru_cached(n):
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
        return fibonacci_lru_cached(n - 1) + fibonacci_lru_cached(n - 2)
    

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


@cache
def fibonacci_closure_cached(n):
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


@lru_cache(maxsize=10)
def fibonacci_closure_lru_cached(n):
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


def check_timings(func, n=100, max_v=40, ordered=False):
    timings = [0] * n
    for i in range(n):        
        if ordered:
            v = max_v - i % max_v
        else:
            v = randint(1, max_v)
        start = timer()
        func(v)
        end = timer()
        timings[i] = end-start
    return timings


def all_timings():
    n = 100
    beg = 5
    # t_f = check_timings(fibonacci, max_v=30)
    t_f_c = check_timings(fibonacci_cached)
    t_f_lc = check_timings(fibonacci_lru_cached)
    
    t_c = check_timings(fibonacci_closure)
    t_c_c = check_timings(fibonacci_closure_cached)
    t_c_lc = check_timings(fibonacci_closure_lru_cached)
    
    t_f_c_o = check_timings(fibonacci_cached, ordered=True)
    t_f_lc_o = check_timings(fibonacci_lru_cached, ordered=True)
    
    t_c_c_o = check_timings(fibonacci_closure_cached, ordered=True)
    t_c_lc_o = check_timings(fibonacci_closure_lru_cached, ordered=True)

    # plt.plot(range(beg, n), t_f[beg:], 'cs-', linewidth=2, label='fib')
    plt.plot(range(beg, n), t_f_c[beg:], 'bs-', linewidth=2, label='fib_cached')
    plt.plot(range(beg, n), t_c[beg:], 'gs-', linewidth=2, label='closure')
    plt.plot(range(beg, n), t_c_c[beg:], 'rs-', linewidth=2, label='closure_cached')
    plt.title('Cached vs not cached')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(range(beg, n), t_f_c[beg:], 'cs-', linewidth=2, label='fib_cached')
    plt.plot(range(beg, n), t_f_lc[beg:], 'bs-', linewidth=2, label='fib_lru')
    plt.plot(range(beg, n), t_f_c_o[beg:], 'gs-', linewidth=2, label='fib_cached_o')
    plt.plot(range(beg, n), t_f_lc_o[beg:], 'rs-', linewidth=2, label='fib_lru_o')
    plt.title('Recursion (Ordered vs not ordered)')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(range(beg, n), t_c_c[beg:], 'cs-', linewidth=2, label='cached')
    plt.plot(range(beg, n), t_c_lc[beg:], 'bs-', linewidth=2, label='lru')
    plt.plot(range(beg, n), t_c_c_o[beg:], 'gs-', linewidth=2, label='cached_o')
    plt.plot(range(beg, n), t_c_lc_o[beg:], 'rs-', linewidth=2, label='lru_o')
    plt.title('Closure (Ordered vs not ordered)')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    all_timings()
    
