# Создайте список классов школы, включающий информацию о студентах и учителях.
# Напишите функцию для подсчета общего количества студентов и учителей.
# school_classes = [
#     {
#         'class_name': '10A',
#         'students': [
#             {'name': 'Иванов Иван', 'age': 16, 'grades': [5, 4, 4, 5]},
#             {'name': 'Петров Петр', 'age': 16, 'grades': [4, 5, 4, 5]},
#             {'name': 'Сидоров Сидор', 'age': 16, 'grades': [3, 3, 4, 4]}
#         ],
#         'teacher': {'name': 'Мария Ивановна', 'subject': 'Математика'}
#     },
#     {
#         'class_name': '11B',
#         'students': [
#             {'name': 'Елена Сергеевна', 'age': 17, 'grades': [5, 5, 5, 5]},
#             {'name': 'Ольга Петровна', 'age': 17, 'grades': [4, 5, 5, 4]},
#             {'name': 'Александр Иванович', 'age': 17, 'grades': [4, 4, 3, 5]}
#         ],
#         'teacher': {'name': 'Андрей Николаевич', 'subject': 'Физика'}
#     }
# ]
# def find_count(school_classes: list):
#     count_teachers = 0
#     count_students = 0
#     count_classes = 0
#     for elem in school_classes:
#         for key, val in elem.items():
#             class_name = elem['class_name']
#             teacher = elem['teacher']
#             students = elem['students']
#
#             for student in students:
#                 name = student['name']
#                 age = student['age']
#                 grades = student['grades']
#             count_students += 1
#         count_classes += 1
#         count_teachers += 1
#
#     return count_students, count_teachers, count_classes
# print(find_count(school_classes))

# Создайте список компаний с информацией о сотрудниках и их зарплатах.
# Напишите функцию для нахождения компании с самой высокой средней зарплатой.
# companies = [
#     {
#         'name': 'Company A',
#         'employees': [
#             {'name': 'John Doe', 'salary': 50000},
#             {'name': 'Jane Doe', 'salary': 55000},
#             {'name': 'Jim Brown', 'salary': 60000}
#         ]
#     },
#     {
#         'name': 'Company B',
#         'employees': [
#             {'name': 'Bob Smith', 'salary': 48000},
#             {'name': 'Sue Johnson', 'salary': 52000},
#             {'name': 'Tom Davis', 'salary': 58000}
#         ]
#     }
# ]
# def find_company_with_highest_average_salary(companies_list):
#     highest_average_salary = 0
#     company_with_highest_salary = None
#
#     for company in companies_list:
#         company_name = company['name']
#         employees = company['employees']
#
#         total_salary = sum(employee['salary'] for employee in employees)
#         average_salary = total_salary / len(employees)
#
#         if average_salary > highest_average_salary:
#             highest_average_salary = average_salary
#             company_with_highest_salary = company_name
#
#     return company_with_highest_salary
#
# highest_salary_company = find_company_with_highest_average_salary(companies)
# print(f"Компания с самой высокой средней зарплатой: {highest_salary_company}")

# Создайте список городов с информацией о климате (температура, влажность) в разные сезоны.
# Напишите функцию для нахождения города с самыми приятными погодными условиями.
# cities_climate = [
#     {
#         'city': 'Нью-Йорк',
#         'seasons': {
#             'зима': {'температура': -1, 'влажность': 60},
#             'весна': {'температура': 12, 'влажность': 65},
#             'лето': {'температура': 28, 'влажность': 70},
#             'осень': {'температура': 16, 'влажность': 68}
#         }
#     },
#     {
#         'city': 'Лос-Анджелес',
#         'seasons': {
#             'зима': {'температура': 12, 'влажность': 75},
#             'весна': {'температура': 20, 'влажность': 70},
#             'лето': {'температура': 32, 'влажность': 65},
#             'осень': {'температура': 25, 'влажность': 72}
#         }
#     },
#     {
#         'city': 'Токио',
#         'seasons': {
#             'зима': {'температура': 5, 'влажность': 55},
#             'весна': {'температура': 15, 'влажность': 60},
#             'лето': {'температура': 28, 'влажность': 75},
#             'осень': {'температура': 20, 'влажность': 70}
#         }
#     }
# ]
# def get_data(my_list: list):
#     list_city = {}
#     list_out = []
#     for elem in my_list:
#         summa_temp = 0
#         summa_humidity = 0
#         city = elem['city']
#         seasons = elem['seasons']
#         for season_name, season_data in seasons.items():
#             temperature = season_data['температура']
#             humidity = season_data['влажность']
#             summa_temp += temperature
#             summa_humidity += humidity
#         aver_t = summa_temp / len(seasons)
#         aver_h = summa_humidity / len(seasons)
#         list_city[city] = (aver_t, aver_h)
#     best_temp = list(range(15, 22))
#     best_hum = list(range(60, 70))
#     for city, parameters in list_city.items():
#         if parameters[0] in best_temp and parameters[1] in best_hum:
#             list_out.append(city)
#     return list_out
# print(get_data(cities_climate))

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

# Создайте список спортивных команд с информацией о игроках и их статистике.
# Напишите функцию для поиска команды с наилучшей средней статистикой игроков.
# sports_teams = [
#     {
#         'team_name': 'Красные короли',
#         'players': [
#             {'name': 'Иванов', 'number': 7, 'scored_goals': 15},
#             {'name': 'Петров', 'number': 11, 'scored_goals': 10},
#             {'name': 'Сидоров', 'number': 9, 'scored_goals': 12},
#         ]
#     },
#     {
#         'team_name': 'Синие молнии',
#         'players': [
#             {'name': 'Смирнов', 'number': 8, 'scored_goals': 20},
#             {'name': 'Кузнецов', 'number': 14, 'scored_goals': 18},
#             {'name': 'Михайлов', 'number': 12, 'scored_goals': 17},
#         ]
#     },
#  ]
# def get_data(teams_list: list):
#     counter_goals = {}
#
#     for elem in teams_list:
#         summa_goals = 0
#         team_name = elem['team_name']
#         players = elem['players']
#         for player in players:
#             name = player['name']
#             number = int(player['number'])
#             scored_goals = int(player['scored_goals'])
#             summa_goals += scored_goals
#             aver = round(summa_goals / len(players), 2)
#         if team_name not in counter_goals:
#             counter_goals[team_name] = aver
#         else:
#             counter_goals[team_name] += aver
#         resalt = max(counter_goals, key=lambda elem: counter_goals[team_name])
#
#     return resalt
# print(get_data(sports_teams))