# Напишите декоратор, который принимает параметр "delay" и задерживает выполнение функции на указанное количество секунд.
'''# import time
#
# def decorator(delay):
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             time.sleep(delay)
#             return result
#         return wrapper
#     return actual_decorator
#
# @decorator(delay=2)
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
# data = [4, 6, '5']
# data2 = ('10', '10', 15)
# result = summa(data, data2)
# print(result)'''
# Создайте декоратор, который принимает параметр "n" и выполняет функцию "n" раз.
'''# def decorator(n):
#
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             total_result = 0
#
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#                 total_result += result
#             return total_result
#
#         return wrapper
#     return actual_decorator
#
# @decorator(n=3)
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
#
# data2 = ('10', '10', 15)
# result = summa(data2)
# print(result)'''