from PIL import Image
import numpy as np


def show_image(path):    
    """ Выводит выбранное изображение на экран

    Args:
        path (str): Путь до изображения
    """
    img = Image.open(path)
    img.show()


def convert_image_to_gray(path):
    """ Конвертирует выбранное изображение в черно-белое

    Args:
        path (str): Путь до изображению
    """
    img = Image.open(path).convert('L')
    img.save('grayscale.png')


def convert_image_to_gray_by_pixels(path):
    """ Конвертирует выбранное изображение в черно-белое попиксельно

    Args:
        path (str): Путь до изображения
    """
    img = Image.open(path)
    w, h = img.size
    pix = np.array(img)
    print(pix)

    for i in range(h):
        for j in range(w):
            r, g, b = pix[i, j]
            gray = int((0.2989 * r) + (0.5870 * g) + (0.1140 * b))
            pix[i, j] = np.array([gray] * 3)
    
    gray = Image.fromarray(pix)
    gray.save('grayscale.png')


def malevich(path, size=(100, 100)):
    """ Рисует черный прямоугольник по центру изображения

    Args:
        path (str): Путь до изображения
        size (tuple, optional): Размер прямоугольника. Defaults to (100, 100).
    """
    img = Image.open(path)
    w, h = img.size
    sw, sh = size
    # закрашиваемая область должна быть не больше самого изображения
    if sw > w:
        sw = w
    if sh > h:
        sh = h

    cx, cy = w / 2, h / 2
    x1, x2 = int(cx - sw / 2), int(cx + sw / 2)
    y1, y2 = int(cy - sh / 2), int(cy + sh / 2)
    pix = np.array(img)
    pix[y1:y2, x1:x2] = np.ones((sh, sw, 3))*240
    mal = Image.fromarray(pix)
    mal.save('malevich.png')


def shadow(path, size=(100, 100), alpha=0.5):
    """ Затеняет выбранную область изображения

    Args:
        path (str): Путь до изображения
        size (tuple, optional): Размер прямоугольника. Defaults to (100, 100).
        alpha (float, optional): Коэффициент наложения. Defaults to 0.5.
    """
    img = Image.open(path)
    w, h = img.size
    sw, sh = size
    # закрашиваемая область должна быть не больше самого изображения
    if sw > w:
        sw = w
    if sh > h:
        sh = h

    cx, cy = w / 2, h / 2
    x1, x2 = int(cx - sw / 2), int(cx + sw / 2)
    y1, y2 = int(cy - sh / 2), int(cy + sh / 2)
    pix = np.array(img)
    area = np.array([[[0, 255, 255]] * sw] * sh) * alpha
    pix[y1:y2, x1:x2] = pix[y1:y2, x1:x2] * (1 - alpha) + area
    
    shd = Image.fromarray(pix)
    shd.save('shadow.png')


def change_color(path):
    old_color = np.array([180, 0, 0])
    new_color = np.array([0, 255, 0])
    diff = 100

    img = Image.open(path)
    w, h = img.size
    pix = np.array(img)

    for i in range(h):
        for j in range(w):
            color = pix[i, j]
            if np.linalg.norm(color-old_color) < diff:
                pix[i, j] = new_color

    chg = Image.fromarray(pix)
    chg.save('changed.png')


def change_color_hsv(path):
    old_h1 = 255
    old_h2 = 0
    new_h = 90
    diff = 25

    img = Image.open(path)
    img = img.convert('HSV')
    w, h = img.size
    pix = np.array(img)

    for i in range(h):
        for j in range(w):
            hue, s, v = pix[i, j]
            if abs(hue-old_h1) < diff or abs(hue-old_h2) < diff:
                pix[i, j] = np.array([new_h, s, v])

    chg = Image.fromarray(pix, mode='HSV')
    chg.convert('RGB').save('changed.png')


if __name__ == '__main__':
    path = "top_logo.png"
    change_color_hsv(path)