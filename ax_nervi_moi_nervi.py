# Создайте программу, которая меняет местами ключи и значения в словаре и выводит полученный результат.
#some_dict = {'apple': 1, 'banana': 2, 'pivo': 3}
# def change_key_value(**kwargs):
#     dict_out = {}
#     for key, value in kwargs.items():
#         dict_out[value] = key
#     return dict_out
# resalt = change_key_value(**some_dict)
# print(resalt)

# def change_key_value(**kwargs):
#     dict_out = {value: key for key, value in kwargs.items()}
#     return dict_out
# resalt = change_key_value(**some_dict)
# print(resalt)

#Напишите функцию, которая принимает список и возвращает новый список без дубликатов.
# some_spisok1 = [5, 55, 5, 25, 'lili', 'kiki', 'kiki', [2, 3], [2, 3]]
# some_spisok2 = [5, 55, 45, 35, 'lili', 'kiki', 'kiki', [2, 3], [2, 3]]
# def return_spisok_without_duplicate(*args):
#     list_out = [element for element in args if args.count(element) < 2]
#     return list_out
# resalt = return_spisok_without_duplicate(*some_spisok1, *some_spisok2)
# print(resalt)

# Создайте программу, которая принимает два списка и объединяет их в один, затем выводит результат.
# some_spisok1 = [5, 55, 5, 25, 'lili', 'kiki', 'kiki', [2, 3], [2, 3]]
# some_spisok2 = [5, 55, 45, 35, 'lili', 'kiki', 'kiki', [2, 3], [2, 3]]
# def union(*args):
#     list_out = [elem for elem in args]
#     return list_out
# resalt = union(*some_spisok1,*some_spisok2)
# print(resalt)

# Напишите функцию, которая принимает два кортежа и возвращает новый кортеж,
# содержащий элементы обоих кортежей.
# some_spisok1 = (5, 55, 5, 25, 'lili', 'kiki', 'kiki', [2, 3], [2, 3])
# some_spisok2 = (5, 55, 45, 35, 'lili', 'kiki', 'kiki', [2, 3], [2, 3])
# def union(*args):
#     for elem in args:
#         elem = (elem, )
#     union_tuple = [elem for elem in args]
#     return union_tuple
#
# resalt = union(*some_spisok1, *some_spisok2)
# print(resalt)

# Создайте программу, которая принимает список строк и возвращает новый список, содержащий
# только строки с длиной больше 5 символов, используя lambda и filter.
# some_text = ['we practice', 'milka', 'moonlight', 'happy and smile']
# def return_some_lenght_string(lenght: int, *args):
#     list_out = filter(lambda elem:  len(elem) > lenght, args)
#     return list(list_out)
# resalt = return_some_lenght_string(5, *some_text)
# print(resalt)

# Напишите функцию, которая принимает список кортежей (имя, возраст) и возвращает список имен,
# отсортированных по возрастанию возраста, используя lambda и sorted.
# some_list = [('Alice', 25), ('Bob', 30), ('Eve', 22), ('David', 40), ('Charlie', 28)]
# def get_name_for_age(*args):
#     list_out = sorted(args,  key=lambda elem: elem[1]) # чудо-чудесное
#     list_name = [element for element in list_out]
#     return list_name
# resalt = get_name_for_age(*some_list)
# print(resalt)

# Создайте программу, которая принимает список чисел и возвращает новый список, с
# одержащий только положительные числа, используя lambda и filter.
# some_spisok = [2, 16, 15, 85, 14, 3]
# def get_odd_numbers(*args):
#     list_out = filter(lambda number:  number % 2 == 0, args)
#     return list(list_out)
# resalt = get_odd_numbers(*some_spisok)
# print(resalt)

# Создайте программу, которая распаковывает словарь и выводит ключи и значения на экран.
# fruits = {
#     'apple': 'red',
#     'banana': 'yellow',
#     'grape': 'purple',
#     'orange': 'orange',
#     'kiwi': 'green'
# }
# def unpack_dict(**kwargs):
#     dict_out = {}
#     for key, value in kwargs.items():
#         dict_out[key] = value
#     return dict_out
# resalt = unpack_dict(**fruits)
# print(resalt)

# Напишите функцию, которая принимает список и возвращает кортеж с минимальным и максимальным значениями списка.
# some_spisok = [4, 21, -100, 16]
# def data_min_max_value(*args):
#     min_value = min(args)
#     max_value = max(args)
#     return (min_value, ), (max_value, )
# resalt = data_min_max_value(*some_spisok)
# print(resalt)

