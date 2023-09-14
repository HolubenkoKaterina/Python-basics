# Посчитать сумму квадратов чисел в списке с использованием лямбда-функции.
# some_spisok = [2, 5, 10, 25, 50]
# def summa_square_numbers(spisok: list):
#     summa = 0
#     for element in spisok:
#         element_new = element ** 2
#         summa += element_new
#     return summa
# resalt = summa_square_numbers(some_spisok)
# print(resalt)
# resalt = lambda element: sum(map (lambda element:(element**2), element))
# print(resalt(some_spisok))

# Найти наибольший элемент в списке чисел с использованием лямбда-функции.
# some_spisok = [2, 5, 10, 25, 50, -100]
# resalt_max_number = lambda element: max(element)
# print(resalt_max_number(some_spisok))

# Проверить, являются ли все элементы списка положительными числами с использованием лямбда-функции.
# some_spisok = [2, 5, 10, 25, 50, -100]
# resalt_check_positive_numbers = lambda element: all(map(lambda element: element > 0, element))
# print(resalt_check_positive_numbers(some_spisok))


# Создать список всех букв в строке в верхнем регистре с использованием генератора списков.
# some_string = 'I Like Python'
# def upper_letters_list(string: str):
#     new_list = []
#     for word in string:
#         if word.isupper():
#             new_list.append(word)
#     return new_list
# r = upper_letters_list(some_string)
# print(r)
# new_list = [word for word in some_string if word.isupper()]
# print(new_list)

# Создать список всех слов в предложении, содержащих более 3-х символов с использованием генератора списков.
# some_words = 'i like python very much. i can everything.'
# def list_words_lenght(some_text: str):
#     words = some_text.split()
#     new_list = []
#     for word in words:
#         if len(word) > 3:
#             new_list.append(word)
#     return new_list
# resalt =list_words_lenght(some_words)
# print(resalt)
# some_words = 'i like python very much. i can everything.'
# words = some_words.split()
# new_list = [word for word in words if len(word) > 3]
# print(new_list)

# Создать список всех чисел от 1 до 1000, которые делятся на 3 и 5 с использованием генератора списков.
#some_numbers = list(range(1, 1000))

# def list_numbers_divide(some_list: list):
#     list_out = []
#     for element in some_list:
#         if element % 3 ==0 and element % 5 ==0 :
#             list_out.append(element)
#     return list_out
# resalt = list_numbers_divide(some_numbers)
# print(resalt)

# resalt = [element for element in some_numbers if element % 3 == 0 and element % 5 == 0 ]
# print(resalt)

# Найти среднее значение списка чисел с использованием лямбда-функции.
#some_spisok = [2, 5, 14,  10]

# def avg_list(spisok: list):
#     summa = 0
#     for element in spisok:
#         summa += element
#         aver = summa / len(spisok)
#     return aver
# resalt = avg_list(some_spisok)
# print(resalt)

# resalt = lambda spisok: sum(some_spisok) / len(some_spisok)
# print(resalt(some_spisok))

# Проверить, есть ли в списке хотя бы одно отрицательное число с использованием лямбда-функции.
#some_spisok = [2, 5, 14, 10, -55]
# def check_negative_number(spisok_numbers: list):
#     for number in spisok_numbers:
#         if number < 0:
#             return False
#     return True
# resalt = check_negative_number(some_spisok)
# print(resalt)
#resalt = lambda spisok: all(number < 0 for number in spisok)
# print(resalt(some_spisok))

# Создать новый список, содержащий только уникальные элементы из исходного списка с использованием лямбда-функции.
# some_spisok = [2, 5, 14,  10, 10, 14]
# resalt_uniq_element = lambda element: set(element)
# print(resalt_uniq_element(some_spisok))

# Создать список всех чисел от 1 до 100, возведенных в квадрат, если число делится на 3 с использованием генератора списков.
#some_spisok = list(range(1, 101))
# def spisok_square_if_number_divide(spisok: list):
#     spisok_out = []
#     for number in spisok:
#         if number % 3 == 0:
#             spisok_out.append(number ** 2)
#     return spisok_out
# resalt = spisok_square_if_number_divide((some_spisok))
# print(resalt)
# resalt = [number ** 2 for number in some_spisok if number % 3 == 0]
# print(resalt)

# Создать список всех палиндромов в диапазоне от 1 до 1000 с использованием генератора списков.
#some_spisok = list(range(1, 1001))
# def palindrome(spisok: str):
#     list_out = []
#
#     for element in spisok:
#         element = str(element)
#
#         if element == element[::-1] and len(element) >= 2:
#             list_out.append(element)
#     return list_out
# resalt = palindrome(some_spisok)
# print(resalt)
# def palindrome(spisok: list):
#     list_out = [str(element) for element in  spisok if str(element) == str(element)[::-1] and len(str(element)) >= 2]
#     return list_out
# resalt = palindrome(some_spisok)
# print(resalt)

