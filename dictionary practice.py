# Создайте вложенный словарь, представляющий собой информацию о студентах.
# Внешние ключи - идентификаторы студентов, а внутренние ключи - "name", "age", "grade".
# Затем выведите имена всех студентов, чей возраст меньше 20 лет.
# students = {
#     'student1': {
#         "name": "Alice",
#         "age": 20,
#         "grades": {"math": 90, "english": 85, "history": 92}
#     },
#     'student2': {
#         "name": "Bob",
#         "age": 19,
#         "grades": {"math": 78, "english": 92, "history": 88}
#     },
#     'student3': {
#         "name": "Carol",
#         "age": 21,
#         "grades": {"math": 95, "english": 87, "history": 84, 'python': 100}
#     }
# }
# def get_students_below_age(students_data, age_limit):
#     for key, value in students.items():
#         if value['age'] < age_limit:
#             print(value['name'])
#
#
# age_input = int(input('Введите возраст: '))
# get_students_below_age(students, age_input)
#
# Создайте функцию, которая принимает список словарей (представляющих собой информацию о фруктах)
# и возвращает новый список, содержащий только фрукты определенного цвета (например, "red").
# fruits = [
#     {'name': 'apple', 'color': 'red', 'taste': 'sweet'},
#     {'name': 'banana', 'color': 'yellow', 'taste': 'sweet'},
#     {'name': 'grape', 'color': 'purple', 'taste': 'sweet'},
#     {'name': 'orange', 'color': 'orange', 'taste': 'citrus'},
#     {'name': 'strawberry', 'color': 'red', 'taste': 'sweet'},
# ]
# def get_product_color(some_list: list):
#     list_out = []
#     what_color = input('введите цвет который вас интересует..')
#     for element in some_list:
#         name = element.get('name')
#         color = element.get('color')
#         taste = element.get('taste')
#         if what_color == color:
#             list_out.append((name, taste))
#     return list_out
# resalt = get_product_color(fruits)
# print(resalt)
#
# Создайте вложенный словарь, представляющий собой информацию о студенте.
# 1. Напишите программу, которая находит студентов с наибольшим и наименьшим возрастом в каждом классе
# и выводит результат в виде словаря.
# 2. Напишите программу, которая находит студента с наибольшим именем по длине в списке.
# students = [
#     {"имя": "Alice", "возраст": 15, "класс": "9A"},
#     {"имя": "Bob", "возраст": 13, "класс": "9A"},
#     {"имя": "Charlie", "возраст": 14, "класс": "9B"},
#     {"имя": "David", "возраст": 16, "класс": "9B"},
# ]
#
#
# def get_info_students(students: list):
#     max_age = {}
#     min_age = {}
#     max_length_name = {}
#     min_length_name = {}
#
#     for info in students:
#         name = info["имя"]
#         age = info["возраст"]
#         clas = info["класс"]
#
#         if clas not in max_age:
#             max_age[clas] = age
#             min_age[clas] = age
#             max_length_name[clas] = name
#             min_length_name[clas] = name
#         else:
#             max_age[clas] = max(max_age[clas], age)
#             min_age[clas] = min(min_age[clas], age)
#
#             if len(name) > len(max_length_name[clas]):
#                 max_length_name[clas] = name
#
#             if len(name) < len(min_length_name[clas]):
#                 min_length_name[clas] = name
#
#     return max_age, min_age, max_length_name, min_length_name
#
# max_age_dict, min_age_dict, max_length_name, min_length_name = get_info_students(students)
# print("Maximum ages in each class:", max_age_dict)
# print("Minimum ages in each class:", min_age_dict)
# print("Maximum length name in each class:", max_length_name)
# print("Minimum length name in each class:", min_length_name)
