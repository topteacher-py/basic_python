""" ИНФО
|-------------------------------------------------------|
|   Оценка времени работы программы при использовании   |
|   различных вариантов создания списков                |
|-------------------------------------------------------|
"""

import numpy.random as nprnd
import timeit

random_list = list(nprnd.randint(1000, size=10000))


def slow_dynamic_list(a):
    # выделяем память динамически под каждый новый элемент
    b = []
    for _a in a:
        b.append(_a**2)
    return b


def slow_static_list(a):
    # сначала выделяем память, потом записываем данные
    b = [0] * len(a)
    for i in range(len(a)):
        b[i] = a[i]**2
    return b


def fast_list(a):
    b = [_a**2 for _a in a]
    return b


def speed_test():
    loop = 1000
    t1 = timeit.timeit(stmt='slow_static_list(random_list)', globals=globals(), number=loop)
    t2 = timeit.timeit(stmt='slow_dynamic_list(random_list)', globals=globals(), number=loop)
    t3 = timeit.timeit(stmt='fast_list(random_list)', globals=globals(), number=loop)
    print('slow static:\t', t1 / loop)
    print('slow dynamic:\t', t2 / loop)
    print('fast:\t\t\t', t3 / loop)


if __name__ == '__main__':
    speed_test()