# Создать список всех уникальных символов в строке с использованием генератора списков.
#some_text = 'i like python and  i can everything.'
# def unique_symbols_in_string(some_string: str):
#     return list(set(some_string))
# resalt = unique_symbols_in_string(some_text)
# print(resalt)
# list_out = lambda text: [set(some_text)]
# print(list_out(some_text))

# Умножить каждый элемент списка на заданное число с использованием лямбда-функции.
#some_spisok = [2, 4, 6, 8, -10, -15]
# def multiply_number(spisok: list):
#     list_out = []
#     what_number_to_multiply = int(input('на какое число надо умножить? '))
#     for element in spisok:
#         if type(element) == int:
#             list_out.append(element * what_number_to_multiply)
#
#     return list_out
#
# resalt = multiply_number(some_spisok)
# print(resalt)

#what_number_to_multiply = int(input('на какое число надо умножить? '))
# resalt = [element * what_number_to_multiply for element in some_spisok]
# print(resalt)

# resalt = lambda spisok: [element * what_number_to_multiply for element in some_spisok]
# print(resalt(some_spisok))

# Проверить, является ли строка палиндромом с использованием лямбда-функции.
#some_text = 'i like python. we can everything.'

# def check_polindrom(text: str):
#     text = list(''.join(text))
#     for element in text:
#         if text != text [::-1]:
#             return False
#     return True
# resalt = check_polindrom(some_text)
# print(resalt)

# resalt_check = lambda text: ''.join(filter(str.isalnum, text.lower())) == ''.join(filter(str.isalnum, text.lower()))[::-1]
# print(resalt_check(some_text))

# Найти наибольшую длину строки в списке с использованием лямбда-функции.
#some_text = ['hello', 'world', 'python we like', 'list', 'string']
# def max_len_str(text:list):
#     maximum_lenght = 0
#     for element in text:
#         if maximum_lenght < len(element):
#             if maximum_lenght < len(element)
#     return maximum_lenght
# resalt = max_len_str(some_text)
# print(resalt)

# resalt = lambda text: max(len(element) for element in text)
# print(resalt(some_text))

# Создать список всех целых чисел от -10 до 10 с использованием генератора списков.
# list_out = lambda a,b: [number for number in range(a, b)]
# print(list_out(-10, 10))

# Посчитать сумму всех элементов матрицы с использованием лямбда-функции.
# some_matrix = [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]
# def sum_matrix(matrix: list):
#     summa = 0
#     for element in matrix:
#         for index in element:
#             summa += index
#     return summa
# resalt = sum_matrix(some_matrix)
# print(resalt)

# resalt = lambda matrix: sum(index for element in matrix for index in element)
# print(resalt(some_matrix))


# Удалить все пробелы из строки с использованием лямбда-функции.
#some_string = " 'i like python' , 'we can everything' "
# new = some_string.replace(' ', '')
# print(new)
# delete_space = lambda text_list: [''.join(letter for letter in text_list if letter != ' ')]
# resalt = delete_space(some_string)
# print(resalt)

# Проверить, являются ли все элементы строки числами с использованием лямбда-функции.
#some_text = " 'i like python' , 'we can everything' , 555"
#some_text = "55, 65, 75"
# def check_string_on_all_numbers(text: str):
#     text = text.split()
#     for element in text:
#         for char in element:
#             if char.isnumeric():
#                 break
#             return False
#     return True
# resalt = check_string_on_all_numbers(some_text)
# print(resalt)

# resalt = lambda text: all(char.isnumeric() for element in text for char in element )
# print(resalt(some_text))

# Создать список всех слов, начинающихся с гласной буквы в предложении с использованием генератора списков.
#some_text = " 'i like python. we like', 'ee like' "
# def begin_on_letter(text: str):
#     letter_begin = input('Введите букву, с которой должны начинаться слова: ').lower()
#     # Удаление кавычек из строки
#     text_without_quotes = text.replace("'", "")
#     words = text_without_quotes.split()
#     list_out = []
#     for word in words:
#         if word.strip().startswith(letter_begin):
#             list_out.append(word)
#     return list_out
#
# result = begin_on_letter(some_text)
# print(result)
#а вот это очень сложно
# begin_on_letter = lambda text, letter_begin, words: [word for word in words if word.strip().startswith(letter_begin)]
# letter_begin = input('Введите букву, с которой должны начинаться слова: ').lower()
# text_without_quotes = some_text.replace("'", "")
# words = text_without_quotes.split()
#
# result = begin_on_letter(some_text, letter_begin, words)
# print(result)

