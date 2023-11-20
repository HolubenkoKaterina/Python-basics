# Задача: Обработка списка чисел
# Напишите функцию process_numbers, которая принимает на вход в список целых чисел и выполняет следующую операцию:
# Умножает каждый элемент таблицы на 2.
# Возвращает новый список, содержащий только те элементы, которые являются четными числами.
# import random
# numbers = random.sample(range(1, 99), random.randint(1, 10))
# print(numbers)
# def process_and_filter_numbers(numbers: list):
#     list_double = [num * 2 for num in numbers]
#     list_out = list(filter(lambda num: num % 2 == 0, list_double))
#     return list_out
# print(process_and_filter_numbers(numbers))

# Попробуйте реализовать функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только уникальные элементы
# из исходного списка, сохраненные в том же порядке, в котором они встречаются в исходном списке.
# numbers = [4, 2, 8, 1, 5, 3, 8, 7, 2, 6, 4, 9, 1, 3, 5]
# def get_uniq_elements(some_list: list):
#     list_out = []
#     for elem in some_list:
#         if elem not in list_out:
#             list_out.append(elem)
#     return list_out
# print(numbers)
# # print(get_uniq_elements(numbers))

# Напишите функцию merge_lists(list1, list2), которая
# принимает два списка и возвращает новый список, состоящий из элементов обоих списков без повторений.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# def merge_lists(lst_1, lst_2):
#     list_out = []
#     for elem in lst_1:
#         for el in lst_2:
#             if elem not in list_out and el not in list_out:
#                 list_out.append(elem)
#             if el not in list_out:
#                 list_out.append(el)
#     return list_out
# print(merge_lists(list1,list2))

# Напишите функцию count_even(lst), которая принимает список целых чисел lst и возвращает количество четных чисел в этом списке.
# import random
# numbers = random.sample(range(1, 99), random.randint(1, 20))
# print(numbers)
# list_out = len(list(filter(lambda elem: elem % 2 == 0, numbers)))
# print(list_out)

# Напишите функцию count_frequency, которая принимает список чисел и возвращает словарь,
# в котором ключами являются уникальные элементы списка, а значениями — количество их появлений в списке.
# numbers = [1, 2, 3, 2, 4, 1, 5, 3, 1, 4, 2, 2, 5]
# def count_frequency(some_list: list):
#     dict_out = {}
#     for num in some_list:
#         if num not in dict_out:
#             dict_out[num] = 1
#         else:
#             dict_out[num] += 1
#     return dict_out
# print(count_frequency(numbers))

# Напишите функцию sort_by_frequency(some_list: list), которая принимает список и возвращает новый список,
# отсортированный по частоте встречаемости элементов в убывающем порядке.
# То есть, элементы, которые встречаются чаще, должны идти в начале списка.
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# print(numbers)
# def sort_by_frequency(some_list: list):
#     list_out = list(sorted(numbers, key=lambda elem: some_list.count(elem), reverse=True))
#     return list_out
# print(sort_by_frequency(numbers))

# у вас есть список чисел, и вы хотите получить новый список,
# содержащий только уникальные числа, которые встречаются четное количество раз.
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# print(numbers)
# def even_frequency_numbers(some_list: list):
#     list_out = [elem for elem in some_list if some_list.count(elem) % 2 == 0]
#     return set(list_out)
# print(even_frequency_numbers(numbers))

# Напишите функцию merge_lists, которая принимает два отсортированных списка
# и возвращает новый отсортированный список, содержащий все элементы из обоих списков.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# list_out = list1 + list2
# print(sorted(list_out, key=lambda elem: elem))

# Напишите функцию calculate_average, которая принимает список чисел и
# возвращает среднее значение этих чисел. Округлите результат до двух знаков после запятой.
# numbers = [2, 5, 8, 11, 14, 58]
# def calculate_average(some_numb: list):
#     summa = sum(some_numb)
#     aver = round(summa / len(some_numb), 2)
#     return aver
# print(calculate_average(numbers))

# Напишите функцию is_palindrome, которая принимает целое число и возвращает True, если число является палиндромом,
# и False в противном случае. Палиндром - это число, которое читается одинаково слева направо и справа налево.
# def is_palindrome(num: int):
#
#     if num < 10:
#         return True
#     elif str(num)[0] == str(num)[-1]:
#         return True
#     else:
#
#         return False
# print(is_palindrome(141))

# Напишите функцию add_matrices(mat1, mat2), которая принимает две матрицы в виде списков списков и возвращает
# новую матрицу, являющуюся результатом сложения входных матриц. Предполагается, что обе матрицы имеют одинаковый размер.
# mat1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# mat2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
# def add_matrices(mat1: list, mat2: list):
#     mat_out = []
#     summa = 0
#     for i in range(len(mat1)):
#         row = []
#         for j in range(len(mat2[0])):
#             summa = mat1[i][j] + mat2[i][j]
#             row.append(summa)
#         mat_out.append(row)
#     return mat_out
# print(add_matrices(mat1, mat2))




