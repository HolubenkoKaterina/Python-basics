# Напишите функцию, которая возвращает другую функцию, возводящую число в заданную степень.
# def num_multiplace(number_to_multiplace):
#     def do_multiplace(stepen_for_number):
#         return number_to_multiplace ** stepen_for_number
#     return do_multiplace
# stepen_for_number = int(input('какая степень числа будет? '))
# resalt = num_multiplace(2)
# print(resalt(stepen_for_number))
###################################################################################################3
# Создайте функцию-счетчик, которая при каждом вызове увеличивает своё значение на единицу.
# def get_resalt_counter():
#     counter = 0
#     def counter_func():
#         nonlocal counter
#         counter += 1
#         return counter
#     return counter_func
# resalt = get_resalt_counter()
# print(resalt())
# print(resalt())
# print(resalt())
############################################################################################33
# Реализуйте функцию-генератор последовательности Фибоначчи, используя замыкания.
# def get_fibonaci_list():
#     def fibonacci_func(num: int):
#         if num <= 1:
#             return []
#         if num == 1:
#             return [1]
#         if num == 2:
#             return [1, 2]
#
#         fibonacci_list = [1, 2]
#         for i in range(2, num):
#             next_fibonacci = fibonacci_list[i - 1] + fibonacci_list[i - 2]
#             fibonacci_list.append(next_fibonacci)
#
#         return fibonacci_list
#
#     return fibonacci_func
#
# number_for_fibonacci = int(input('Введите, сколько чисел Фибоначчи нужно вывести: '))
# resalt = get_fibonaci_list()
# print(resalt(number_for_fibonacci))
#########################################################################################################333
# # Напишите функцию, которая принимает на вход массив чисел и возвращает функцию, вычисляющую среднее арифметическое этих чисел.
# spisok_numbers = [2, 3, 5, 4, 1]
# def get_aver():
#     def average_numbers(some_numbers):
#         suma = 0
#         lenght = len(some_numbers)
#         for num in some_numbers:
#             suma += num
#         aver = suma / lenght
#         return aver
#     return average_numbers
# resalt = get_aver()
# print(resalt(spisok_numbers))
#################################################################################################
# Создайте функцию, которая проверяет, является ли заданное слово палиндромом.
# def answer_palindrom():
#     def check_palindrom(some_word):
#
#         if word == word[::-1]:
#             return 'да, это слово палиндромом!'
#         else:
#             return 'нет, это не палиндромом!'
#     return check_palindrom
# word = input('какое слово вы хотите проверить?...')
# resalt = answer_palindrom()
# print(resalt(word))
#######################################################################################################
# Реализуйте функцию, принимающую на вход функцию и возвращающую новую функцию, которая при каждом
# вызове сначала выводит "Начало выполнения", затем вызывает переданную функцию и в конце выводит "Завершение выполнения".
# def start():
#     def finish():
#         print('начало выполнения')
#         print('Завершение выполнения')
#     return finish
#
# resalt = start()
# print(resalt())
###############################################################################################################3
# Напишите функцию, которая принимает на вход массив строк и возвращает новый массив, содержащий только уникальные строки.
# string_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
# def get_uniq():
#     def uniq_elements(some_list):
#
#            list_out = set(some_list)
#            return list(list_out)
#     return uniq_elements
#
# resalt = get_uniq()
# print(resalt(string_list))
########################################################################################################################
# Создайте функцию, которая генерирует случайный пароль заданной длины и набора символов.
# import random
# import string
#
# def get_parol(length: int):
#     def make_parol():
#         parol_element = string.digits + string.ascii_letters + string.punctuation
#         parol = ''.join(random.choice(parol_element) for _ in range(length))
#         return parol
#     return make_parol
#
# length_parol = int(input('Введите длину пароля: '))
# resalt = get_parol(length_parol)
# print(resalt())
# print(resalt())
# print(resalt())
########################################################################################################
# Реализуйте функцию, которая преобразует строку в формате "Имя Фамилия" в формат "Фамилия, Имя".
# def get_info_person(some_info: str):
#     def change_2name_1name():
#         nonlocal some_info
#         names = some_info.split()
#         if len(names) == 2:
#             return names[1], names[0]
#         else:
#             print('неправильный формат..')
#
#     return change_2name_1name
# info = input('введите имя и фамилию..')
# resalt = get_info_person(info)
# print(resalt())
##########################################################################################################
# Напишите функцию, которая принимает на вход число и возвращает функцию, проверяющую, является ли заданное число простым.
# def get_check_number(num: int):
#     def check_number_for_simple():
#         if num <= 1:
#             return False
#         if num <= 3:
#             return True
#         if num % 2 == 0 or num % 3 == 0:
#             return False
#         i = 5
#         while i * i <= num:
#             if num % i == 0 or num % (i + 2) == 0:
#                 return False
#             i += 6
#         return True
#     return check_number_for_simple
#
# number_to_check = int(input('Введите ваше число: '))
# resalt = get_check_number(number_to_check)
# print(resalt())
