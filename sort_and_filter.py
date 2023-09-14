# Отфильтровать имена, начинающиеся с определенной буквы, из списка имен.
#names_list = ["Alice", "Bob", "Eve", "David", "Charlie", 'chloe']
# list_out = names_list.copy()
# for name in list_out:
#     for letter in name:
#         list_out.sort()
# print(list_out)

# sorting_list = sorted([letter for letter in names_list])
# print(sorting_list)

# Извлечь из списка только числа, находящиеся в определенном диапазоне.
#some_spisok = [2, 3, 4, 5, 6, 8, 9]
# def get_numbers_in_range(*args, start: int, finish: int):
#     list_out = []
#     args = sorted(args)
#     for element in args:
#         if start <= element < finish:
#             list_out.append(element)
#     return list_out
# resalt = get_numbers_in_range(*some_spisok, start=4, finish=16)
# print(resalt)

# def get_numbers_in_range(*args, start: int, finish: int):
#     args = sorted(args)
#     list_out = [element for element in args if start <= element < finish]
#     return list_out
# resalt = get_numbers_in_range(*some_spisok, start=4, finish=16)
# print(resalt)

# Фильтрация слов из списка на основе их длины (например, все слова длиной менее 5 символов).
# some_spisok =[ 'we' , 'like',  'python', 'we' ,'did', 'it', 'hello', 'morning', 'sidr']
# def filter_words_for_lenght(*args, lenght: int):
#
#     resalt = [words for words in args if len(words) > lenght]
#     return resalt
# resalt = filter_words_for_lenght(*some_spisok, lenght=5)
# print(resalt)

# Отфильтровать отрицательные числа из списка.
# some_spisok = [-16, -25, 0, 15, 28]
# def filter_spisok_for_negative_numbers(*args):
#     spisok_out = [number for number in args if  number > 0 ]
#     return spisok_out
# resalt = filter_spisok_for_negative_numbers(*some_spisok)
# print(resalt)

# Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). С помощью list comprehension преобразовать
# двумерный список в одномерный так, чтобы значения элементов шли в обратном порядке.
# Результат отобразить в виде строки из чисел, записанных через пробел.
# some_list = [[1, 2, 3, 4],
#              [5, 6, 7, 8],
#              [9, 8, 7, 6],
#              [5, 4, 3, 2]
#              ]
# def union_numbers_in_list_In_reverse(*args):
#     list_out = []
#     for element in args:
#         for number in element:
#             number = reversed(element)
#             list_out = [number for element in reversed(args) for number in reversed(element)]
#     return list_out
# resalt = union_numbers_in_list_In_reverse(*some_list)
# print(resalt)

# some_list = [[1, 2, 3, 4],
#              [5, 6, 7, 8],
#              [9, 8, 7, 6],
#              [5, 4, 3, 2]
#              ]
#
# def union_numbers_in_list_In_reverse(*args):
#     list_out = []
#     for element in reversed(args):
#         for number in reversed(element):
#             list_out.append(str(number))
#     return ' '.join(list_out)
#
# result = union_numbers_in_list_In_reverse(*some_list)
# print(result)

# Извлечь из списка только строки, состоящие из заглавных букв.
# some_spisok = [, 'like',  'P', 'We'ython', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def get_strings_upper_letter(args):
#     list_out = [element for element in args if element.istitle()]
#     return list_out
#
# result = get_strings_upper_letter(some_spisok)
# print(result)

#  Фильтрация элементов списка, которые удовлетворяют определенному условию (например, числа, кратные 3).
# some_numbers = [16, 3, 13, 27, 21]
# def number_multiplicity( mumb_multiplicity: int, *args):
#     resalt = [numb for  numb in args if numb % mumb_multiplicity ==0]
#     return resalt
# resalt = number_multiplicity(*some_numbers, mumb_multiplicity=3)
# print(resalt)

# Отфильтровать элементы списка, которые являются объектами определенного класса.
# some_numbers = [16, 3, 'python', 13, 27, '21', [26, 14]]
# def get_some_class(what_clas, *args):
#     list_out = [element for element in args if type(element) == what_clas]
#     return list_out
# resalt = get_some_class( str, *some_numbers)
# print(resalt)

# Извлечь из списка только строки, содержащие только цифры.
# mixed_list = ['apple', '123', 'banana', '456', 'cherry', 'hello', '789', 55]
# def get_numbers(*args):
#     list_out = [elem for elem in args if type(elem) == int or elem.isdigit()]
#     return list_out
# resalt = get_numbers(*mixed_list)
# print(resalt)

