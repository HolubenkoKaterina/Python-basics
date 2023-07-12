# 1. Напишите программу, которая добавляет элемент в конец кортежа.
'''def element_in_tuple(kortez:tuple, add_el: str):
    kortez_new = kortez + (add_el,)
    return kortez_new
elem_add = input('введите ваш элемент..')
kort = ('5', 45, 'python', 100, 'we can')
print(element_in_tuple(kort, elem_add))'''
# 2. Напишите программу, которая удаляет определенный элемент из кортежа.
'''def del_element_in_tuple(kortez:tuple, del_elem:str):
    kortez_new = list(kortez)
    if del_elem in kortez_new:
        print('есть такой элемент..')
        kortez_new.remove(del_elem)
        kortez_new = tuple(kortez_new)
    else:
        print("такого элемента нет..")
    return kortez_new
elem_del = input('введите ваш элемент..')
kort = ('5', 45, 'python', 100, 'we can')
print(del_element_in_tuple(kort, elem_del))
'''
# 4. Напишите программу, которая находит пересечение двух множеств и возвращает список с общими элементами.
'''def intersection_to_list(set1:set, set2:set):
    itog = set1.intersection(set2)
    itog_list = list(itog)

    return itog_list
set1 = {'one', 1, 'two', 22, 33 , 10}
set2 = {'one', 12, 'two', 22 }
resalt = intersection_to_list(set1,set2)
print(f'общие элементы из множества {set1} и множества {set2} будет такой: {resalt}' )
'''
# 5. Напишите программу, которая находит объединение двух множеств и возвращает список всех уникальных элементов.
'''def union_sets(set1: set, set2:set ):
    itog = list()
    itog = set1.union(set2)
    return itog

set1 = {'one', 1, 'two', 22, 33 , 10}
set2 = {'one', 12, 'two', 22 }
resalt = union_sets(set1, set2)
print(f' результат обьединения множества {set1} и множества {set2} \n будет вот такой результат: {resalt}')'''
# 6. Напишите программу, которая находит разность двух множеств и возвращает список элементов, которые присутствуют
# только в одном из множеств.
'''def difference_sets_in_list(set1: set, set2: set):
    if len(set1) > len(set2):
        itog = list(set1 - set2)
        print(f'{set1} содержит больше элементов, чем {set2}')
    else:
        itog = list(set2 - set1)
        print(f'{set2} содержит больше элементов, чем {set1}')

    return itog

set1 = {'one', 1, 'two', 22, 33 , 10}
set2 = {'one', 12, 'two', 22, '100', 150, 250}
resalt = difference_sets_in_list(set1, set2)
print(resalt)
'''
# 1. Напишите программу, которая объединяет два кортежа, добавляя элементы из второго кортежа в конец первого.
'''def unit_tuple(kor1:tuple, kor2:tuple):
    itog = kor1+kor2
    return itog
kort1 = ('one', 'two', 'three')
kort2 = (1, 2, 3,)
resalt = unit_tuple(kort1,kort2)
print(f'а вот что мы получим при обьединении кортежа\n {kort1}  и {kort2} : {resalt}')'''
# 2. Напишите программу, которая удаляет повторяющиеся элементы из кортежа.
'''kortez = ('one', 'two', 'three', 'one', 'two', 'three' )
def delete_repetitive_elements(some_kortez:tuple):
    some_kortez_to_list = list(some_kortez)
    some_kortez_to_list = set(some_kortez_to_list)
    return tuple(some_kortez_to_list)
resalt = delete_repetitive_elements(kortez)
print(resalt)
'''
'''# 3. Напишите программу, которая разделяет кортеж на два, на основе определенного элемента.
tuple_in = ('one', 'two', 'l', 'four', '55', '150')
word = input('введите элемент по которому мы разделим наш кортеж..')
def change_tuple_to_list(some_tuple:tuple):
    some_tuple_to_list = list(some_tuple)
    return some_tuple_to_list
resalt_tuple_list = change_tuple_to_list(tuple_in)
print(resalt_tuple_list)
def split_tuple_on_some_word(result_tuple_list, word):
    tuple_out_1 = []
    tuple_out_2 = []
    flag = False
    for element in result_tuple_list:
        if element == word:
            flag = True
        if not flag:
            tuple_out_1.append(element)
        else:
            tuple_out_2.append(element)
    return tuple_out_1, tuple_out_2

split_result = split_tuple_on_some_word(tuple_in, word)
print(f"Слово '{word}': первый список {split_result[0]}, второй список {split_result[1]}")'''
# 4. Напишите программу, которая проверяет, является ли список подмножеством множества.
'''some_set = {'mimi', 'kiki', 'lili', 'fifi', '1', '2', '3'}
subset = {'1', '2', '3'}
def check_subset_in_some_set(some_set:set, subset:set):
     return subset.issubset(some_set)

resalt_check_subset_in_some_set = check_subset_in_some_set(some_set,subset)
print(resalt_check_subset_in_some_set)
'''
# 5. Напишите программу, которая добавляет элемент в список только в том случае, если его нет в множестве.
'''some_list = ['mimi', 'kiki', 'lili', 'fifi', '1', '2', '3', 'fifi', 'fifi', 5]
some_set = {'1', '2'}

def change_some_set_to_list(some_set):
    some_new_list = list(some_set)
    return some_new_list

resalt_change_some_set_to_list = change_some_set_to_list(some_set)
print(resalt_change_some_set_to_list)

def add_new_element_to_some_list(some_list, some_set):
    list_out = some_list.copy()

    while True:
        what_append = input('Введите элемент, который хотите добавить: ')
        if what_append not in some_set:
            list_out.append(what_append)
        else:
            print('Такой элемент уже существует во множестве.')

        question = input('Будем еще что-то добавлять? (y/n): ').lower()
        if question == 'n':
            break

    return list_out

resalt_list_out = add_new_element_to_some_list(some_list, some_set)
print(resalt_list_out)'''
'''def change_type_list_in_set(some_list):
    some_set = set(some_list)
    return some_set

def check_element_in_spisok_and_set(some_list, some_set):
    resalt_some_set = change_type_list_in_set(some_list)
    return resalt_some_set.issubset(resalt_some_set)

resalt_check = check_element_in_spisok_and_set(some_list, some_set)
print(resalt_check)
'''
# 6. Напишите программу, которая удаляет все элементы из списка, которые также присутствуют в множестве.
'''some_list = ['mimi', 'kiki', 'lili', 'fifi', '1', '2', '3', 'fifi', 'fifi', 5, '1', '2']
some_set = {'1', '2'}
def change_type_set_to_list(some_set: set):
    new_list = list(some_set)
    return new_list
new_list = change_type_set_to_list(some_set)
print(new_list)

def check_element_in_some_list(some_list: list, some_set: set):
    some_list_out = some_list.copy()
    some_set = new_list
    for element in some_list:
        if element in new_list:
            some_list_out.remove(element)
    return some_list_out
resalt_spisok = check_element_in_some_list(some_list, some_set)
print(f' вот новый список без элементов из множества {some_set}\n {resalt_spisok}')
'''
# 1. Напишите программу, которая меняет порядок элементов в кортеже на обратный.
'''def change_type_tuple_to_list(some_tuple:tuple):
    some_tuple_to_list = list(some_tuple)
    return some_tuple_to_list
tuple_input = ('one', 'two', 'three', 1, 2, 3, 55, 'one', 'two', 'three')
resalt_transform_tuple_to_list = change_type_tuple_to_list(tuple_input)
#print(resalt_transform_tuple_to_list)
def reverse_some_tuple(some_tuple:tuple):
    some_tuple = resalt_transform_tuple_to_list
    some_tuple.reverse()
    return tuple(some_tuple)
tuple_input = ('one', 'two', 'three', 1, 2, 3, 55, 'one', 'two', 'three')

print(reverse_some_tuple(tuple_input))'''
# 2. Напишите программу, которая удаляет все элементы из кортежа.
'''def change_type_tuple_to_list(some_tuple:tuple):
    some_tuple_to_list = list(some_tuple)
    return some_tuple_to_list
tuple_input = ('one', 'two', 'three', 1, 2, 3, 55, 'one', 'two', 'three')
resalt_transform_tuple_to_list = change_type_tuple_to_list(tuple_input)
print(resalt_transform_tuple_to_list)

def delete_elements_in_tuple(some_tuple:tuple):
    some_tuple.clear()
    return tuple(some_tuple)
resalt_clear_typle = delete_elements_in_tuple(resalt_transform_tuple_to_list)
print(resalt_clear_typle)
'''
# 3. Напишите программу, которая удаляет первое вхождение определенного элемента из кортежа
'''def change_type_tuple_to_list(some_tuple):
    some_tuple_to_list = list(some_tuple)
    return some_tuple_to_list
tuple_input = ('one', 'two', 'three', 1, 2, 3, 55, 'one', 'two', 'three')
resalt_transform_tuple_to_list = change_type_tuple_to_list(tuple_input)
print(resalt_transform_tuple_to_list)
delete_element = input('что надо удалить ')

def check_element_to_delete(some_list:list, elem_to_check:str):
    for elements in some_list:
        if elem_to_check == elements:
            return True
    return False
resalt_to_check = check_element_to_delete(resalt_transform_tuple_to_list, delete_element)
print(check_element_to_delete(resalt_transform_tuple_to_list, delete_element ))

def del_first_entry_in_tuple(some_tuple:tuple, delete_element: str):
    some_tuple_new = list(some_tuple)
    if resalt_to_check:

        for element in some_tuple_new:
            if element == delete_element:
                some_tuple_new.remove(delete_element)
                break
    return tuple(some_tuple_new)
print(del_first_entry_in_tuple(tuple_input, delete_element))'''
# 4. Напишите программу, которая находит количество общих элементов в списке и множестве.
'''some_list = ['one', 144, 'three', 11, 12, 13, 55, 'one']
some_set = {'one', 'two', 'three', 1, 2, 3, 55, 'one', 'two', 'three', 'fifty five'}
print(some_set)
print(some_list)
def count_common_elements(some_list:list, some_set:str):
    count = 0
    for element in some_list:
        for elem in some_set:
            if element == elem:
                count += 1
    return count
resalt = count_common_elements(some_list, some_set)
print(f'{resalt} это количество общих элементов \n в списке {some_list} и множестве {some_set}')
'''
# 5. Напишите программу, которая удаляет все повторяющиеся элементы из списка, сохраняя только уникальные элементы.
'''def uniq_element_in_list(some_list:list):
    some_list_to_uniq = set(some_list)
    some_list_set_return_list = list(some_list_to_uniq)
    return some_list_set_return_list
list_interesting = ['one', 'two', 'three', 'one', 'two', 'three','one', 'two', 'three', 1, 2, 3, 1, 1]
resalt = uniq_element_in_list(list_interesting)
print(resalt)'''
# 6. Напишите программу, которая находит симметрическую разность двух множеств и возвращает список элементов,
# которые присутствуют только в одном из множеств.
'''some_set1 = {1, 5, 10, 'dog', 'cat', 'friends', 'friends forever'}
some_set2 = {5, 10, 'dog', 'cat', 'not friends', 'we like python'}
def find_simmetric_difference(some_set1:set, some_set2:set):
    some_set1.difference_update(some_set2)
    return some_set1
print(find_simmetric_difference(some_set1,some_set2))'''
# Удалите элемент "banana" из множества.
'''some_set = {"apple", "banana", "cherry", "orange"}
print(some_set)
def change_type_set_to_list(some_set:set):
    some_list = list(some_set)
    return some_list
resalt_list = change_type_set_to_list(some_set)
print(resalt_list)

def delete_element_in_set(some_set):
    some_set = resalt_list


    while True:
        what_delete = input('что хотите удалить? ')
        if what_delete in resalt_list:
            resalt_list.remove(what_delete)
            print(f'элемент {what_delete} удален')
        else:
            print('а такого элемента в списке нет..')
        question = input('продолжаем или нет? (y/n) ').lower()
        if question != 'y':
            break


    return set(resalt_list)
some_set_out = delete_element_in_set(some_set)
print(some_set_out)'''
# Создайте множество, содержащее элементы "apple", "banana" и "cherry".Добавьте элемент "orange" в множество.
'''some_set = {'kiwi', 'apple', 'milk', 'milki way'}
def change_type_set_to_list(some_set:set):
    some_list = list(some_set)
    return some_list
some_list = change_type_set_to_list(some_set)
print(some_list)

def append_element_to_set(some_set: set):
    some_set = some_list


    while True:
        for element in some_list:
            word = input('что добавим? ')
            some_list.append(word)
            question = input('добавлять еще будем? (y/n)').lower()
            if question == 'y':
                continue
            else:
                break
        return set(some_list)
print(append_element_to_set(some_set))'''
# 6. Напишите программу, которая находит элементы, которые встречаются более одного раза в списке, и добавляет их в множество.
'''some_list = ['one', 'one', 'two', '1', '1', 2, 5, '5', 'two']
def add_element_to_set(some_list: list):
    set_out = set()
    counter = 0
    for element in some_list:
        counter = some_list.count(element)
        if counter > 1:
            set_out.add(element)
    return set_out
set_out = add_element_to_set(some_list)
print(set_out)'''
# Создайте два множества с элементами "apple", "banana", "cherry" и "orange". Вычислите и выведите их пересечение.
'''some_set1 = {"apple", "banana", "cherry", "orange"}
some_set2 = {"apple", "banana", "pivo", "coffee"}
def intersection_for_two_sets(some_set1: set, some_set2: set):
    set_intersection = some_set1.intersection(some_set2)
    return set(set_intersection)
set_intersection = intersection_for_two_sets(some_set1,some_set2)
print(set_intersection)'''
# 1. Напишите программу, которая заменяет все вхождения определенного элемента в кортеже другим элементом.
'''some_tuple = ('one', 'two', 'one', '55', 100, 'two')
def replace_element_in_tuple(some_tuple):
    some_list = list(some_tuple)

    while True:
        what_replace = input('Что нужно заменить? ')
        replace_out = input('На что нужно заменить? ')

        flag = False
        for index in range(len(some_list)):
            if what_replace == some_list[index]:
                some_list[index] = replace_out
                flag = True

        if not  flag:
            print('Такого элемента нет в списке.')

        question = input('Продолжаем замену? (y/n): ').lower()
        if question != 'y':
            break

    new_tuple = tuple(some_list)
    return new_tuple

resalt = replace_element_in_tuple(some_tuple)
print(resalt)
'''
#Создайте список списков, где каждый внутренний список содержит числа от 1 до 5.
# Затем отсортируйте каждый внутренний список по возрастанию.
'''spisok = [[1, 3, 4, 2, 5], [5, 4, 3, 2, 1], [5, 3, 2, 1, 4]]
def sotred_list(spisok:list):
    for element in spisok:
        for i in range(len(element) - 1):
            for j in range(len(element) -i - 1):
                if element[j] > element[j +1]:
                    element[j], element[j +1] = element[j+1], element[j]
    return spisok
itog = sotred_list(spisok)
print(itog)'''
#  Внешний словарь должен содержать ключи "name", "age" и "grades". Внутренний словарь (grades) должен содержать предметы
#  в качестве ключей и оценки в качестве значений.
# Создайте список вложенных словарей, представляющих собой информацию о студентах.
# Каждый словарь должен содержать ключи "name", "age" и "grades" (см. предыдущее задание).
# Создайте функцию, которая принимает этот список и возвращает среднюю оценку каждого студента.
'''students = {
    'student1': {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 90, "english": 85, "history": 92}
    },
    'student2': {
        "name": "Bob",
        "age": 19,
        "grades": {"math": 78, "english": 92, "history": 88}
    },
    'student3': {
        "name": "Carol",
        "age": 21,
        "grades": {"math": 95, "english": 87, "history": 84, 'python': 100}
    }
}
def aver_marks_from_students(students:dict):
    sum_grades = 0
    list_out = []
    for key, value in students.items():
        names = value['name']
        grades = value['grades']
        average_mark = round(sum(grades.values()) / len(grades))
        list_out.append((names, average_mark))
    return list_out
itog_aver_marks = aver_marks_from_students(students)
print(itog_aver_marks)

def print_student_apper_some_marks(students:dict):
    students = itog_aver_marks
    list_marks = []
    what_aver_marks = int(input('введите оценку '))
    for element in itog_aver_marks:
        if what_aver_marks <= element[1]:
            list_marks.append(element)
    return list_marks
itogi = print_student_apper_some_marks(students)
print(f' вот список студентов и их оценки, у которых балл выше чем заданный \n {itogi}')
'''
# Создайте список словарей, где каждый словарь представляет собой информацию о студенте
# (ключи: "name", "age", "grade"). Затем отсортируйте список словарей по возрастанию значения ключа "age".
'''students = {
    'student1': {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 90, "english": 85, "history": 92}
    },
    'student2': {
        "name": "Bob",
        "age": 19,
        "grades": {"math": 78, "english": 92, "history": 88}
    },
    'student3': {
        "name": "Carol",
        "age": 21,
        "grades": {"math": 95, "english": 87, "history": 84, 'python': 100}
    }
}
def get_age_students(students:dict):
    list_age = []
    for key, value in students.items():
        name = value['name']
        age = value['age']

        list_age.append((name, age))
    return list_age
age_list = get_age_students(students)


def sort_age_student(students:dict):
    students = age_list
    len_spisok = len(age_list)
    for element in age_list:
        for i in range(len_spisok - 1):
            for j in range(len_spisok - i - 1):
                if age_list[j][1] > students[j + 1][1]:
                    age_list[j], age_list[j + 1] = age_list[j + 1], age_list[j]
    return age_list
itog = sort_age_student(students)
print(f'вот отсортированный список студентов по возрасту \n {itog}')# тут я чуть не чокнулась

'''