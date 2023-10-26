# Создайте декоратор, который проверяет, что переданный аргумент больше заданного значения.
'''def decorator(value):
    def decorator_inner(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (list, tuple, str)):
                    for elem in arg:
                        if isinstance(elem, int):
                            if value <= elem:
                                raise ValueError('значение превышает указанное')
                            else:
                                return func(*args, **kwargs)
                        else:
                            raise ValueError('не тот тип данных')
        return wrapper
    return decorator_inner
@decorator(value=4)

def summa(*args):
    summa = 0
    for arg in args:
        for ele in arg:
            if isinstance(ele, int):
                summa += ele
    return summa
lisat_num = [5, 4]
resalt = summa(lisat_num)
print(resalt)'''
# # Создайте декоратор, который принимает список чисел и умножает результат функции на все элементы этого списка.
'''# def decorator():
#
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             for el in spisok:
#                 if type(el) == int:
#                     result *= el
#                 elif isinstance(el, str) and el.isdigit():
#                     result *= int(el)
#                 else:
#                     raise ValueError('тип данных не числовой!')
#             return result
#         return wrapper
#     return actual_decorator
#
# @decorator(spisok=data)
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
# Создайте декоратор, который принимает параметр "retry_count" и повторяет выполнение функции заданное количество
# раз в случае возникновения исключения.
'''# def decorator(retry_count):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(retry_count +1):
#                 try:
#                     resalt = func(*args, **kwargs)
#                     return resalt
#                 except Exception as ex:
#                     if _ == retry_count:
#                         raise ex
# 
#         return wrapper
#     return decorator_inner
# @decorator(retry_count=4)
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