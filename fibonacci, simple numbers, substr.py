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
######################################################################3
# генератор чисел Фибоначчи
# def get_fibonacci_generator(number):
#     a, b = 0, 1
#     for _ in range(number):
#         yield b
#         a, b = b, a + b
#
# number = int(input('Введите количество чисел Фибоначчи: '))
# fibonacci_generator = get_fibonacci_generator(number)
#
# for num in fibonacci_generator:
#     print(num)
#################################################################################
# Реализуйте функцию, которая принимает число и возвращает функцию для проверки, является ли оно числом Фибоначчи.
# def wrapper():
#     fibonacci_list = [1, 2]
#
#     def check_fibonacci(number):
#         if number in fibonacci_list:
#             return True
#         while fibonacci_list[-1] < number:
#             next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
#             fibonacci_list.append(next_fibonacci)
#             if next_fibonacci == number:
#                 return True
#         return False
#
#     return check_fibonacci
#
#
# number_to_check = int(input('Enter a number: '))
# resalt = wrapper()
# print(resalt(number_to_check))
###########################################################################################3
# numbers_add = [int(num) for num in input('Введите ваши числа через запятую: ').replace(',', '').split()]

#Напишите функцию для разбиения строки на подстроки заданной длины.
# text = 'i like PYTHON so much python my LOVE'
# def make_substr(some_text: str, lenght_substr: int):
#     some_sudstr = []
#     for elem in range(0, len(some_text), lenght_substr):
#         some_substring = some_text[elem:elem + lenght_substr]
#         some_sudstr.append(some_substring)
#
#     return some_sudstr
# resalt = make_substr(text,lenght_substr=3)
# print(resalt)
