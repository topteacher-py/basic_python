

def multy_table(col_beg, col_end, row_beg, row_end):
    h = col_end - col_beg + 1
    w = row_end - row_beg + 1
    multy = [0] * h  # пустая таблица из h строк
    for i in range(h):
        new_string = [0] * w  # пустая строка из w чисел
        for j in range(w):
            new_string[j] = (i + col_beg) * (j + row_beg)
        multy[i] = new_string
    return multy


def show_table(table):
    h = len(table)  # высота (количество строк)
    w = len(table[0])  # ширина (количество столбцов)
    for i in range(h):
        for j in range(w):
            print(f'{table[i][j]:3d}', end=' ')
        print('')


if __name__ == '__main__':
    multy = multy_table(0, 37, 0, 27)
    show_table(multy)
