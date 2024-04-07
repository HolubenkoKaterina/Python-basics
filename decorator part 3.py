# Напишите декоратор, который принимает параметр "retry_exceptions" и повторяет выполнение функции только в случае определенных исключений.
'''# def retry_decorator(retry_exceptions):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             retries = 3
#             while retries > 0:
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except retry_exceptions as e:
#                     print(f"An exception occurred: {e}. Retrying...")
#                     retries -= 1
#             raise Exception("Max retries reached. Function failed.")
#         return wrapper
#     return decorator
#
# def divide_by_zero():
#     return 10 / 0
#
# @retry_decorator((ZeroDivisionError,))
# def safe_divide_by_zero():
#     return divide_by_zero()
#
# result = safe_divide_by_zero()
# print(result)
'''
#Создайте декоратор, который принимает параметр "valid_values" и проверяет, что возвращаемое значение функции находится
# в списке допустимых значений.
'''# def decorator(valid_values):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             resalt = func(*args, **kwargs)
#             if resalt not in valid_values:
#                 raise ValueError('значение превышает допустимый диапазон!')
# 
#             return resalt
#         return wrapper
#     return decorator_inner
# @decorator(valid_values=range(10, 20))
# def summa(*args):
#     summa = 0
#     for arg in args:
#         for ele in arg:
#             if isinstance(ele, int):
#                 summa += ele
#     return summa
# lisat_num = [5, 4]
# resalt = summa(lisat_num)
# print(resalt)'''
# Создайте декоратор, который оборачивает результат выполнения функции в HTML-тег.
'''# def html_wrapper(func):
#     def wrapper(*args, **kwargs):
#         resalt = func(*args, **kwargs)
#         html_result = f"<html>{resalt}</html>"
#         return html_result
#     return wrapper
# 
# @html_wrapper
# def greet(name):
#     return f"<h1>Hello, {name}!</h1>"
# name_in = input('name? ')
# resalt = greet(name_in)
# print(resalt)'''