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
# Создайте декоратор, который повторяет выполнение функции заданное количество раз и выводит среднее время выполнения.
'''# import time
#
# def decorator(n):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             total_execution_time = 0
#
#             for _ in range(n):
#                 start = time.time()
#                 result = func(*args, **kwargs)
#                 finish = time.time()
#                 execution_time = finish - start
#                 total_execution_time += execution_time
#
#                 #print(f"Время выполнения {func.__name__}: {execution_time:.6f} секунд")
#
#             average_execution_time = total_execution_time / n
#             print(f"Среднее время выполнения {func.__name__}: {average_execution_time:.6f} секунд")
#
#             return result
#
#         return wrapper
#     return decorator_inner
#
# @decorator(n=5)
# def summa(a, b):
#     return a + b
#
# result = summa(4, 10)
# print(result)'''
# Создайте декоратор, который заменяет все гласные буквы в результате выполнения функции на '*'.
'''#def decorator(letter):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
# 
#             if isinstance(result, str):
#                 result = result.lower()
#                 result = result.replace(letter, '*')
#             else:
#                 raise ValueError('не тот тип данных')
#             return result
# 
#         return wrapper
# 
#     return decorator_inner
# 
# 
# @decorator(letter='l')
# def text(some_text: str):
#     return some_text
# 
# 
# data = ['i like python']
# result = text(data)
# print(result)'''
# Создайте декоратор, который записывает результат выполнения функции в файл.
'''# def derorator_log(file_name):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             resalt = func(*args, **kwargs)
#             with open(file_name, 'w', encoding='utf-8') as log_file:
#                 log_file.write(f"Результат выполнения функции {func.__name__}({args}, {kwargs}) = {resalt}\n")
#             return resalt
#         return wrapper
#     return decorator_inner
# @derorator_log(file_name='file_log.log')
# def plus(a, b):
#     return a + b
# resalt = plus(5, 10)
# print(resalt)'''
# # Создайте декоратор, который делает первую букву результата выполнения функции заглавной.
'''# def decorator(func):
#     def wrapper(*args, **kwargs):
#         resalt = func(*args, **kwargs)
#         if isinstance(resalt, str):
#             return resalt.title()
#         else:
#             raise ValueError('не тот тип данных!')
#     return wrapper
# @decorator
# def change_text(some_text: str):
#     resalt = [word.lower() for word in some_text.split()]
#     return ' '.join(resalt)
# text = 'I LIKE PYTHON'
# resalt = change_text(text)
# print(resalt)'''