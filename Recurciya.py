# Вывод чисел от 1 до N: Напишите рекурсивную функцию для вывода всех целых чисел от 1 до N.
# def print_numbers(n):
#     if n >= 1:
#         print(n)
#         print_numbers(n - 1)
# res = print_numbers(5)
# print(res)

# Расчет факториала: Напишите функцию, которая вычисляет факториал заданного положительного целого числа с использованием рекурсии.
# def factorial(n):
#     if n == 1:
#        return 1
#     else:
#         return n * factorial(n - 1)
# res = factorial(5)
# print(res)

# Определение четности числа: Напишите рекурсивную функцию, которая определяет, является ли заданное целое число четным или нечетным.
# def check_odd(n):
#     if n == 0:
#         return True
#     if n == 1:
#         return False
#     else:
#         return check_odd(n - 2)
# res = check_odd(16)
# print(res)

# Сумма чисел от 1 до N: Напишите функцию, которая вычисляет сумму всех целых чисел от 1 до N с использованием рекурсии.
# def summa_numbers(n):
#     if n ==1:
#         return 1
#     else:
#         return n + summa_numbers(n - 1)
# res = summa_numbers(5)
# print(res)

# Вывод строки в обратном порядке: Напишите функцию, которая выводит символы в строке в обратном порядке с использованием рекурсии.
# my_str = 'love'
# def reverse_string(some_str: str, ind=0):
#     if len(some_str) == ind:
#         return ''
#     else:
#         return reverse_string(some_str, ind+1) + some_str[ind]
# res = reverse_string(my_str)
# print(res)