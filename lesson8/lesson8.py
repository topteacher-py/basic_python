def example1():
    # \' - экранирование символа
    string = 'abc123#@+\', "hello"'
    string1 = '123a bbc acd amb cdab'
    print(string1)
    # print(len(string))  # вычисляет длину строки
    string_list = list(string)  # превращаем строку в список
    # print(string_list)
    print(string1.split('a'))
    print('A'.join(string1.split('a')))
    print('_'.join(string1.split(' ')))


def work_with_text():
    text = 'Зинаида Николаевна Некрасова (урождённая Фёкла Анисимовна Викторова,' \
           ' вторая половина сентября (?) 1846 (?), Вышний Волочёк (?),' \
           ' Российская империя — 25 января 1915, Саратов) — супруга и' \
           ' сотрудница российского поэта, публициста и общественного' \
           ' деятеля Николая Алексеевича Некрасова; О её детстве и юности' \
           ' практически ничего не известно. Существуют различные версии' \
           ' даты её рождения, происхождения и обстоятельств знакомства' \
           ' с поэтом. Девушка познакомилась с поэтом в 1870 году и сразу' \
           ' стала близким для него человеком; Некрасов много сделал, чтобы' \
           ' дать ей достойное образование, ввёл её в круг своих близких' \
           ' друзей и родственников. Зинаида Николаевна выполняла некоторые' \
           ' поручения поэта при корректировке и публикации его произведений.' \
           ' Зинаиде Некрасовой поэт посвятил поэму «Дедушка», а также минимум три' \
           ' стихотворения в книге «Последние песни», права на публикацию которой' \
           ' были переданы автором супруге. Она участвовала в издании и распространении' \
           ' дешёвых изданий стихотворений супруга.'

    splitted_text = text.split('.')  # части текста, разделенные точками
    sentence_num = 0
    for t in splitted_text:
        for st in t.split(';'):
            if st != '':
                sentence_num += 1
    print('Количество предложений:', sentence_num)


def super_split(text, delimeters):
    """
    Разделяет text с учетом всех разделителей из списка
    :param text:        текст для обработки
    :param delimeters:  список разделителей
    :return:            список разделенных частей текста
    """
    # переменная для хранения полностью разделенных частей текста
    splitted = [text]  # список из 1 элемента
    for d in delimeters:  # цикл по разделителям
        """ на каждой итерации все предложения разделяются
            новым разделителем и сохраняются в виде нового списка """
        more_splitted = []  # пустой список
        for s in splitted:
            """ ---- 2й вариант
            ms = s.split(d)
            # lambda - маленькая локальная функция
            # фильтруем список предложений от пустых
            ms = filter(lambda _ms: _ms != '', ms)
            more_splitted += ms
            """
            # ---- 2й вариант (укороченный)
            more_splitted += filter(lambda _s: _s != '', s.split(d))
            """ ---- 1й вариант
            for st in s.split(d):
                if st != '':
                    # добавить элемент в конец списка
                    more_splitted.append(st)
            """
        # сохраняем новый список предложений
        print(more_splitted)
        splitted = more_splitted
    return splitted


def super_split_use():
    text = 'aaa. bbb; ccc.; ddd|||, eee@eee.mail.ru'
    splitted = super_split(text, delimeters=['.', ';', '|', '@', ' ', ','])
    for s in splitted:
        print(f'{s = }')


def work_with_file():
    # открываем файл random_text.txt ТОЛЬКО для записи
    # флаг w - для записи (write)
    # флаг r - для чтения (read)
    # флаг a - дозаписать файл (append)
    with open('random_text.txt', 'a') as f:
        f.write('A'*500)

    with open('random_text.txt', 'r') as f:
        text = f.read()
    print(len(text))


if __name__ == '__main__':
    example1()
