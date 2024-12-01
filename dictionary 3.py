# Создайте список задач с категориями и статусами. Напишите функцию для подсчета количества невыполненных задач в каждой категории.
# tasks = [
#     {'title': 'Подготовить презентацию', 'category': 'Работа', 'status': 'В процессе'},
#     {'title': 'Купить продукты', 'category': 'Дом', 'status': 'Новая'},
#     {'title': 'Записаться на занятия йогой', 'category': 'Спорт', 'status': 'Новая'},
#     {'title': 'Прочитать новую книгу', 'category': 'Личное', 'status': 'Завершена'},
#     {'title': 'Убраться в комнате', 'category': 'Дом', 'status': 'В процессе'}
# ]
# def get_data(task_list: list):
#     status_not_end = {}
#     for elem in task_list:
#         title = elem['title']
#         category = elem['category']
#         status = elem['status']
#         if status != 'Завершена':
#             if category not in status_not_end:
#                 status_not_end[category] = 1
#
#             else:
#                 status_not_end[category] += 1
#     return status_not_end
# print(get_data(tasks))

# Создайте список книг в библиотеке с информацией о жанрах и авторах. Напишите функцию для поиска наиболее популярного жанра.
# library_books = [
#     {
#         'title': 'Война и мир',
#         'author': 'Лев Толстой',
#         'genre': 'Роман'
#     },
#     {
#         'title': 'Преступление и наказание',
#         'author': 'Федор Достоевский',
#         'genre': 'Роман'
#     },
#     {
#         'title': '1984',
#         'author': 'Джордж Оруэлл',
#         'genre': 'Антиутопия'
#     },
#     {
#         'title': 'Мастер и Маргарита',
#         'author': 'Михаил Булгаков',
#         'genre': 'Роман'
#     },
#     {
#         'title': 'Анна Каренина',
#         'author': 'Лев Толстой',
#         'genre': 'Роман'
#     }
# ]
# def find_data(some_list: list):
#     genre_dict = {}
#     for elem in some_list:
#         title = elem['title']
#         author = elem['author']
#         genre = elem['genre']
#         if genre not in genre_dict:
#             genre_dict[genre] = 1
#         else:
#             genre_dict[genre] += 1
#         resalt = max(genre_dict, key=genre_dict.get)
#     return resalt
# print(find_data(library_books))