# Фильтрация дубликатов из списка элементов.
# some_list = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
# def filter_duplicate(*args):
#     duplicate = [elem for elem in args if args.count(elem) > 1]
#     return list(set(duplicate))
# resalt = filter_duplicate(*some_list)
# print(resalt)

# Отфильтровать элементы списка, которые начинаются с гласной буквы.
# some_list = ['idol', 'we', 'like', 'python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def begin_letter(letter, *args):
#
#     list_out = [elem for elem in args if elem[0] == letter]
#     return list_out
# resalt = begin_letter('i', *some_list)
# print(resalt)

# def begin_letter(letter, *args):
#
#     list_out = filter(lambda elem: elem[0] == letter,  args)
#     return list(list_out)
# resalt = begin_letter('i', *some_list)
# print(resalt)

# Извлечь из списка только элементы с нечетными индексами.
#some_list = ['idol', 'we', 'like', 'python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def get_odd_element_index(*args):
#     list_out = [elem for index, elem in enumerate(args) if index % 2 != 0]
#     return list_out
# resalt = get_odd_element_index(*some_list)
# print(resalt)

# Фильтрация элементов списка, которые являются палиндромами.
# some_list = ['idol', 'we', 'like', 'python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def check_pallindrom(*args):
#     list_out = [elem for elem in args if elem[::1] == elem[::-1]]
#     return list_out
# resalt = check_pallindrom(*some_list)
# print(resalt)

# some_list = ['idol', 'we', 'like', 'python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def is_palindrome(word):
#     return word == word[::-1]
#
# def check_palindrome(*args):
#     palindromes = filter(is_palindrome, args)
#     return list(palindromes)
# resalt = check_palindrome(*some_list)
# print(resalt)

# Используйте следующий список из строк:

t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!"
    ]
# Необходимо преобразовать его в двумерный (вложенный) список lst, где каждая строка представляется
# списком из слов (слова разделяются пробелом), но сохранять слова только длиной более трех символов.
# Решить данную задачу с использованием list comprehension. Результат отобразить с помощью команды:
# def get_words_some_length(length_input, *args):
#     list_out = []
#     for words in args:
#         word = words.split()
#         filtered_words = [letter for letter in word if len(letter) > length_input]
#         if filtered_words:
#             list_out.append(filtered_words)
#     return list_out
#
# result = get_words_some_length(5, *t)
# print(result)

# # Отфильтровать строки, состоящие только из пробелов, из списка строк.
# some_list = ['python', '   ', 'programming', '  ', '  hello']
# def get_str_without_gap(*arg):
#     list_out = [elem for elem in arg if not elem.isspace()]
#     return list_out
# resalt = get_str_without_gap(*some_list)
# print(resalt)

# Извлечь из списка только элементы, которые являются числами с плавающей запятой.
# some_list = ['python', 3.14, 15, 28, '58', 5.0]
# def get_element_float(*args):
#
#     list_out = [elem for elem in args if type(elem) == float]
#     return list_out
# resalt = get_element_float(*some_list)
# print(resalt)

# Фильтрация элементов списка, которые содержат определенный символ.
# some_spisok = ['like',  'P', 'We', 'python', 'we', 'did', 'it', 'hello', 'morning', 'sidr']
# def filter_element_include_symbol(symbol, *args):
#     list_out = [elem for elem in args if symbol.lower() in elem]
#     return list_out
# resalt = filter_element_include_symbol('i', *some_spisok)
# print(resalt)

# Отфильтровать элементы списка, которые являются списками определенной длины.
# some_list = [1, [2, 3], [4, 5, 6], 'hello', [7, 8], [9, 10, 11]]
# def filter_list_for_lenght(lenght, *args):
#     list_out = [element for element in args if type(element) == list and len(element) >= lenght]
#     return list_out
# resalt = filter_list_for_lenght(1, *some_list)
# print(resalt)

#  На вход поступает таблица целых чисел, на выходе нужно отобразить эту же таблицу в транспонированном виде
#  (строки заменяются на столбцы), используя команду:
#
# for row in A:
#     print(*row)
# где A - транспонированный двумерный список. Желательно сделать эту задачу не пересматривая видео
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# def change_matrix(some_list: list):
#     rows = len(matrix)
#     columns = len(matrix[0])
#     transposed_matrix = []
#     for elem in range(columns):
#         transposed_row = []
#         for element in range(rows):
#             transposed_row.append(matrix[element][elem])
#         transposed_matrix.append(transposed_row)
#
#     return transposed_matrix
# resalt = change_matrix(matrix)
# print(resalt)

