# 13. Подсчитайте количество элементов в словаре.
# 14. Проверьте, пуст ли словарь.
# 15. Найдите минимальный и максимальный ключ в словаре.
# num_dict = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five'
# }
# max_key = float('-inf')
# min_key = float('inf')
# for key, val in num_dict.items():
#      if type(key) == int and max_key < key:
#         max_key = key
#      if type(key) == int and min_key > key:
#         min_key = key
# print(max_key, min_key)

# 16. Найдите минимальное и максимальное значение в словаре.
# num_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5
# }
# max_val = float('-inf')
# min_val = float('inf')
# for key, val in num_dict.items():
#     if type(val) == int and val > max_val:
#         max_val = val
#     if type(val) == int and val < min_val:
#         min_val = val
# print(min_val, max_val)

# 17. Найдите сумму всех значений в словаре (если значения числовые).
# num_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5
# }
# summa = 0
# for key, val in num_dict.items():
#     if type(val) == int:
#         summa += val
# print(summa)

# 18. Поменяйте местами ключи и значения в словаре.
# num_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5
# }
# new_dict = {}
# for key, val in num_dict.items():
#     new_dict[val] = key
# print(new_dict)

# 19. Создайте словарь, в котором значения являются списками.
# 20. Обновите значение в списке, который является значением в словаре.
# my_dict = {
#     'ключ1': [1, 2, 3],
#     'ключ2': ['a', 'b', 'c'],
#     'ключ3': [True, False, True]
# }
# for key, val in my_dict.items():
#     my_dict['ключ2'][1] = 40
# print(my_dict)

# 21. Найдите ключ, соответствующий максимальному значению в словаре.
# 22. Найдите ключ, соответствующий минимальному значению в словаре.
# my_dict = {
#     'ключ1': [1, 2, 3],
#     'ключ2': [4, 5, 6],
#     'ключ3': [7, 8, 9]
# }
# min_val = float('inf')
# max_val = float('-inf')
#
# for key, val in my_dict.items():
#     for elem in val:
#         if isinstance(elem, int):  # Проверяем, является ли элемент целым числом
#             if elem > max_val:
#                 max_val = elem
#             if elem < min_val:
#                 min_val = elem
#
# print(min_val, max_val)

# 22. Найдите ключ, соответствующий минимальному значению в словаре.
# my_dict = {
#     18: [1, 2, 3],
#     28: [4, 5, 6],
#     'ключ3': [7, 8, 9]
# }
# min_key = float('inf')
# for key, val in my_dict.items():
#     if isinstance(key, int):
#         if key < min_key:
#             min_key = key
# print(min_key)

# 23. Удалите все элементы с определенным значением.
# my_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5
# }
# def del_some_value(some_dict: dict, value_delete):
#     for key, val in some_dict.items():
#         if val == value_delete:
#             del [val]
#     return some_dict
# print(del_some_value(my_dict, value_delete=3))
# print(del_some_value(my_dict, value_delete=15))

# 24. Отсортируйте элементы словаря по ключам.
# 25. Отсортируйте элементы словаря по значениям.
# my_dict = {
#     'b': 2,
#     'a': 1,
#     'd': 4,
#     'c': 3
# }
# my_dict = sorted(my_dict, key=lambda elem: elem[0])
# print(my_dict)
# my_dict = sorted(my_dict.items(), key=lambda elem: elem[1])
# print(my_dict)

# 26. Объедините два словаря, обновив значения с общими ключами.
# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5
# }
#
# dict2 = {
#     'c': 6,
#     'd': 7,
#     'f': 8,
#     'g': 9,
#     'h': 10
# }
'''метод update не возращает новый словарь, надо исходный словарь скопировать, а потом обновить и распечатать'''
import datetime
# dict1_new = dict1.copy()
# dict1_new.update(dict2)
# print(dict1_new)

# 27. Создайте словарь, используя генератор словаря.
import random
"""sample дает случайное число ключей из диапазона random.sample(range(1, 11), вот тут random.randint(0, 11))"""
# my_dict = {key: val for key in random.sample(range(1, 11), random.randint(0, 11)) for val in range(random.randint(0, 11))}
# print(my_dict)
''' random.sample(range(1, 11), 5) вот тут 5 это количество ключей'''
# my_dict = {key: val for key in random.sample(range(1, 11), 5) for val in range(random.randint(0, 11))}
# print(my_dict)

# 28. Посчитайте, сколько раз каждый элемент встречается в списке и создайте словарь.
# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# counter = 0
# my_dict = {}
# for elem in my_list:
#     if elem not in my_dict:
#         my_dict[elem] = 1
#     else:
#         my_dict[elem] += 1
# print(my_dict)

