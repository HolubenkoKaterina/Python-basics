# a)	Создайте словарь, представляющий информацию о студенте (имя, возраст, средний балл).
# b)	Добавьте вложенные словари, чтобы представить информацию о нескольких студентах.
# c)	Найдите средний возраст среди всех студентов.
# d)	Найдите студента с наивысшим средним баллом.

# student1_info = {
#     'имя': 'Иван',
#     'возраст': 20,
#     'средний балл': 4.95
# }
#
# student2_info = {
#     'имя': 'Мария',
#     'возраст': 19,
#     'средний балл': 4.8
# }
#
# students = [student1_info, student2_info]
# print(students)
# def get_data(list_students: list):
#     aver_grades = []
#     summa_grades = 0
#     max_grade = float('-inf')
#     student_name = None
#     for elem in list_students:
#         name = elem['имя']
#         age = elem['возраст']
#         aver_grade = elem['средний балл']
#         if aver_grade > max_grade:
#             max_grade = aver_grade
#             student_name = name
#         aver_grades.append(aver_grade)
#     for el in aver_grades:
#         summa_grades += el
#     aver = summa_grades / len(aver_grades)
#     return f'{aver} средняя оценка , максимальная оценка {max_grade}, имя студента с максимальным баллом {student_name}'
# res = get_data(students)
# print(res)

# Создайте список целых чисел и найдите сумму всех элементов.
# import random
# numbers_list = random.sample(range(4, 15), random.randint(2, 8))
# print(numbers_list)
# summa = 0
# for elem in numbers_list:
#     summa += elem
# print(summa)

# Создайте список слов и найдите самое длинное слово.
# list_words = ['Яблоко', 'Машина', 'Солнце', 'Книга', 'Дом', 'Велосипед', 'Молоко']
# max_lenght = float('-inf')
# for elem in list_words:
#     if len(elem) > max_lenght:
#         max_lenght = len(elem)
# print(max_lenght)

# Создайте два списка чисел и найдите их сумму попарно.
# import random
# list1 = random.sample(range(1, 11), 4)
# list2 = random.sample(range(11, 21), 4)
# print(list1)
# print(list2)
# summa_list = []
# summa = 0
# for index in range(len(list1)):
#     summa_list.append(list1[index] + list2[index]) # сама не решила к сожалению
# print(summa_list)

# 47. Создайте список и удалите из него все дубликаты.
# list_numb = [18, 11, 13, 20, 18, 11, 13, 20]
# list_out = set(list_numb)
# print(list_out)

# Создайте список, содержащий списки чисел, и найдите сумму элементов внутренних списков.
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list_sum = []
# for elem in list_of_lists:
#     summa = 0
#     for el in elem:
#         summa += el
#     list_sum.append(summa)
# print(list_sum)

# Создайте список, в котором каждый элемент - это пара (имя, возраст), и найдите средний возраст.
# people = [
#     ("Иван", 20),
#     ("Мария", 19),
#     ("Петр", 22),
#     ("Анна", 21)
# ]
# aver_age = 0
# aver = 0
# for elem in people:
#     aver_age += elem[1]
#     aver = aver_age / len(people)
# print(aver)

# Создайте список, представляющий матрицу, и выполните операцию транспонирования.
# matrix = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# matrix_out = []
# for rows in range(len(matrix[0])):
#     row = []
#     for strings in range(len(matrix)):
#         row.append(matrix[strings][rows])
#     matrix_out.append(row)
# print(matrix)
# print(matrix_out)

# Напишите программу, которая находит самое длинное слово в строке.
# import string
# my_string = '«Python — потрясающий язык программирования!»'
# # Убираем знаки препинания
# new_string = str.maketrans('', '', string.punctuation)
# new = my_string.translate(new_string)
# new_string = new.replace('«', '').replace('»', '')
# max_len = float('-inf')
# for word in new_string.split():
#     if len(word) > max_len:
#         max_len = len(word)
#
# print(max_len)

