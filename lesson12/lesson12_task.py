""" ИНФО
|-------------------------------------------|
|   Задание: Создайте комплекс функций      |
|   для отрисовки золотых прямоугольников   |
|-------------------------------------------|
|   Предлагаю реализовать функции:          |
|   * calc_image_size - размер изображения  |
|   * rectangle_coords - координаты         |
|   * golden_rectangles - отрисовка         |
|   * дополнительные при необходимости      |
|-------------------------------------------|
|   * Реализовать весь функционал для       | 
|     цветного изображения (опционально)    |
|-------------------------------------------|
"""

import numpy as np
from PIL import Image
from lesson12 import fibonacci_closure


def calc_image_size(n, side):
    """
    Рассчитывает размер изображения
    для отрисовки золотых прямоугольников

    Args:
        n (int): количество прямоугольников
        side (int): длина стороны наименьшего прямоугольника

    Returns:
        Tuple[int, int]: размеры изображения
    """
    v = calc_vector(n)
    if v in ['left', 'right']:
        h = fibonacci_closure(n) * side
        w = fibonacci_closure(n + 1) * side
    else:
        h = fibonacci_closure(n + 1) * side
        w = fibonacci_closure(n) * side
    return 2 * h, 2 * w


def calc_vector(n):
    """
    Рассчитывает направления присоединения
    n-го прямоугольника
    :param n: номер прямоугольника
    :return: направление
    """
    if n == 1:
        return 'begin'
    v = (n-1) % 4
    if v == 1:
        return 'left'
    elif v == 2:
        return 'down'
    elif v == 3:
        return 'right'
    else:
        return 'up'


def rectangle_coords(n, side, img_size):
    """
    Рассчитывает координаты прямоугольника
    по его номеру и единичной длине стороны 

    Args:
        n (int): номер прямоугольника
        side (int): единичная длина стороны
        img_size : размер изображения

    Returns:
        Tuple[int, int, int, int]: координаты прямоугольника
    """
    h, w = img_size
    # координаты первого квадрата
    x0, y0 = int(-side/2 + w/2), int(-side/2 + h/2)
    x1, y1 = int(side/2 + w/2), int(side/2 + h/2)
    for i in range(2, n+1):
        phi = fibonacci_closure(i)
        v = calc_vector(i)
        s = side * phi
        if v == 'left':
            x0, y0 = x0 - s, y0
            x1, y1 = x0 + s, y0 + s
        elif v == 'down':
            x0, y0 = x0, y1
            x1, y1 = x0 + s, y0 + s
        elif v == 'right':
            x0, y0 = x1, y1 - s
            x1, y1 = x0 + s, y1
        elif v == 'up':
            x0, y0 = x1 - s, y0 - s
            x1, y1 = x1, y0 + s

    return x0, y0, x1, y1


def plot_rect(image, coords, color):
    """
    Отрисовка квадратика на изображении
    :param image: изображение
    :param coords: координаты
    :param color: цвет
    :return: изображение с квадратиком
    """
    x0, y0, x1, y1 = coords
    h, w = y1 - y0, x1 - x0
    image[y0:y1, x0:x1, :] = np.array([[[color, 255, 255]] * w] * h)
    return image


def golden_rectangles(n, side):
    """
    Отрисовывает разными цветами n золотых
    прямоугольников на изображении

    Args:
        n (int): количество прямоугольников
        side (int): единичная длина стороны
    """
    img_size = calc_image_size(n, side)
    h, w = img_size
    src = np.zeros((h, w, 3), dtype='uint8')
    colors = [int(255 / n * (i + 0.5)) for i in range(n)]
    for i in range(1, n+1):
        coords = rectangle_coords(i, side, img_size)
        src = plot_rect(src, coords, colors[i-1])

    x_beg = y_beg = x_end = y_end = -1
    for y in range(h):
        for x in range(w):
            if src[y, x, 1] and x_beg < 0:
                x_beg, y_beg = x, y
            if src[-y-1, -x-1, 1] and x_end < 0:
                x_end, y_end = w - x, h - y
            if x_beg >= 0 and x_end >= 0:
                break
        else:
            continue
        break
    img = Image.fromarray(src[y_beg:y_end, x_beg:x_end],
                          mode="HSV")
    img.show()
    # img.save('fibonacci.png')


if __name__ == '__main__':
    # количество золотых прямоугольников
    n = 6
    # Длина стороны первого прямоугольника в пикселях
    side = 20
    golden_rectangles(n, side)
    
    