# Создать список всех четных чисел из списка чисел с использованием генератора списков.
# some_numbers = [4, 6, 15, 7, 21, 25, 14]
# list_out = [number for number in some_numbers if number % 2 == 0]
# print(list_out)

# Создать список всех элементов матрицы, находящихся на главной диагонали, с использованием генератора списков.
# some_numbers = [[2, 4, 6],
#                 [8, 10, 12],
#                 [14, 16, 18]]
# def sum_numbers_in_matrix_diagonal(numbers_list: list):
#     sum_diagonal = 0
#     for element in range(len(numbers_list)):
#         if element == element:
#                 sum_diagonal += numbers_list[element][element]
#     return sum_diagonal
# print(sum_numbers_in_matrix_diagonal(some_numbers))

# list_out = sum([ some_numbers[element][element] for element in range(len(some_numbers)) if element == element])
# print(list_out)

# Создайте лямбда-функцию, которая проверяет, является ли каждый элемент списка положительным.
#some_spisok = [4, 14, 15]
# def check_positive_list(some_numbers_list: list):
#     for number in some_numbers_list:
#         if number < 0:
#             return False
#     return True
# resalt = check_positive_list(some_spisok)
# print(resalt)

# resalt = lambda spisok: any(number > 0 for number in some_spisok)
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая удаляет все отрицательные числа из списка.
#some_spisok = [4, -14, -15]
# def delete_negative_number(some_numbers_list: list):
#     list_out = []
#     for number in some_numbers_list:
#         if number > 0:
#             list_out.append(number)
#     return list_out
# resalt = delete_negative_number(some_spisok)
# print(resalt)

# resalt = lambda spisok: [number for number in some_spisok if number > 0]
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только буквы.
#some_spisok = ['abc123', 'def', '456', 'ghi789', 'jkl', 'mno']
# def return_only_letters_string(spisok: list):
#     list_out = []
#     for element in spisok:
#         if  element.isalpha():
#             list_out.append(element)
#     return list_out
# resalt = return_only_letters_string(some_spisok)
# print(resalt)
# resalt = lambda spisok: [element for element in spisok if element.isalpha()]
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая проверяет, является ли строка длинной больше заданного значения.
# some_string = 'we can'
# resalt = lambda strings, lenght_number: ( (len(strings)) >= lenght_number  )
# print(resalt(some_string, 7))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только символы, отличные от букв и цифр
# some_spisok = ['abc123', 'def', '456', '///*****-', 'ghi789', 'jkl//.', 'mno', '///*-']
# def return_only_symbols_string(spisok: list):
#     list_out = []
#     for element in spisok:
#         if all(not letter.isalnum() for letter in element):
#             list_out.append(element)
#     return list_out
#
# resalt = return_only_symbols_string(some_spisok)
# print(resalt)
# resalt = lambda spisok: [element for element in spisok if all(not letter.isalnum() for letter in element)]
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только цифры.
#some_list = ['100', 'python', '150', '450']
# for element in some_list:
#     list_out = []
#     if element.isdigit():
#         list_out.append(element)
#         print(list_out)

# resalt = lambda spisok: [element for element in spisok if element.isdigit()]
# print(resalt(some_list))

# Создайте лямбда-функцию, которая возвращает список чисел, умноженных на 2, если они четные, и на 3, если они нечетные.
#some_numbers = [4, 6, 8, 3]
# list_out = []
# for element in some_numbers:
#     if element % 2 == 0:
#         element = element * 2
#         list_out.append(element)
#     if element % 2 != 0:
#         element = element * 3
#         list_out.append(element)
# print(list_out)

# resalt = lambda some_numbers: [element * 2 if element % 2 == 0 else element * 3 for element in some_numbers]
# print(resalt(some_numbers))

# Создайте лямбда-функцию, которая принимает список чисел и возвращает среднее арифметическое всех чисел.
# some_spisok = [2, 4, 6, 8]
# resalt = lambda spisok: sum(element for element in spisok)/ len(spisok)
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только слова с четным числом букв.
#some_spisok_strings = ['we like python', 'common', 'do not cry']
# def even_lenght_word(text: list):
#     list_out = []
#
#     for element in text:
#         words = element.split()
#         for word in words:
#             if len(word) % 2 == 0:
#                 list_out.append(word)
#     return list_out
# resalt = even_lenght_word(some_spisok_strings)
# print(resalt)

# resalt = lambda spisok: [word for element in spisok for word in element.split() if len(word) % 2 == 0]
# print(resalt(some_spisok_strings))

# Создайте лямбда-функцию, которая проверяет, является ли каждое слово в списке палиндромом.
# some_words = ['mam', 'lilil', 'kola', 'a', 't']
# resalt = lambda spisok: all(element == element[::-1] for element in spisok  )
# print(resalt(some_words))

