# Напишите декоратор, который принимает параметр "message" и выводит это сообщение перед выполнением функции.
'''# def decorator_out (message):
#     def decorator(func):
#         def wrapper( *args, **kwargs):
#             print(message)
#             resalt = func(*args, **kwargs)
#             return resalt
#         return wrapper
#     return decorator
# @decorator_out(message='а вот и наше сообщение!')
#
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
# Создайте декоратор, который принимает параметр "log_file" и записывает лог выполнения функции в указанный файл.
'''def decorator(file_name):
    def decorator_inner(func):
        def wrapper(*args, **kwargs):
            resalt = func(*args, **kwargs)
            with open(file_name, 'w', encoding='utf-8') as my_file:
               my_file.write(f"Вызвана функция {func.__name__} с аргументами {args} и результатом {resalt}\n")
            return resalt
        return wrapper
    return decorator_inner
@decorator(file_name='file_file.log')
def summa(*args):
    summa = 0
    for arg in args:
        for ele in arg:
            if isinstance(ele, int):
                summa += ele
    return f'{summa} сумма которая получилась'
lisat_num = [5, 4]
resalt = summa(lisat_num)
print(resalt)'''
# Создайте декоратор, который принимает параметр "max_result" и проверяет,
# что результат функции не превышает значение "max_result".
'''# def decorator_out(max_result):
#     def decorator_in(func):
#         def wrapper(*args, **kwargs):
#             resalt = func(*args, **kwargs)
#             if resalt < max_result:
#                 return resalt
#             else:
#                 raise ValueError('а превышает указанное значение!')
#         return  wrapper
#     return decorator_in
# @decorator_out(max_result=36)
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
# Напишите декоратор, который принимает параметр "allowed_args" в виде списка, и проверяет,
# что функция вызывается только с аргументами из этого списка.
'''# def decorator(allowed_args):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             for arg in args:
#                 if arg not in allowed_args:
#                     raise ValueError
#                 return func(*args, **kwargs)
#         return inner
#     return wrapper
# args_allowed = [2, 4, 48]
# 
# @decorator(allowed_args=args_allowed)
# def summa(a, b):
#     return a + b
# 
# resalt = summa(2, 4)
# print(resalt)'''
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