# Напишите программу, которая проверяет, начинается ли строка с определенного префикса.
# strin = 'Python — потрясающий язык программирования!'
# def prefix(some_text: str, prefix_find: str):
#     for word in some_text.split():
#         if word.startswith(prefix_find):
#             return '+'
#     return '-'
# resalt = prefix(strin, prefix_find='потр')
# print(resalt)

# Создайте два множества и найдите их объединение.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))

# Создайте два множества и найдите их пересечение.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))

# Создайте множество с буквами алфавита и проверьте, содержит ли оно все гласные буквы.
# alphabet_set = set('bcdefghijklmnopqrstuvwxyz')
# vowels_set = set('aeiou')
# contains_vowels = all(vowel in alphabet_set for vowel in vowels_set)
# print(contains_vowels)

# Создайте множество с числами и найдите максимальное и минимальное значения.
# set_check = {1, 2, 3, 4, 5}
# min_el = float('inf')
# max_el = float('-inf')
# for elem in set_check:
#     if elem > max_el:
#         max_el = elem
#     if elem < min_el:
#         min_el = elem
# print(max_el, min_el)

# Создайте два множества и найдите разницу между ними (элементы, которые есть в первом, но отсутствуют во втором).
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.difference(set2))

# Создайте словарь с данными о квартире (адрес, площадь, количество комнат) и выведите площадь квартиры.
# apartment_data = {
#     'flat1': {'address': 'ул. Ленина, 1', 'area': 50, 'rooms': 2},
#     'flat2': {'address': 'ул. Пушкина, 5', 'area': 70, 'rooms': 3},
#     'flat3': {'address': 'ул. Гагарина, 10', 'area': 40, 'rooms': 1}
# }
# def get_data(some_dict: dict, adress_get_area):
#     for key, val in some_dict.items():
#         area_flat = val['area']
#         adress = val['rooms']
#         if adress_get_area == adress:
#             return area_flat
# resalt = get_data(apartment_data, adress_get_area=1)
# print(resalt)

# Создайте словарь с данными о языке программирования (название, создатель, год создания) и найдите создателя языка.
# programming_languages = {
#     'Python': {'creator': 'Guido van Rossum', 'year_created': 1991},
#     'Java': {'creator': 'James Gosling', 'year_created': 1995},
#     'C++': {'creator': 'Bjarne Stroustrup', 'year_created': 1985},
#     'JavaScript': {'creator': 'Brendan Eich', 'year_created': 1995},
#     'Ruby': {'creator': 'Yukihiro Matsumoto', 'year_created': 1995}
# }
# def get_data_author(some_dict: dict, language_find: str):
#     for key, val in some_dict.items():
#         language = key
#         author = val['creator']
#         year = val['year_created']
#         if language_find.lower() in language.lower():
#             return language, year
#
# resalt = get_data_author(programming_languages, language_find='thon')
# print(resalt)

# Создайте список словарей, представляющий информацию о рецептах (название, ингредиенты и их количество)
# и найдите все рецепты, в которых используется определенный ингредиент.
# recipes = [
#     {
#         'название': 'Салат "Цезарь"',
#         'ингредиенты': {
#             'листья салата': 150,
#             'куриное филе': 200,
#             'гренки': 100,
#             'пармезан': 50,
#             'соус "Цезарь"': 50
#         }
#     },
#     {
#         'название': 'Борщ',
#         'ингредиенты': {
#             'свекла': 200,
#             'картофель': 150,
#             'капуста': 100,
#             'мясо': 300,
#             'лук': 50,
#             'морковь': 50
#         }
#     },
#     {
#         'название': 'Пицца',
#         'ингредиенты': {
#             'тесто': 200,
#             'помидоры': 100,
#             'сыр': 100,
#             'пепперони': 50
#         }
#     }
# ]
# def get_data(some_list: list, ingredient_find):
#     for elem in some_list:
#         name = elem['название']
#         ingredients = elem['ингредиенты']
#         for ingredient in ingredients:
#             if ingredient_find.lower() in ingredient.lower():
#                 return name
# resalt = get_data(recipes, ingredient_find='свек')
# print(resalt)

