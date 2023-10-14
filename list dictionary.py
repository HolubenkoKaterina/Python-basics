
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
# # Пример использования
# highest_salary_company = find_company_with_highest_average_salary(companies)
# print(f"Компания с самой высокой средней зарплатой: {highest_salary_company}")
















# Создайте список городов с информацией о климате (температура, влажность) в разные сезоны. Напишите функцию для нахождения города с самыми приятными погодными условиями.
# Создайте список столовых, включающий информацию о меню и столиках. Напишите функцию, которая предлагает клиенту подходящие столики в зависимости от его предпочтений в меню.
# Создайте список задач с категориями и статусами. Напишите функцию для подсчета количества невыполненных задач в каждой категории.
# Создайте список книг в библиотеке с информацией о жанрах и авторах. Напишите функцию для поиска наиболее популярного жанра.
# Создайте список праздников с информацией о датах и странах, в которых они отмечаются. Напишите функцию для поиска праздника в определенной стране по дате.
# Создайте список проектов с информацией о задачах и сроках выполнения. Напишите функцию для нахождения проектов, сроки выполнения задач в которых наиболее близки к истечению.
# Создайте список спортивных команд с информацией о игроках и их статистике. Напишите функцию для поиска команды с наилучшей средней статистикой игроков.