# Напишите программу, которая принимает строку и возвращает кортеж с количеством гласных и согласных букв.
# some_text = 'we like python so much!'
# vowes = 'a,o,u,e,y,i'
# def count_vowes_consonants_letters(text: str):
#     list_out = []
#     vowes_count = 0
#     not_vowes_count = 0
#     for letters in text:
#         if letters.isalnum():
#             if letters in vowes:
#                 vowes_count += 1
#             else:
#                 not_vowes_count += 1
#     return tuple((vowes_count, not_vowes_count))
# resalt = count_vowes_consonants_letters(some_text)
# print(resalt)

# Создайте функцию, которая принимает кортеж и возвращает его элементы в обратном порядке.
#some_data = ('python', 'we', 'like')
# def reverse_tuple(some):
#     new = list(some)
#     u = new[::-1]
#
#     return tuple(u)
# resalt = reverse_tuple(some_data)
# print(resalt)

# Напишите функцию, которая принимает список строк и возвращает новый список,
# содержащий только строки, начинающиеся с заглавной буквы, используя lambda и filter.
# some_data = ['python', 'We', 'like']
# def upper_words(text: list):
#     list_out = filter(lambda elem: elem[0].isupper(), text)
#     return list(list_out)
# resalt = upper_words(some_data)
# print(resalt)

# Создайте программу, которая принимает список слов и возвращает новый список,
# содержащий только слова, содержащие букву "а", используя lambda и filter.
# some_data = ['python', 'We', 'like', 'alphabet',  'and book']
# def get_words_for_letter(data: list, letter_find: str):
#     list_out = []
#     for element in data:
#         words = element.split()
#         for word in words:
#             if letter_find in word and word != letter_find:
#                 list_out.append(word)
#     return list_out
#
# resalt = get_words_for_letter(some_data, 'k')
# print(resalt)

# Напишите функцию, которая принимает список чисел и возвращает список их квадратов, используя lambda и map.
# some_spisok = list(range(1, 20))
# def return_square(some_spisok):
#     list_out = map(lambda number: number ** 2, some_spisok)
#     return list(list_out)
# resalt = return_square(some_spisok)
# print(resalt)

# Напишите программу, которая упаковывает числа от 1 до 10 в список и выводит его на экран.
# some_spisok = list(range(1, 11))
# def pack_list(*args):
#     list_out = [numb for numb in args]
#     return list_out
# resalt = pack_list(*some_spisok)
# print(resalt)

# Напишите функцию, которая принимает два списка и возвращает список с элементами,
# которые есть только в одном из списков.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# def uniq_element(spisok1: list, spisok2: list):
#     new = [elem for elem in spisok1 if elem not in spisok2] + [elem for elem in spisok2 if elem not in spisok1]
#     return new
# resalt = uniq_element(list1, list2)
# print(resalt)

# def uniq_element(spisok1: list, spisok2: list):
#     new_spisok1 = set(spisok1)
#     new_spisok2 = set(spisok2)
#     new = set(new_spisok1 ^ new_spisok2)
#     return list(new)
# resalt = uniq_element(list1, list2)
# print(resalt)

# Создайте программу, которая принимает строку и выводит словарь,
# в котором ключи - это символы из строки, а значения - количество их повторений.
#some_text = 'ppython'
# def make_dict(text: str):
#     dict_out = {}
#     for element in text:
#         dict_out[element] = text.count(element)
#     return dict_out
# resalt = make_dict(some_text)
# print(resalt)

# def make_dict(text: str):
#     dict_out = {element: text.count(element) for element in text}
#     return dict_out
# resalt = make_dict(some_text)
# print(resalt)

# Напишите функцию, которая принимает словарь и возвращает новый
# словарь без элементов с отрицательными значениями.
# some_dictin = {'lili': 5, 'mimi': -25, 'zizi': 'fifi', 'fifi': 100}
# def return_dict_positive_value(dictin:dict):
#     dict_out = {}
#     for key, value in dictin.items():
#         if type(value) == int and value > 0:
#             dict_out[key] = value
#     return dict_out
# resalt = return_dict_positive_value(some_dictin)
# print(resalt)