# Создайте список словарей, представляющий информацию о городах (название, население, страна) и найдите город с наибольшим населением.
# cities = [
#     {
#         'название': 'Нью-Йорк',
#         'население': 8537673,
#         'страна': 'США'
#     },
#     {
#         'название': 'Токио',
#         'население': 13929286,
#         'страна': 'Япония'
#     },
#     {
#         'название': 'Лондон',
#         'население': 8908081,
#         'страна': 'Великобритания'
#     }
# ]
# def get_max_population(list_cities: list):
#     max_population = float('-inf')
#     country_max_popation = None
#     for elem in list_cities:
#         city = elem['название']
#         population = elem['население']
#         country = elem['страна']
#         if population > max_population:
#             max_population = population
#             country_max_popation = country
#     return max_population, country_max_popation
# resalt = get_max_population(cities)
# print(resalt)

# Создайте функцию, которая находит наименьшее значение в списке чисел.
# import random
# list_num = random.sample(range(3, 21), random.randint(2, 15))
# print(list_num)
# min_val = float('inf')
# for num in list_num:
#     if min_val > num:
#         min_val = num
# print(min_val)

# Создайте функцию, которая находит количество гласных букв в строке.
# some_str = 'i like python very much!'
# vowes = 'aeiouy'
# count = 0
# for letter in some_str:
#     if letter.lower() in vowes:
#         count += 1
# print(count)

# Создайте функцию, которая принимает произвольное количество аргументов и возвращает их сумму, используя оператор * для распаковки.
# nums = [(4, 6), 15, 0]
# def summa(*args):
#     summa = 0
#     for arg in args:
#         if isinstance(arg, (int, float)):
#             summa += arg
#         elif isinstance(arg, (tuple, set)):
#             summa += sum(arg)
#     return summa
# resalt = summa(*nums)
# print(resalt)

# Напишите функцию, которая принимает список чисел и возвращает наименьшее число, используя оператор * для распаковки списка.
# list_nums = [4, 15, -28, (-65, -1)]
# def get_min_num(*args):
#     min_num = float('inf')
#     for arg in args:
#         if isinstance(arg, (int, float)):
#             if arg < min_num:
#                 min_num = arg
#         elif isinstance(arg, (tuple, set, list)):
#             for elem in arg:
#                 if elem < min_num:
#                     min_num = elem
#     return min_num
# resalt = get_min_num(*list_nums)
# print(resalt)

# Создайте функцию, которая принимает два списка и объединяет их в один, используя оператор *.
# list1 = [4, 6]
# list2 = ['python', '18']
# def union_lists(list1, list2):
#     resalt_list = [*list1, *list2]
#
#     return resalt_list
# realt = union_lists(list2, list1)
# print(realt)

# Создайте функцию-генератор, которая генерирует числа от 1 до N.
# def generator(n):
#     for num in range(n, n+1):
#         yield num
# resalt = generator(n=10)
# for num in resalt:
#     print(num)

# Напишите функцию-генератор, которая генерирует четные числа от 0 до N.
# def generator(n):
#     for num in range(0, n):
#         if num % 2 == 0:
#             yield num
# resalt = generator(14)
# for num in resalt:
#     print(num)

# Преобразование списка строк в список их длин.
# strings = [
#     'Короткая строка',
#     'Немного длиннее',
#     'Эта строка еще длиннее чем предыдущая',
#     'Самая длинная строка в этом списке. Она содержит больше всего символов.'
# ]
# resalt = [len(elem) for elem in strings]
# print(resalt)

# Умножение каждого элемента списка на определенное число.
# import random
# list_num = random.sample(range(4, 15), random.randint(2, 7))
# print(list_num)
# resalt = [num * 2 for num in list_num]
# print(resalt)