# Напишите функцию count_vowels_and_consonants, которая принимает строку и возвращает
# кортеж с количеством гласных и согласных букв в этой строке (регистр букв не имеет значения).
# import string
# text = 'i practice python tasks with CHAT GPT! '
# translator = str.maketrans('', '', string.punctuation)
# text_new = text.translate(translator)
# print(text_new)
# def count_vowels_and_consonants(stroka: str):
#     vowels = 0
#     consonants = 0
#     for letters in stroka.lower():
#         if letters in 'aeouiy'.lower():
#             vowels += 1
#         else:
#             consonants += 1
#     return f'({vowels}, {consonants})'
# print(count_vowels_and_consonants(text_new))

# Напишите функцию add_matrices(mat1, mat2), которая принимает две матрицы
# (представленные в виде списка списков) одинакового размера и возвращает новую матрицу, являющуюся их суммой.
# mat1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# mat2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
# def add_matrices(mat1: list, mat2: list):
#     if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
#         raise ValueError("Размеры матриц не совпадают")
#
#     result_matrix = []
#
#     for i in range(len(mat1)):
#         row = []
#         for j in range(len(mat1[0])):
#             summa = mat1[i][j] + mat2[i][j]
#             row.append(summa)
#         result_matrix.append(row)
#     return result_matrix
# print(add_matrices(mat1, mat2))


"""
    Функция принимает матрицу и возвращает её транспонированный вариант.
    Транспонирование матрицы — это операция, при которой строки матрицы становятся столбцами, и наоборот.

    Пример:
    transpose_matrix([[1, 2, 3]
                    , [4, 5, 6]])
    Возвращает:
    [[1, 4],
     [2, 5],
     [3, 6]]
    """

# def transpose_matrix(matrix):
#     m_out = []  # Список для хранения транспонированной матрицы
#     for index in range(len(matrix[0])):  # Перебираем индексы столбцов
#         row = []  # Создаем пустой список для текущего столбца
#         for elem in matrix:  # Перебираем строки матрицы
#             row.append(elem[index])  # Добавляем элемент из текущего столбца
#         m_out.append(row)  # Добавляем текущий столбец в результат
#     return m_out
#
# matrix = [[1, 2, 3], [4, 5, 6]]
# result = transpose_matrix(matrix)
# print(result)

# Напишите функцию split_list, которая принимает на вход список чисел и разделяет его на два списка.
# Первый список должен содержать только четные числа из
# исходного списка, а второй - только нечетные числа. Функция должна возвращать кортеж из двух списков.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def split_list(numbers: list):
#     odd = []
#     no_odd = []
#     list_out = []
#     for elem in numbers:
#         if elem % 2 == 0:
#             odd.append(elem)
#         else:
#             no_odd.append(elem)
#         list_out = (odd, no_odd)
#     return list_out
# print(split_list(numbers))

# Найти сумму четных чисел в списке.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# summa = sum([num for num in numbers if num % 2 == 0])
# print(summa)

# Рассмотрим задачу на вложенные списки, представленные в виде матрицы.
# Допустим, у нас есть матрица, представляющая таблицу оценок студентов:
# grades = [
#     [95, 87, 91],
#     [88, 76, 90],
#     [92, 89, 78]
# ]
# def average_grades(matrix: list):
#     averages = []
#     for stud in matrix:
#         summa = 0
#         for grade in stud:
#             summa += grade
#         aver = summa / len(stud)
#         averages.append(aver)
#
#     return averages
# result = average_grades(grades)
# print(result)

# есть список студентов, каждый из которых представлен в
# # виде вложенного списка. Каждый вложенный список содержит имя студента (строка) и его средний балл (число).
# написать функцию sort_students, которая принимает список студентов и
# возвращает новый список студентов, отсортированный по среднему баллу в убывающем порядке.
# students = [
#     ["Alice", 85],
#     ["Bob", 90],
#     ["Charlie", 78],
#     ["David", 92],
#     ["Emily", 88]
# ]
# def sort_students(students: list):
#     out = sorted(students, key=lambda elem: elem[1], reverse=True)
#     return out
# print(sort_students(students))

# написать функцию transpose_matrix, которая
# принимает матрицу (список списков) и возвращает транспонированную матрицу.
# Транспонирование матрицы - это операция, при которой строки становятся столбцами, а столбцы - строками.
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# def transpose_matrix(matrix: list):
#     transposed_matrix = []
#     for i in range(len(matrix)):
#         row = []
#         for j in range(len(matrix)):
#             row.append(matrix[j][i])
#         transposed_matrix.append(row)
#     return transposed_matrix
# print(matrix)
# print(transpose_matrix(matrix))

# 0 0  0 1
# 1 0  1 1
# 2 0  2 1
