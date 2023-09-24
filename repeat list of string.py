# Объединить все строки из списка в одну большую строку.
# some_text = ['i like python!', 'hello my furry friend']
# list_out = []
# for elem in some_text:
#     list_out.append(elem)
# print(list_out)
import string

# Разделить строку на список подстрок, используя определенный разделитель.
# text = ['i: like: python!', 'hello my, furry, friend']
# text_new = []
# for elem in text:
#     words = elem.split(':')
#     text_new.append(words)
# print(text_new)

# Найти самую длинную строку в списке.
# text = ['i like python!', 'hello my furry friend', 'maman']
# max_lenght_string = 0
# for elem in text:
#     lenght = len(elem)
#     if len(elem) > max_lenght_string:
#         max_lenght_string = lenght
# print(max_lenght_string)

# Найти самую короткую строку в списке.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', 'ytikjvxtrud']
# min_lenght = len(text[0])
# shortest_string = ''
# for elem in text:
#     if len(elem) < min_lenght:
#         min_lenght = len(elem)
#         shortest_string = elem
# print(f'{min_lenght} размер минимальной строки в {text}, минимальная строка {shortest_string}')

# Посчитать количество символов в каждой строке списка.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', 'ytikjvxtrud']
# list_counter = []
# for elem in text:
#     counter_chars = 0
#     for char in elem:
#         counter_chars += 1
#     list_counter.append(counter_chars)
# print(list_counter)

# Удалить все пустые строки из списка.
# text = ['i like python!', 'hello my furry friend', '', 'maman', '4458', '8', '!', 'ytikjvxtrud', '']
# text_out = []
# for elem in text:
#     if len(elem) != 0:
#         text_out.append(elem)
# print(text_out)

# Проверить, все ли строки начинаются с определенной подстроки.
# text = ['i like python!', 'hello my furry friend', '', 'maman', '4458', '8', '!', 'ytikjvxtrud', '']
# substr = 'i'
# flag = False
# for elem in text:
#     if elem.startswith(substr):
#         flag = True
#     else:
#         flag = False
# if flag == True:
#     print('+')
# else:
#     print('-')

# Заменить все вхождения определенной подстроки во всех строках списка.
# text = ['i like python!', 'hello my furry friend', '', 'maman', '4458', '8', '!', 'ytikjvxtrud', '']
# substr = 'i'
# substr_change = '*'
# text_out = []
# for elem in text:
#     if substr in elem:
#         elem = elem.replace(substr, substr_change)# напоминаю себе что строку надо перезаписать т.к. она не изменияется
#         text_out.append(elem)
# print(text_out)

# Привести все строки к нижнему регистру.
# text = ['I like python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '']
# text_out = []
# for elem in text:
#     elem = elem.lower()
#     text_out.append(elem)
# print(text_out)

# Привести все строки к верхнему регистру.
# text = ['I like python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '']
# text_out = []
# for elem in text:
#     elem = elem.upper()
#     text_out.append(elem)
# print(text_out)

# Удалить все символы пунктуации из каждой строки.
# import string
# text = ['I like python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '']
# text_out = []
# for elem in text:
#     clean = ''
#     for char in elem:
#         if char not in string.punctuation:
#             clean += char
#     text_out.append(clean)
# print(text_out)

# Найти строки, содержащие определенное ключевое слово.
# text = ['I like Python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# string_to_find = 'python'
# list_out = []
# for elem in text:
#     if string_to_find.lower() in elem.lower():
#         list_out.append(elem)
# print(list_out)

# # Отсортировать строки в алфавитном порядке.
# text = ['I like Python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# text = sorted(text)
# print(text)

# Отсортировать строки в обратном алфавитном порядке.
# text = ['I like Python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# text = sorted(text, reversed=True)
# print(text)

# Удалить все пробелы из каждой строки.
# text = ['I like Python!', 'hellO my furry friend8', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# text_out = []
# for elem in text:
#     elem = elem.replace(' ', '')
#     text_out.append(elem)
# print(text_out)

# Удалить все цифры из каждой строки.
# text = ['I like Python!', 'hellO my furry friend8', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# text_out = []
# for elem in text:
#     clean = ''
#     for char in elem:
#         if not char.isdigit():
#             clean += char
#     text_out.append(clean)
# print(text_out)

# Отфильтровать строки, содержащие только буквы.
# text = ['I like Python!', 'hellO my furry friend8', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# def filtered(some_text: list):
#     resalt = [elem for elem in some_text if elem.isalpha()]
#     return resalt
# resalt = filtered(text)
# print(resalt)
#другой вариант
# text = ['I like Python!', 'hellO my furry friend8', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '', 'python']
# def filtered(some_text: list):
#     text_out = lambda elem: elem.isalpha()
#     result = filter(text_out, some_text)
#     return list(result)
#
# filtered_text = filtered(text)
# print(filtered_text)