# Перевод температуры из Цельсия в Фаренгейт для списка температур.
# data = float(input('введите ваши градусы Цельсия  '))
# data_out = data * 9 / 5 + 32
# print(f'{data_out} F')

# Проверка, все ли элементы списка положительны.
# import random
# list_num = random.sample(range(-50, 51), random.randint(2, 8))
# print(list_num)
# resalt = all(elem > 0 for elem in list_num)
# print(resalt)

# Проверка, все ли элементы строки являются буквами верхнего регистра.
# text = 'python i like'
# resalt = all(letter.isupper() for letter in text)
# print(resalt)

# Проверка, все ли элементы вложенных списков являются числами.
# list_elem = [[2, 14], [14, 14]]
# resalt = all(type(el) == int for elem in list_elem for el in elem)
# print(resalt)

# Проверка, есть ли в списке хотя бы один отрицательный элемент.
# import random
# list_num = random.sample(range(-15, 16), random.randint(2, 8))
# print(list_num)
# resalt = any(elem < 0 for elem in list_num)
# print(resalt)

# Проверка, есть ли в строке хотя бы один символ верхнего регистра.
# text = 'i like python'
# resalt = any(letter.isupper() for letter in text)
# print(resalt)

# Проверка, есть ли во всех вложенных списках хотя бы один нулевой элемент.
# import random
# nested_list = [[0, 4, 15], [0, 2]]
# #nested_list = [[random.randint(-11, 9) for _ in range(3)] for _ in range(3)]
# print(nested_list)
# resalt = any(el == 0 for elem in nested_list for el in elem)
# print(resalt)

# Фильтрация списка, чтобы получить только положительные числа.
# import random
# list_num = random.sample(range(-15, 16), random.randint(2, 8))
# print(list_num)
# resalt = list(filter(lambda elem: elem > 0, list_num))
# print(resalt)

# Фильтрация списка строк, чтобы получить только строки, содержащие определенную подстроку.
# text = ["Привет, мир!", "Python — потрясающий язык программирования!", "OpenAI создал умного помощника по имени ChatGPT!",
# "Зима близко, приготовьтесь к снегопаду!",  "Коты любят играть с мячиками."]
# substr = 'от'
# resalt = list(filter(lambda string: substr.lower() in string.lower(), text))
# print(resalt)

# Фильтрация списка, чтобы получить только четные числа.
# import random
# list_num = random.sample(range(-15, 16), random.randint(2, 8))
# print(list_num)
# resalt = list(filter(lambda num: num % 2 == 0, list_num))
# print(resalt)

# Декоратор с параметрами для ограничения доступа: Напишите декоратор, который принимает
# список разрешений в качестве параметра и разрешает выполнение функции только пользователям с соответствующими разрешениями.
# employees = [
#     {
#         'имя': 'Иван',
#         'фамилия': 'Петров',
#         'должность': 'менеджер'
#     },
#     {
#         'имя': 'Елена',
#         'фамилия': 'Сидорова',
#         'должность': 'разработчик'
#     },
#     {
#         'имя': 'Анна',
#         'фамилия': 'Иванова',
#         'должность': 'тестировщик'
#     },
#     {
#         'имя': 'Дмитрий',
#         'фамилия': 'Козлов',
#         'должность': 'аналитик'
#     }
# ]
# def get_info(employee_list: list, position_find):
#     names = []
#     for elem in employee_list:
#         name = elem['имя']
#         surname = elem['фамилия']
#         position = elem['должность']
#         if position_find.lower() in position.lower():
#             names.append(surname)
#     return names
# resalt = get_info(employees, position_find='лит')
#
# def decorator(resalt):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             for person in resalt:
#                 if person in args[0].lower():
#                     return func(*args, **kwargs)
#                 else:
#                     return "Доступ запрещен"
#         return inner
#     return wrapper
#
# @decorator(resalt)
# def check(user):
#     return f"Доступ разрешен, {user}!"
# result = check('козлов')
# print(result)

