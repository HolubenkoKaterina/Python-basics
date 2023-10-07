# Отсортировать список кортежей по второму элементу.
# my_list = [(1, 'apple'), (4, 'date'), (2, 'banana'), (3, 'cherry')]
# resalt = sorted(my_list, key=lambda x: x[1])
# print(resalt)

# Отсортировать список списков по длине подсписков.
# my_list = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9],
#     [10]
# ]
# resalt = sorted(my_list, key=lambda elem: len(elem))
# print(resalt)

# Отсортировать список чисел по их абсолютным значениям.
# my_list = [7, -3, 5, -1, 0, -2, 9, -4]
# resalt = sorted(my_list, key=lambda elem: abs(elem), reverse=True)
# print(resalt)

# Отсортировать список строк в обратном алфавитном порядке.
# my_list = ["apple", "banana", "cherry", "apple", "date"]
# resalt = sorted(my_list, key=lambda elem: elem, reverse=True)
# print(resalt)

# Отсортировать список словарей по значениям ключа 'age'.
# my_list = [
#     {'name': 'John Doe', 'age': 38, 'city': 'New York'},
#     {'name': 'Jane Smith', 'age': 25, 'city': 'Los Angeles'},
#     {'name': 'Bob Johnson', 'age': 35, 'city': 'Chicago'}
# ]
# def sorted_key(some_list: list):
#     resalt = sorted(some_list, key=lambda x: x['age'])
#     return resalt
# res = sorted_key(my_list)
# print(res)

# Отсортировать список дат (строки формата 'ГГГГ-ММ-ДД') по возрастанию.
# date_list = [
#     '2022-10-15',
#     '2022-09-28',
#     '2022-11-03',
#     '2022-08-07',
#     '2022-12-25'
# ]
# resalt = sorted(date_list, key=lambda x: x, reverse=False)
# print(resalt)

# Отсортировать список дат в обратном порядке.
# date_list = [
#     '2022-10-15',
#     '2022-09-28',
#     '2022-11-03',
#     '2022-08-07',
#     '2022-12-25'
# ]
# resalt = sorted(date_list, key=lambda x: x, reverse=True)
# print(resalt)

# Отсортировать список чисел сначала по четности, затем по возрастанию.
# import random
# list_number = [elem for elem in range(random.randint(1, 101))]
# resalt = sorted(list_number, key=lambda x: x % 2 == 0, reverse=True)
# print(resalt)

# Отсортировать список строк по количеству гласных букв в них.
# my_list = ["apple", "banana", "cherryyy",  "dat"]
# vowes = 'aeouiy'
#
# listik = []
# for elem in my_list:
#     counter = 0
#     for char in elem:
#         if char in vowes:
#             counter += 1
#     listik.append(counter)
# resalt = sorted(listik, key=lambda x: x)
# print(resalt)

# Отсортировать список кортежей сначала по первому элементу, затем по второму.
# my_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (12, 'bananas')]
# resalt = sorted(my_tuples, key=lambda elem: elem[0])
# print(resalt)
