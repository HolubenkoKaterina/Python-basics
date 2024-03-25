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