# Создайте функцию, которая определяет, является ли строка палиндромом.
# import string
# text = 'I like python!'
# translator = str.maketrans('', '', string.punctuation)
# new_text = text.translate(translator)
# cleaned_text = new_text.replace(' ', '').lower()
# def check(text: str):
#     return cleaned_text == cleaned_text[::-1]
# resalt = check(cleaned_text)
# print(resalt)

# Создайте функцию, которая объединяет два списка чисел в список кортежей,
# где каждый кортеж содержит элементы с одинаковыми индексами.
# list1 = [2, 4, 6, 8, 10]
# print(list1)
# list2 = [1, 3, 5, 7, 9]
# print(list2)
# def combine_lists(list1, list2):
#     list_out = []
#     for index in range(len(list1)):
#         tuple_element = (list1[index], list2[index])
#         list_out.append(tuple_element)
#     return list_out
#
# result = combine_lists(list1, list2)
# print(result)

# Напишите функцию, которая объединяет список имен и список фамилий в список полных имён, используя zip().
# names = ['Александр', 'Екатерина', 'Михаил',  'Анна',  'Иван', 'Наталья', 'Дмитрий',  'Александра', 'Сергей',  'Ольга']
# surnames = ['Иванов',  'Смирнова',  'Кузнецов',  'Попова',  'Васильев',  'Петрова',  'Соколов',  'Михайлова',  'Новиков', 'Федорова']
# persons = list(zip(names, surnames))
# print(persons)

# Создайте функцию, которая объединяет список дат и список событий в словарь, где даты служат ключами, а события - значениями.
# dates = ['2023-10-27', '2023-11-05', '2023-11-12', '2023-11-19', '2023-12-03']
# planes = ['Встреча с клиентом', 'Презентация нового продукта', 'Конференция "Технологии будущего"', 'Заключение партнерского соглашения', 'Обучение новых сотрудников']
# dict_out = {}
# for elem in dates:
#     for el in planes:
#         dict_out[elem] = el
# print(dict_out)

# Отсортировать список чисел в порядке возрастания и сохранить результат в новом списке.
# import  random
# list_nums = random.sample(range(1, 15), random.randint(2, 8))
# print(list_nums)
# resalt = sorted(list_nums, key=lambda elem: elem)
# print(resalt)

# Отсортировать список строк в алфавитном порядке и вернуть отсортированный список.
# text = [
#     "Привет, как дела?",
#     "Python - потрясающий язык программирования!",
#     "Сегодня отличный день для изучения нового",
#     "OpenAI разрабатывает потрясающие технологии",
#     "Лучше всего начинать с малого и постепенно двигаться вперёд"
# ]
# resalt = sorted(text, key=lambda elem: elem)
# print(resalt)

# Отсортировать список словарей по определенному ключу (например, "возраст" или "имя") и сохранить результат в новом списке.
# people_data = [
#     {'имя': 'Иван', 'возраст': 25},
#     {'имя': 'Мария', 'возраст': 30},
#     {'имя': 'Алексей', 'возраст': 28},
#     {'имя': 'Елена', 'возраст': 22},
#     {'имя': 'Дмитрий', 'возраст': 35}
# ]
# resalt = sorted(people_data, key=lambda elem: elem['возраст'])
# print(resalt)

# Отсортируйте список словарей по ключу, представляющему дату.
# events_data = [
#     {'date': '2023-10-28', 'event': 'Meeting'},
#     {'date': '2023-10-29', 'event': 'Conference'},
#     {'date': '2023-10-30', 'event': 'Presentation'},
#     {'date': '2023-10-31', 'event': 'Workshop'},
#     {'date': '2023-11-01', 'event': 'Seminar'}
# ]
# resalt = sorted(events_data, key=lambda elem: elem['date'])
# print(resalt)

