# Создайте декоратор, который принимает параметр "max_duration" и выводит предупреждение, если функция выполняется дольше указанного времени.
'''# import time
# def decorator(max_duration):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             start = time.time()
#             resalt = func(*args, **kwargs)
#             finish = time.time()
#             dif = finish - start
#             if dif > max_duration:
#                 print(f'функция {func.__name__ } выполняется больше времени чем указано как {max_duration}')
#         return inner
#     return wrapper
# @decorator(max_duration=2)
# def long_running_function():
#      time.sleep(3)
#      print("Функция завершена")
# resalt = long_running_function()
# print(resalt)'''
# Напишите декоратор, который принимает параметр "threshold" и выполняет функцию только если переданный аргумент больше этого порога.
'''#def decorator(threshold):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             resalt = func(*args, **kwargs)
#             for arg in args:
#                 if isinstance(arg, int):
# 
#                     if threshold > arg:
#                             return resalt
#                     else:
#                         raise ValueError('значение больше заданного')
# 
#             else:
#                 raise ValueError('тип данных не соответствует')
#         return wrapper
#     return decorator_inner
# @decorator(threshold=3)
# def summa_numb(a, b):
#     return a + b
# resalt = summa_numb(2, 0)
# print(resalt)'''
# Создайте декоратор, который принимает параметр "retry_delay"
# и повторяет выполнение функции с указанной задержкой при возникновении исключения.
'''# import time
# def decorator(retry_delay):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             time.sleep(retry_delay)
#             resalt = func(*args, **kwargs)
#             return resalt
#         return inner
#     return wrapper
# @decorator(retry_delay=2)
# def say_hello():
#     return "Hello, world!"
# resalt = say_hello()
# print(resalt)'''
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