# 29. Найдите наиболее часто встречающийся элемент в словаре.
# my_dict = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}
# max_count = max(my_dict.values())
# most_common_elements = [key for key, val in my_dict.items() if val == max_count]
# print("Наиболее часто встречающиеся элементы:", most_common_elements)

# 30. Удалите элемент с наименьшим значением в словаре.
# my_dict = {1: 2, 2: 2, 3: 2, 4: 2, 5: 12}
# min_val = min(my_dict.values())
# my_dict_new = {key: val for key, val in my_dict.items() if val != min_val}
# print(my_dict_new)


# 31. Создайте словарь, в котором значения являются словарями.
# 32. Получите значение из вложенного словаря по нескольким ключам.
# my_dict = {
#     'dict1': {'a': 1, 'b': 2, 'c': 3},
#     'dict2': {'x': 10, 'y': 20, 'z': 30},
#     'dict3': {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
# }
# list_out = []
# for key, val in my_dict.items():
#     if 'apple' in val:
#         list_out.append(val['apple'])
# print(list_out)

# 33. Создайте словарь, содержащий информацию о студентах (имя, возраст, оценки и т. д.).
# 34. Найдите средний возраст студентов в словаре из предыдущей задачи.
# 35. Удалите студента из словаря на основе его имени.
# 36. Обновите оценку студента в словаре.
# students = {
#     'student1': {
#         'name': 'Иванов Иван',
#         'age': 20,
#         'grades': [4, 5, 3, 4]
#     },
#     'student2': {
#         'name': 'Петров Петр',
#         'age': 19,
#         'grades': [5, 5, 4, 5]
#     },
#     'student3': {
#         'name': 'Сидоров Сидор',
#         'age': 21,
#         'grades': [3, 4, 3, 3]
#     }
# }
# def aver_age_students(some_dict: dict):
#     list_age = []
#
#     summa = 0
#     for student, val in some_dict.items():
#         age = val['age']
#         grade = val['grades']
#         name_student = val['name']
#         list_age.append(age)
#     for elem in list_age:
#         summa += elem
#         aver_age = summa / len(list_age)
#
#     return (f'средний возраст студентов {aver_age}')
# print(aver_age_students(students))

# def del_student(some_dict: dict, st_name):
#     new_dict = {}
#     for student, val in some_dict.items():
#         name_student = val['name']
#         if name_student != st_name:
#             new_dict[student] = val
#     return new_dict
# print(del_student(students, st_name='Сидоров Сидор'))

# 37. Создайте словарь, содержащий информацию о книгах (название, автор, год выпуска и т. д.).
# 38. Найдите книгу с наибольшим годом выпуска.
# books = {
#     'book1': {'title': 'Война и мир', 'author': 'Лев Толстой', 'year': 1869},
#     'book2': {'title': 'Преступление и наказание', 'author': 'Федор Достоевский', 'year': 1866},
#     'book3': {'title': '1984', 'author': 'Джордж Оруэлл', 'year': 1949},
#     'book4': {'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': 1967}
# }
# import  datetime
# def find_oldest_book(my_dict: dict):
#     now = datetime.datetime.now().year
#     oldest_book = None
#     max_age = float('-inf')
#     for book, val in my_dict.items():
#         year = val['year']
#         title = val['title']
#         author = val['author']
#         age_book = now - year
#         if age_book > max_age:
#             max_age = age_book
#             oldest_book = title
#     return max_age, oldest_book
#
# print(find_oldest_book(books))

# # 39. Создайте словарь, содержащий информацию о городах (название, население, регион и т. д.).
# # 40. Найдите город с наибольшим населением.
# cities = {
#     'city1': {'name': 'Нью-Йорк', 'population': 8500000, 'region': 'Нью-Йорк'},
#     'city2': {'name': 'Лос-Анджелес', 'population': 4000000, 'region': 'Калифорния'},
#     'city3': {'name': 'Чикаго', 'population': 2700000, 'region': 'Иллинойс'},
#     'city4': {'name': 'Майами', 'population': 470000, 'region': 'Флорида'},
#     'city5': {'name': 'Хьюстон', 'population': 2300000, 'region': 'Техас'}
# }
# def find_biggest_city(some_dict: dict) -> int:
#     biggest_population = float('-inf')
#     city = None
#     for city, val in some_dict.items():
#         name_city = val['name']
#         population = val['population']
#         region = val['region']
#         if population > biggest_population:
#             biggest_population = population
#             city = name_city
#     return {biggest_population}, {city}, {name_city}
# print(find_biggest_city(cities))