# #Отсортируйте список кортежей сначала по первому элементу, а затем по второму элементу.
# list_of_tuples = [
#     (1, 2),
#     (3, 4),
#     (5, 6),
#     (7, 8),
#     (9, 10)
# ]
# resalt = sorted(list_of_tuples, key=lambda elem: (elem[0], elem[1]))
# print(resalt)

# Напишите программу, которая читает содержимое текстового файла и выводит его на экран.
# text = 'Яблоко, Машина'
# def write_text(some_text, path):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             my_file.write(some_text)
#     except FileNotFoundError as ex:
#         print(ex)
# res = write_text(text, 'text.txt')
#
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             return my_file.read()
#     except FileNotFoundError as ex:
#         print(ex)
# resalt = read_file('text.txt')
# print(resalt)

# Напишите функцию, которая читает текст из одного файла и записывает его в другой файл.
# text = [2, 4, 6]
# def write_text(text, path):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             my_file.write(str(text))
#     except FileNotFoundError as ex:
#         print(ex)
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             return my_file.read()
#     except FileNotFoundError as ex:
#         print(ex)
# def write_new(text, path):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             return my_file.write(text)
#     except FileNotFoundError as ex:
#         print(ex)
#
# write_text(text, 'text.txt')
# content = read_file('text.txt')
# write_new(content, 'text1.txt')

# Создайте программу, которая добавляет текст в конец существующего текстового файла.
# text = 'i like python!'
# appended_data = 'very much'
# def write_text(some_text, path):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             my_file.write(str(text))
#     except FileNotFoundError as ex:
#         print(ex)
#
# def append_data(data, path):
#     try:
#         with open(path, 'a', encoding='utf-8') as my_file:
#             my_file.write(str(data) + '\n')
#     except FileNotFoundError as ex:
#         print(ex)
# write_text(text, 'text.txt' )
# append_data(appended_data, 'text.txt')

# Факториал числа: Напишите функцию, которая вычисляет факториал заданного положительного целого числа с использованием рекурсии.
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# res = factorial(15)
# print(res)

# Сумма чисел: Создайте функцию, которая вычисляет сумму всех чисел от 1 до заданного положительного целого числа с использованием рекурсии.
# def summa(n):
#     if n == 1:
#         return 1
#     return n + summa(n - 1)
# res = summa(4)
# print(res)

# Счетчик с начальным значением: Создайте замыкание, которое
# предоставляет счетчик с возможностью установки начального значения при его создании.
# def decorator(start_counter):
#     def wrapper(func):
#         counter = start_counter
#         def inner(*args, **kwargs):
#             nonlocal counter
#             resalt = func(*args, **kwargs)
#             counter += 1
#             return resalt
#         return inner
#     return wrapper
#
# @decorator(start_counter=4)
# def summa(numbers: list):
#     summa = 0
#     for num in numbers:
#         summa += num
#     return summa
# res = summa([4, 6])
# print(res)

# Напишите программу, которая создает бинарный файл и записывает в него список чисел.
# import pickle
# text = 'i like dogs'
# def write_file(some_text, path):
#     try:
#         with open(path, 'wb') as my_file:
#             pickle.dump(some_text, my_file)
#     except FileNotFoundError as ex:
#         print(ex)
# spisok = [4, 6]
# write_file(spisok, 'some_text')

# def read_file(path):
#     try:
#         with open(path, 'rb') as my_file:
#             data = pickle.load(my_file)
#             print(data)
#     except FileNotFoundError as ex:
#         print(ex)
#
# read_file('some_text')

# Декоратор для логирования:
# Напишите декоратор, который регистрирует вызов функции и выводит информацию о нем,
# такую как имя функции и переданные аргументы.

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         resalt = func(*args, **kwargs)
#         name = func.__name__
#         arguments = args
#         return f'{name} and {arguments}'
#     return wrapper
# @decorator
# def check(user):
#     return f"Доступ разрешен, {user}!"
#
# result = check('козлов')
# print(result)







