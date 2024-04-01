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
