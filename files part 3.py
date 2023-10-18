# # 18. Создать файл, содержащий строки разной длины. Прочитать файл, найти самую длинную строку и вывести ее на экран.
# strings_list = [
#     "Это короткая строка.",
#     "Это средняя строка с более длинным содержанием.",
#     "Это очень длинная строка, которая может содержать много текста и продолжаться далее.",
#     "Короткая строка",
#     "Ещё одна длинная строка для разнообразия.",
#     "Строка средней длины.",
# ]
#
# def write_some_strings(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for string in data:
#                 my_file.write(string + '\n')
#     except FileNotFoundError as ex:
#         raise ex
#
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             max_length = 0
#             max_string = ''
#             for string in my_file:
#                 stripped_string = string.strip()
#                 if len(stripped_string) > max_length:
#                     max_length = len(stripped_string)
#                     max_string = stripped_string
#             return max_string
#     except FileNotFoundError as ex:
#         raise ex
#
# write_some_strings('strings_list.txt', strings_list)
# result = read_file('strings_list.txt')
# print(result)

# 26. Создать файл с данными о задачах и их статусах в формате "название задачи, статус".
# Прочитать файл, вывести все задачи с определенным статусом.
# tasks_data = [
#     "Разработка нового функционала, в работе",
#     "Тестирование приложения, завершена",
#     "Подготовка презентации, не начата",
#     "Оптимизация базы данных, в работе",
#     "Анализ конкурентов, завершена",
#     "Планирование маркетинговой кампании, не начата",
# ]
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(elem + '\n')
#     except FileNotFoundError as ex:
#         raise (ex)
#
#
# def read_file(path, status_check):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             list_task = []
#             for elem in my_file:
#                 content = elem.strip('').split(', ')
#                 name_task = content[0]
#                 status = content[1]
#                 if status == status_check:
#                     list_task.append(name_task)
#             return list_task
#     except FileNotFoundError as ex:
#         print(ex)
# resalt = read_file('tasks_data.txt', status_check='завершена')
# print(resalt)

# 27. Создать программу для составления списка покупок. Реализовать добавление и удаление товаров из списка в файле.
# shopping_list = [
#     {"продукт": "Яблоки", "цена": 10},
#     {"продукт": "Молоко", "цена": 25},
#     {"продукт": "Хлеб", "цена": 15},
#     {"продукт": "Масло", "цена": 30},
#     {"продукт": "Сахар", "цена": 20},
#     {"продукт": "Яйца", "цена": 15},
#     {"продукт": "Мука", "цена": 18},
#     {"продукт": "Помидоры", "цена": 12},
#     {"продукт": "Огурцы", "цена": 10},
#     {"продукт": "Картошка", "цена": 8}
# ]
# import json
# def write_shopping_list(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             json.dump(data, my_file, ensure_ascii=False, indent=4)
#     except FileNotFoundError as ex:
#         print(ex)
# write_shopping_list('shopping_list.json', shopping_list)
#
# def read_file(path):
#     try:
#         with open(path, 'r+', encoding='utf-8') as my_file:
#             content = json.load(my_file)
#             return content
#     except FileNotFoundError as er:
#         print(er)
# resalt = read_file('shopping_list.json')
# print(resalt)
# product_to_add = input('введите ваш продукт ')
# product_price_add = float(input('и его цену '))
# product_input = {"продукт": product_to_add, "цена": product_price_add}  # Формируем словарь
# def add_product_to_shopping_list(path):
#     try:
#         with open(path, 'r+', encoding='utf-8') as my_file:
#             content = json.load(my_file)  # Загружаем текущий список покупок
#             content.append(product_input)  # Добавляем новый продукт к списку
#             my_file.seek(0)  # Перемещаем курсор в начало файла
#             json.dump(content, my_file, ensure_ascii=False, indent=4)
#     except FileNotFoundError as ex:
#         print(ex)
# add_product_to_shopping_list('shopping_list.json')