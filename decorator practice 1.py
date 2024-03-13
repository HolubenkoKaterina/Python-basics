# Создайте декоратор, который проверяет, что переданное значение аргумента положительное.
'''#def decorator(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, (list, tuple)):
#                 for num in arg:
#                     if isinstance(num, int) and num < 0:
#                         raise ValueError('Negative value detected in the argument.')
#             else:
#                 raise ValueError('Argument is not a list or tuple.')
#         return func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def summa(*args):
#     total_sum = 0
#     for arg in args:
#         if isinstance(arg, (list, tuple)):
#             for el in arg:
#                 if isinstance(el, int):
#                     total_sum += el
#                 if isinstance(el, str):
#                     if el.isdigit():
#                         total_sum += int(el)
#     return total_sum
#
# data2 = ('10', '10', -105)
# result = summa(data2)
# print(result)'''
# Создайте декоратор, который проверяет, что переданный аргумент - строка.
'''# def decorator(func):
#     def wrapper(*args, **kwargs):
#
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise ValueError('не тот тип данных!')
#
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# def summa(numbers):
#     total_sum = 0
#     for num in numbers:
#         total_sum += num
#     return total_sum
# data = [2, 4, '5']
# resalt = summa(data)
# print(resalt)'''
# Создайте декоратор, который проверяет, что переданный аргумент - число.
'''# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if not isinstance(args[0], int):
#             raise ValueError('не тот тип данных!')
#
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# def check(number):
#     if number > 0:
#         return ('+')
#     if number < 0:
#         return('-')
#     if number == 0:
#         return('0!')
# number = 5
# resalt = check(number)
# print(resalt)'''
