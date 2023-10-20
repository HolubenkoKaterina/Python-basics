# 13. Создать файл с данными о товарах в формате "название, количество, цена". Прочитать файл, вычислить общую стоимость товаров
# и записать результат в другой файл.
# products_data = [
#     "Яблоки, 10, 50",
#     "Бананы, 20, 30",
#     "Груши, 15, 40",
#     "Апельсины, 25, 35",
# ]
#
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(elem + '\n') #так как передается список а не строка то надо записывать по элементам
#     except FileNotFoundError as er:
#         print(er)
# write_file('products_data.txt', products_data)
#
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             summa = 0
#             content = my_file.readlines()
#             for elem in content:
#                 parts = elem.strip().split(',')
#                 quantity = int(parts[1])
#                 price = int(parts[2])
#                 summa += quantity * price
#             print(summa)
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('products_data.txt', products_data)
# read_file('products_data.txt')

# 23. Создать файл, содержащий данные о предметах в формате "название, вес, цена".
# Прочитать файл, найти предмет с наибольшим отношением цены к весу.
# items_data = [
#     "Книга, 1.5, 500",
#     "Ноутбук, 2.8, 1500",
#     "Флешка, 0.05, 30",
#     "Камера, 0.3, 700",
#     "Мышь, 0.1, 20",
# ]
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(elem + '\n')
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('items_data.txt', items_data)
# def read_file(path):
#     highest_ratio = 0
#     best_item = None
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             content = my_file.readlines()
#             for elem in content:
#                 parts = elem.strip().split(',')
#                 name = parts[0]
#                 weight = float(parts[1])
#                 price = int(parts[2])
#                 ratio = price / weight
#                 if ratio > highest_ratio:
#                     highest_ratio = ratio
#                     best_item = name
#             print(f"The item with the highest price-to-weight ratio is: {best_item}")
#     except FileNotFoundError as ex:
#         print(ex)
#
# read_file('items_data.txt')


# # 31. Создать файл, содержащий данные о покупках пользователей в формате "пользователь, товар, цена".
# # Прочитать файл, вычислить общую сумму покупок каждого пользователя.
# purchases_data = [
#     "Иван, Ноутбук, 1500",
#     "Иван, книга, 1500",
#     "Иван, флешка, 1500",
#     "Иван, Ноутбук, 3500",
#     "Мария, Книга, 500",
#     "Мария, флешка, 700",
#     "Петр, Флешка, 30",
#     "Елена, Камера, 700",
#     "елена, Мышь, 20",
# ]
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(elem + '\n')
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('purchases_data.txt', purchases_data)
# def read_file(path):
#     summa = 0
#     names_buy = {}
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             content = my_file.readlines()
#             for elem in content:
#                 elements = elem.strip().split(',')
#                 name = elements[0]
#                 buy = int(elements[2])
#                 if name in names_buy:
#                     names_buy[name] += buy
#                 else:
#                     names_buy[name] = buy
#             return names_buy
#     except FileNotFoundError as er:
#         print(er)
# resalt = read_file('purchases_data.txt')
# for key, val in resalt.items():
#     print(key, val)

# 16. Создать файл с данными о книгах в формате "название, автор, год издания".
# Прочитать файл, найти все книги определенного автора и вывести их на экран.
# books_data = [
#     "Война и мир, Лев Толстой, 1869",
#     "Преступление и наказание, Федор Достоевский, 1866",
#     "1984, Джордж Оруэлл, 1949",
#     "Гарри Поттер и философский камень, Джоан Роулинг, 1997",
#     "Мастер и Маргарита, Михаил Булгаков, 1967",
#     "Анна Каренина, Лев Толстой, 1877",
#     "Война и мир, Лев Толстой, 1869",
#     "Братья Карамазовы, Федор Достоевский, 1880"
# ]
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(elem + '\n')
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('books_data.txt', books_data)
# def read_file(path, author):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             content = my_file.readlines()
#             for element in content:
#                 elem = element.strip().split(', ')
#                 name_book = elem[0]
#                 author_name = elem[1]
#                 if author_name == author:
#                     print(f'{author_name}, {name_book}')
#     except FileNotFoundError as ex:
#         print(ex)
#
# read_file('books_data.txt', 'Лев Толстой')