# Разделить строки на два списка: те, которые содержат гласные, и те, которые содержат согласные.
# import string
#
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
#
# vowels = {}
# consonants = {}
# punctuation = {}
# digits = {}
#
# vowes_chars = 'aouyie'
# punctuation_chars = string.punctuation
#
# for elem in text:
#     for char in elem.lower():
#         if char.isalpha():
#             if char in vowes_chars:
#                 if char in vowels:
#                     vowels[char] += 1
#                 else:
#                     vowels[char] = 1
#             else:
#                 if char in consonants:
#                     consonants[char] += 1
#                 else:
#                     consonants[char] = 1
#         elif char.isnumeric():
#             if char in digits:
#                 digits[char] += 1
#             else:
#                 digits[char] = 1
#         elif char in punctuation_chars:
#             if char in punctuation:
#                 punctuation[char] += 1
#             else:
#                 punctuation[char] = 1
#
# print("Гласные:", vowels)
# print("Согласные:", consonants)
# print("Цифры:", digits)
# print("Знаки пунктуации:", punctuation)

# Посчитать количество строк, в которых содержится определенный символ.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# counter = 0
# symbol = 'a'
# for elem in text:
#     if symbol in elem.lower():
#         counter += 1
# print(counter)

# Перевернуть каждую строку в обратном порядке.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# list_out = []
# for elem in text:
#     list_out.append(elem[::-1])
# print(list_out)

# Заменить все гласные буквы в строках на определенный символ.
# vowes_chars = 'aouyie'
# symbol_to_change = '*'
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# list_out = []
# for elem in text:
#     word = ''
#     for char in elem.lower():
#         if char.lower() in vowes_chars:
#             word += symbol_to_change
#         else:
#             word += char
#     list_out.append(word)
# print(list_out)

# Заменить все цифры в строках на букву 'X'.
# text = ['i like python!', 'hello my furry friend', 'mamam', '4458', '8', '!', '']
# list_out = []
# symbol_to_change = 'X'
# for elem in text:
#     word = ''
#     for char in elem:
#         if char.isnumeric():
#             word += symbol_to_change
#         else:
#             word += char
#     list_out.append(word)
# print(list_out)

# Подсчитать количество строк, в которых первая и последняя буквы совпадают.
# text = ['i like python!', 'hello my furry friend', 'mamam', '4458',  '']
# counter = 0
# for elem in text:
#     if  len(elem) > 0 and elem[0].lower() == elem[-1] : # иначе возникает ошибка
#         counter += 1
# print(counter)

# Удалить из строк все символы, не являющиеся буквами.
# text = ['i like python!', 'hello my furry friend', 'mamam', '4458', '8', '!', '']
# text_out = []
# for elem in text:
#     element = ''
#     for char in elem:
#         if not  char.isalpha():
#             element += char
#         else:
#             pass
#     text_out.append(element)
# print(text_out)

# Проверить, являются ли все строки палиндромами (читаются одинаково слева направо и справа налево).
# text = ['mamam']
# flag = True
# for elem in text:
#     if elem.lower() != elem[::-1]: #сравнение первого элемента и последнего. если [0] то сравнение первого элемента с последующими
#         flag = False
#         break
#
# if flag ==  True:
#     print('+')
# else:
#     print('-')

# Найти строки, которые начинаются с определенной буквы.
# text = ['i like python!', 'hello my furry friend', 'i mamam', '4458', '8', '!', '']
# find_symbol_begin = 'i'
# text_out = []
# for elem in text:
#     if elem.lower().startswith(find_symbol_begin):
#         text_out.append(elem)
# print(text_out)

# Подсчитать количество строк, содержащих определенное количество символов.
# text = ['i like python!', 'hello my furry friend', 'i mamam', '4458', '8', '!', ' ']
# counter = 0
# list_out = []
# find_lenght = 1
# for elem in text:
#     if len(elem) == 1:
#         counter += 1
#         list_out.append(elem)
# print(f' кол-во строк {counter}, \n список таких строк  {list_out}')

# Заменить все пробелы в строках на подчеркивания.
# text = ['i like python!', 'hello my furry friend', 'i mamam', '4458', '8', '!', ' ']
# text_out = []
# symbol = '_'
# for elem in text:
#     element = ''
#     for char in elem:
#         if char == ' ':
#             element += symbol
#         else:
#             element += char
#     text_out.append(element)
# print(text_out)

# Удалить из строк все символы, не являющиеся буквами или цифрами.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# list_out = []
# for elem in text:
#     if any(char.isalnum() for char in elem):
#         list_out.append(elem)
# print(list_out)

# Посчитать количество строк, в которых нет буквенных символов.
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# counter = 0
# for elem in text:
#     if not any(char.isalpha() for char in elem):
#         break
#     else:
#         counter += 1
# print(counter)
# другая запись
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# counter = 0
# for elem in text:
#     has_letters = False
#     for char in elem:
#         if char.isalpha():
#             has_letters = True
#             break
#     if not has_letters:
#         counter += 1
# print(counter)
