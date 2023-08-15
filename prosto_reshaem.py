# Дан словарь с информацией о студентах и их предметах. Каждый студент представлен вложенным словарем с ключами
# "имя" и "предметы", где предметы являются вложенным словарем с ключами "название" и "оценка". Найдите студента с
# наибольшим средним баллом по предметам.
# students = [
#     {
#         'name': 'Иванова',
#         'item': {
#             'математика': 58,
#             'английский': 95
#         }
#     },
#     {
#         'name': 'Петров',
#         'item': {
#             'математика': 75,
#             'python': 100
#         }
#     },
#     {
#         'name': 'Сидоренко',
#         'item': {
#             'математика': 80,
#             'python': 87,
#             'английский': 90
#         }
#     }
# ]
# def find_student_with_highest_average(students):
#     highest_average = 0
#     student_with_highest_average = None
#     for student in students:
#         name = student['name']
#         items = student['item']
#         total_score = sum(items.values())
#         average_score = total_score / len(items)
#         if average_score > highest_average:
#             highest_average = average_score
#             student_with_highest_average = name
#     return student_with_highest_average
# highest_average_student = find_student_with_highest_average(students)
# print(highest_average_student)

# Дан словарь с информацией о покупках пользователей. Каждая покупка представлена вложенным словарем с ключами
# "пользователь", "продукт" и "количество". Посчитайте общее количество продуктов, купленных каждым пользователем.
# purchases = [
#     {"пользователь": "John", "продукт": "Яблоко", "количество": 3},
#     {"пользователь": "Alice", "продукт": "Апельсин", "количество": 2},
#     {"пользователь": "Bob", "продукт": "Банан", "количество": 1},
#     {"пользователь": "Alice", "продукт": "Груша", "количество": 4},
#     {"пользователь": "John", "продукт": "Мандарин", "количество": 2},
# ]
# def count_purchases(purchases: list, user: str):
#     dict_out = {}
#
#     for elements in purchases:
#         name = elements["пользователь"]
#         purchase = elements["продукт"]
#         counts = elements["количество"]
#         if name in dict_out:
#             dict_out[name] += counts
#         else:
#             dict_out[name] = counts
#     return dict_out
# resalt = count_purchases(purchases, 'Alice')
# print(resalt)

# Дан словарь с информацией о путешествиях. Каждое путешествие представлено вложенным словарем с ключами
# "название", "страна" и "бюджет". Отсортируйте путешествия по возрастанию бюджета.
# travelling = [
#     {'country': 'Turkey', 'budget': 100000, 'time_days': '10'},
# {'country': 'Tailand', 'budget': 100000, 'time_days': '8'},
# {'country': 'Dubai', 'budget': 180000, 'time_days': '10'},
# {'country': 'Egypt', 'budget': 110000, 'time_days': '12'},
# ]
# def get_value_by_key(travelling:list):
#     dict_out = {}
#     for tur in travelling:
#         country_name = tur['country']
#         budget_travel = tur['budget']
#         time_tur = tur['time_days']
#         budget_travel = int(budget_travel)
#         dict_out[country_name] = budget_travel
#     return country_name, budget_travel
#
# dict_out = get_value_by_key(travelling)
# print(dict_out)

# Проверьте, является ли множество подмножеством всех других множеств.
# a = {1, 2}
# b = {1, 2, 3}
# c = {1, 2, 3, 4}
# is_subset_of_all = all(a.issubset(s) for s in [b, c])
# print(is_subset_of_all)

# Проверьте, является ли множество подмножеством каждого множества в списке множеств.
# sets = [{1, 2}, {1, 2, 3}, {1, 2, 3, 4}]
# set1 = {1, 2}

# Напишите программу, которая суммирует элементы кортежа, игнорируя элементы с нечетными индексами.
# kort = ('dog', '35', '25' , 35, 30, 5)
# def summa_element(kortez:tuple):
#     summa = 0
#     for index, element in enumerate(kortez):
#         if index % 2 != 0 and type(element) == int:
#             summa += element
#     return summa
# print(summa_element(kort))

# Напишите программу, которая находит произведение элементов кортежа, находящихся на четных индексах.
# kort = (5 ,'5', '10', 5, '44', 'kik')
# def multiplace_element(kortez: tuple):
#     mult = 1
#     for index, element in enumerate(kortez):
#         if type(element) == int and index % 2 == 0:
#             mult *= element
#     return mult
# print(multiplace_element(kort))

# Найдите симметрическую разность нескольких множеств.
# set1 = {1, 2, 3}
# set2 = {5, 6, 7}
# set3 = {2, 3, 5}
# set4 = list([set1, set2, set3])
# def symmetric_difference(sett:list):
#     result = set()
#     for element in sett:
#         result.symmetric_difference_update(element)
#     return result
#
# result_set = symmetric_difference(set4)
# print(result_set)

# Проверьте, содержит ли множество все элементы из нескольких списков.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# list3 = [5, 6, 7, 8]
# list_itogo = list1 + list2 + list3
# set_itogo = {2, 3, 4}
# print(set_itogo.issubset(set(list_itogo)))
# print(set(list_itogo))

# Найдите сумму элементов, присутствующих в нечетном количестве, в нескольких множествах.
# sets = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
# dict_out = {}
# for element in sets:
#     for number in element:
#         if number not in dict_out:
#             dict_out[number] = 1
#         else:
#             dict_out[number] += 1
# print(dict_out)
# summa = 0
# for key, val in dict_out.items():
#     if val % 2 != 0:
#         summa += val
# print(summa)
# пришлось подсматривать немного


