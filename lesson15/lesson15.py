"""
Алгоритмы сортировки
"""
import random
from timeit import default_timer as timer


def basic_sort():
    n = 20
    a = [random.randint(-50, 50) for _ in range(n)]
    print(*a)
    a.sort(key=lambda x: x**2)
    print(*a)
    a.sort(reverse=True)
    print(*a)


def bubble_sort():
    n = 1000
    a = [random.randint(1, n) for _ in range(n)]
    while True:
        # флаг замены элементов
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                swapped = True  # произошла замена
                a[i], a[i+1] = a[i+1], a[i]  # замена
        # если не было ни одной замены,
        # значит, список полностью отсортирован
        if not swapped:
            break


def shaker_sort():
    n = 1000
    a = [random.randint(1, n) for _ in range(n)]
    while True:
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                swapped = True
                a[i], a[i+1] = a[i+1], a[i]
        for i in range(len(a)-1, 0, -1):
            if a[i] < a[i-1]:
                swapped = True
                a[i], a[i-1] = a[i-1], a[i]
        if not swapped:
            break


def check_timings():
    n = 1000
    start = timer()
    for _ in range(n):
        bubble_sort()
    end = timer()
    print('Пузырек: ', (end-start)/n)
    start = timer()
    for _ in range(n):
        shaker_sort()
    end = timer()
    print('Шейкер:  ', (end-start)/n)


def search_example():
    a = random.sample(list(range(10000)), 1000)
    b = random.randint(0, 10000)
    # линейный
    for i, e in enumerate(a):
        if e == b:
            print(f'Элемент {b} найден под номером {i}')
            break
        elif i == len(a)-1:
            print(f'Элемент {b} не найден')
    # бинарный
    a.sort()
    beg = 0
    end = len(a)
    while (end - beg) >= 2:
        cnt = (beg + end) // 2
        if a[cnt] == b:
            print(f'Элемент {b} найден под номером {cnt}')
            break
        elif a[cnt] > b:  # b слева
            end = cnt
        else:  # b справа
            beg = cnt
    else:
        print(f'Элемент {b} не найден')


if __name__ == '__main__':
    search_example()