# Напишите функцию, которая принимает список кортежей (имя, зарплата)
# и возвращает список имен, отсортированных по убыванию зарплаты, используя lambda и sorted.
# employees_list = [('Alice', 5000), ('Bob', 4000), ('Charlie', 6000), ('David', 5500)]
# def sort_salary(salary: list):
#     sorted_salary = sorted(salary, key=lambda elem: elem[1], reverse=True)
#     sorted_names = [elem[0] for elem in sorted_salary]
#     return sorted_names
# resalt= sort_salary(employees_list)
# print(resalt)

# Создайте программу, которая принимает список чисел и возвращает новый
# список, содержащий только числа больше 10, используя lambda и filter.
# spisok = list(range (2, 22))
# def get_number(number_upp, *args):
#     list_out = filter(lambda elem: elem > number_upp, args)
#     return list(list_out)
# resalt = get_number(10, *spisok)
# print(resalt)

# Напишите функцию, которая принимает список строк и возвращает новый список,
# содержащий только строки, оканчивающиеся на букву "s", используя lambda и filter.
# some_spisok = [2, 'apples', 'bananas', 'apples', 15, 'grapes', [1, 2, 3], 'dogs']
# def get_element_end_some_letter( *args, letter):
#     list_out = filter(lambda elem: type(elem) == str and elem.endswith(letter), args)
#     return list(list_out)
# resalt = get_element_end_some_letter(letter='s', *some_spisok)
# print(resalt)

# Напишите программу, которая принимает словарь и возвращает список его ключей,
# отсортированных в алфавитном порядке.
# some_dict = {'lili': 1, 'fifi': 2, 'mimi': 4, 'vivi': 5, 'aiai': 6}
# def sort_key(dictin: dict):
#     for key, value in dictin.items():
#         list_out = sorted(key for key in dictin)
#     return list_out
# resalt = sort_key(some_dict)
# print(resalt)

# Создайте функцию, которая принимает список кортежей и возвращает новый список с элементами,
# упорядоченными по возрастанию второго элемента каждого кортежа.
# some_spisok = [(10, 55), (25, 60), (13, 95), (96, 100)]
# def sort_list(some_spisok):
#     listik = lambda elem: elem[1] in some_spisok
#     list_out = sorted(some_spisok, key=listik, reverse=True)
#     return  list(list_out)
# resalt = sort_list(some_spisok)
# print(resalt)

# Напишите программу, которая упаковывает числа от 1 до 5 в словарь,
# где ключами являются числа, а значениями их квадраты.
# some_numbers = range(1, 10)
# def pack_dict(numberi):
#     dict_out = {number: number ** number for number in numberi}
#     return dict_out
# resalt = pack_dict(some_numbers)
# print(resalt)

# Напишите функцию, которая принимает список и возвращает список его уникальных элементов
# в том же порядке, в котором они встречаются в исходном списке.
#some_spisok = ['lisa', 'miska', 'lisa', 'lemon', 'miska', 4, 45, 4, '55', '56', '55']
# def get_unique_element(some_spisok: list):
#     uniq_elements = []
#     for elem in some_spisok:
#         if elem not in uniq_elements:
#             uniq_elements.append(elem)
#     return uniq_elements
# resalt = get_unique_element(some_spisok)
# print(resalt)

# Напишите функцию, которая принимает список кортежей (имя, рост) и возвращает список имен,
# отсортированных по возрастанию роста, используя lambda и sorted.
# people_list = [('Alice', 165), ('Bob', 180), ('Charlie', 170), ('David', 175)]
# def sort_name_for_growth(people_list: list):
#     sorted_growth = sorted(people_list, key=lambda elem: elem[1], reverse=False)
#     sorted_name = [elem[0] for elem in sorted_growth]
#     return sorted_name
# resalt = sort_name_for_growth(people_list)
# print(resalt)

# Создайте программу, которая принимает список строк и возвращает новый список,
# содержащий только строки, содержащие цифры, используя lambda и filter.
# some_spisok = ['apple', 34, 'banana', '3', 'cherry', [1, 2, 3], 'orange', {'key': 'value'}, '3.14', 'grape', '(1, 2, 3)']
# def get_numeric(*args):
#     list_out = filter(lambda elem: type(elem) == str and any(el.isdigit() for el in elem), args)
#     return list(list_out)
#
# resalt = get_numeric(*some_spisok)
# print(resalt)

# Напишите функцию, которая принимает список чисел и возвращает новый список,
# содержащий квадратный корень из этих чисел, используя lambda и map.
# some_list = [4, 16, 81, 9, 4]
# def square(*args):
#     resalt = map(lambda elem: elem ** 0.5, args)
#     return list(resalt)
# resalt = square(*some_list)
# print(resalt)