# Создайте лямбда-функцию, которая возвращает список чисел, возведенных в заданную степень.
# some_spisok = [2, 4, 6, 10]
# resalt = lambda spisok, number: [element ** 2 for  element in spisok]
# print(resalt(some_spisok, 2))

# Создайте лямбда-функцию, которая возвращает список строк, в которых каждое слово состоит из одной буквы.
#some_words = ['mam', 'lilil', 'kola', 'a', 't', 'p']
# for element in some_words:
#     list_out = []
#     if len(element) == 1:
#         list_out.append(element)
#         print(list_out)
# resalt = lambda text: [element  for element in text if len(element) == 1]
# print(resalt(some_words))


# Создайте лямбда-функцию, которая возвращает список строк в верхнем регистре.
#some_spisok_strings = ['i like python', 'we can']
# for element in some_spisok_strings:
#     list_out = []
#     list_out.append(element.upper())
#     print(list_out)
# resalt = lambda string: [element.upper() for element in string ]
# print(resalt(some_spisok_strings))

# Создайте лямбда-функцию, которая проверяет, является ли строка числом.
#some_spisok_strings = ['i like python', 'we can']
# some_spisok = [4, 5]
# resalt = lambda spisok: all(type(element) == int for element in spisok)
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только числа.
# some_spisok_strings = ['i like python', 'we can', 55, 45]
# resalt = lambda spisok: [element for element in spisok if type(element) == int]
# print(resalt(some_spisok_strings))

# Создайте лямбда-функцию, которая объединяет два списка в кортежи, содержащие элементы с одинаковыми индексами.
# spisok1 = [1, 3, 4, 7]
# spisok2 = [2, 5, 8, 9]
# list_out = []
# for element, elem in zip(spisok1, spisok2):
#     list_out.append((element, elem))
# print(tuple(list_out))
#
# resalt = lambda sp1, sp2: tuple((element, elem) for element, elem in zip(sp1, sp2))
# print(resalt(spisok1, spisok2))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только символы, являющиеся согласными буквами.
# some_text = ['we can', 'i can', 'we do', 'i do', 'you']
# vowels_letters = ['a', 'o', 'u', 'e', 'y', 'i']
# list_out = []
# for element in some_text:
#     for let in element:
#         for letter in vowels_letters:
#             if let == letter:
#                 list_out.append(let)
# print(list_out)

# resalt = lambda some_text, vowels_letters: [let for element in some_text for let in element if let.lower() in vowels_letters]
# print(resalt(some_text, vowels_letters))

# Создайте лямбда-функцию, которая приводит все строки в списке к нижнему регистру и удаляет пробел
#some_text = ['we can', 'i CAN', 'we do', 'I do', 'YOU']
# some_text = ['WE can do everything',  'we do']
# list_out = []
# for phrases in some_text:
#     phrases_new = phrases.replace(' ', '')
#     list_out.append(phrases_new.lower())
# print(list_out)

# resalt = lambda text: [phrases.replace(' ', '').lower() for phrases in text]
# print(resalt(some_text))

#Создайте лямбда-функцию, которая возвращает список строк, в которых каждое слово начинается с заглавной буквы.
#some_text = ['we can', 'i CAN', 'we do', 'I do', 'YOU']
# list_out = []
# for phrases in some_text:
#     words_list = phrases.lower().split()
#     for words in words_list:
#         list_out.append(words.capitalize())
# print(list_out)
# пока что запись этой лямбды слишком сложно. но и задача не проста
# resalt = lambda text: [' '.join([word.capitalize() for word in phrase.lower().split()]) for phrase in text]
# print(resalt(some_text))
# Создайте лямбда-функцию, которая проверяет, являются ли все строки в списке палиндромами.
# text = ['lisa', 'mimim', 'ili imi']
# resalt = lambda spisok: all(element == element[::-1] for element in spisok)
# print(resalt(text))

# Создайте лямбда-функцию, которая возвращает список строк, содержащих только уникальные символы.
#some_spisok = ["madam", "red", "blue", "level", "green"]
# list_out = []
# for element in some_spisok:
#
#     words = element.split()
#     for word in words:
#         if len(word) == len(set(word)):
#             list_out.append(words)
# print(list_out)
# слишком сложно осознать
# resalt = lambda text: [word for element in text for word in element.split() if len(word) == len(set(word))]
# print(resalt(some_spisok))

# Создайте лямбда-функцию, которая возвращает список строк в обратном порядке.
# some_text = ['i like python', 'we can learn']
# resalt = lambda spisok: [spisok[::-1]]
# print(resalt(some_text))
