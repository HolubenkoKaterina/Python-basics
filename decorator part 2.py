# Создайте декоратор, который принимает параметр "retry_count" и повторяет выполнение
# функции заданное количество раз в случае возникновения исключения.
'''# def decorator(retry_count):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#
#             for _ in range(retry_count):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Error occurred: {e}")
#             return ValueError("Exceeded retry attempts")
#         return inner
#     return wrapper
# @decorator(retry_count=4)
# def divide_by_zero(a, b):
#     return a / b
#
# resalt = divide_by_zero(4, 0)
# print(resalt)
'''
# Создайте декоратор, который принимает параметр "allow_users" (список пользователей)
# и разрешает выполнение функции только определенным пользователям.
'''# def decorator(allow_users):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             name = input('Введите имя: ').title()
#             if name in allow_users:
#                 return func(*args, **kwargs)
#             else:
#                 raise ValueError(f'Пользователь {name} не имеет доступа к выполнению этой функции')
#         return inner
#     return wrapper
# 
# allow_users = ['Mimi Lili', 'Lili Mimi', 'Kiki Vivi']
# 
# @decorator(allow_users)
# def hello():
#     print('Привет !')
# 
# result = hello()
# print(result)
'''
# Напишите декоратор, который принимает параметр "min_duration" и выводит предупреждение, если функция выполняется менее указанного времени.
'''# import time
# def decorator(min_duration):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             start = time.time()
#             resalt = func(*args, **kwargs)
#             finish = time.time()
#             res = finish - start
#             if res < min_duration:
#                 print(
#                     f"Предупреждение: Время выполнения функции {func.__name__} составило менее {min_duration} секунд.")
# 
#         return inner
#     return wrapper
# @decorator(min_duration=3)
# def long_running_function():
#     time.sleep(2)
#     print("Функция завершена")
# 
# resalt = long_running_function()
# print(resalt)'''