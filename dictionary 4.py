# Создайте список праздников с информацией о датах и странах, в которых они отмечаются.
# Напишите функцию для поиска праздника в определенной стране по дате.
# holidays = [
#     {'name': 'Новый год', 'date': '01-01', 'country': 'Россия'},
#     {'name': 'День независимости', 'date': '04-07', 'country': 'США'},
#     {'name': 'День Бастилии', 'date': '14-07', 'country': 'Франция'},
#     {'name': 'Праздник весны и труда', 'date': '01-05', 'country': 'Множество стран'},
#     {'name': 'День победы', 'date': '09-05', 'country': 'Россия'},
#     {'name': 'Рождество', 'date': '25-12', 'country': 'Множество стран'},
#
# ]
# def get_data(some_list_of_dict: list,  data_find):
#     list_out = []
#     for elem in some_list_of_dict:
#         holiday = elem['name']
#         data_holiday = elem['date']
#         country = elem['country']
#         if data_holiday == data_find:
#             # if country == country_find.lower():
#             list_out.append((holiday, country, data_find))
#     return list_out
# print(get_data(holidays, data_find='01-01'))

# Создайте список проектов с информацией о задачах и сроках выполнения.
# Напишите функцию для нахождения проектов, сроки выполнения задач в которых наиболее близки к истечению.
# projects = [
#     {
#         'project_name': 'Проект 1',
#         'tasks': [
#             {'title': 'Задача 1', 'deadline': '2023-10-15'},
#             {'title': 'Задача 2', 'deadline': '2023-10-05'},
#             {'title': 'Задача 3', 'deadline': '2023-10-03'}
#         ]
#     },
#     {
#         'project_name': 'Проект 2',
#         'tasks': [
#             {'title': 'Задача 4', 'deadline': '2023-10-02'},
#             {'title': 'Задача 5', 'deadline': '2023-09-30'}
#         ]
#     }
# ]
# import datetime
# def get_data(task_list: list):
#     list_title = []
#     now_date = datetime.datetime.now().day
#     for elem in task_list:
#         project_name = elem['project_name']
#         tasks = elem['tasks']
#         for task in tasks:
#             title = task['title']
#             deadline_str = task['deadline']
#             deadline_date = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')
#             if (deadline_date - datetime.datetime.now()).days < 4:
#                 list_title.append((project_name,  title))
#     return list_title
# print(get_data(projects))

