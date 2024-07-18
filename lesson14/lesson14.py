import random
import json


def tuple_list_example():
    t = (1, 2, 3)
    l = [1, 2, 3]
    print(type(t))
    print(type(l))
    print(t == l)
    print(list(t) == l)
    print(tuple(l) == t)
    print('\nизменяемость list:')
    print(id(l))
    l.append(4)
    print(id(l))
    print(l)
    print('\nнеизменяемости tuple:')
    print(id(t))
    t = (*t, 4)
    print(id(t))
    print('\nсхожесть:')
    for i in l:
        print(i, end=' ')
    print('')
    for i in t:
        print(i, end=' ')
    print('')


def set_example():
    # set - множество
    print('Пустое множество:', {})
    a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    s = set(a)
    print(s)
    print(set('hello world'))
    print('\nhash')
    try:
        print({[1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2]})
    except Exception as ex:
        print(ex)
    h = [(1, 2, 3), (3, 2, 1), (1, 2, 3), (1, 2)]
    print(set(h))
    print([hash(e) for e in h])
    print([hash(e) for e in 'hello world'])


def dict_example():
    # some_dict = {'key': 'value', 'key2': 5, 4: 5}
    # print(some_dict)
    # print(list(some_dict.keys()))
    # print(list(some_dict.values()))
    student1 = {'name': 'Игорь', 'surname': 'Горшков',
                'subjects': [], 'marks': []}
    student2 = {'name': 'Иван', 'surname': 'Иванов',
                'subjects': [], 'marks': []}
    students = [student1, student2]
    # print(students)
    # фамилии и имена
    # print([s['surname'] for s in students])
    # print([s['name'] for s in students])
    # назначаем предметы
    all_subjects = ['математика', 'физика', 'химия', 'ОБЖ',
                    'литература', 'история', 'физкультура',
                    'география']
    for i, _ in enumerate(students):
        random.shuffle(all_subjects)
        students[i]['subjects'] =\
            random.sample(all_subjects, 5)
        students[i]['marks'] = [random.randint(3,5) for _ in range(5)]
    print_students(students)


def print_students(students):
    name_shift = max([len(s['name'] + s['surname'])
                           for s in students])
    name_shift += 3  # spaces
    subj_shift = max([max([len(sb) for sb in s['subjects']])
                           for s in students])
    print(students)
    for s in students:
        name, surname, subjects, marks = s.values()
        print((surname+' '+name).ljust(name_shift), end='')
        for i, m in enumerate(marks):
            if i > 0:
                print(' '*name_shift, end='')
            print(subjects[i].ljust(subj_shift), m)

    with open('students.json', 'w') as f:
        json.dump(students, f, indent=2,
                  separators=(',', ':'),
                  ensure_ascii=False)


if __name__ == '__main__':
    dict_example()
